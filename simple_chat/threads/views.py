from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from threads.models import Thread, Message
from threads.serializers import (
    ThreadListCreateSerializer, ThreadDeleteSerializer,
    MessageListCreateSerializer
                                 )
from users.backends import JWTAuthentication


class ThreadListCreateView(ListCreateAPIView):
    """
    This APIView provides `list` and `create` action
    with 'id', 'header', 'participants', 'created_time'
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Thread.objects.all()
    serializer_class = ThreadListCreateSerializer

    def perform_create(self, serializer):
        if serializer.is_valid():
            owner = self.request.user
            thread = Thread.objects.create()
            thread.participants.add(owner)
            serializer.save(owner=self.request.user)

            return Response(serializer.data)
        # try:
        #     participants = self.request.data.get('participants')
        #     thread = Thread.objects.filter(participants__in=participants).distinct()
        # except TypeError:
        #     # The request user is set as owner automatically.
        #     serializer.save(owner=self.request.user, participants=self.request.user)

        return Response(serializer.data)


class ThreadDeleteView(GenericAPIView):
    """
    This APIView provides 'delete' action with 'id'
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = ThreadDeleteSerializer

    def delete(self, request, id=None):
        queryset = Thread.objects.filter(id=id)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MessageListCreateView(ListCreateAPIView):
    """
    This APIView provides `list` action
    with 'sender', 'text', 'is_read', 'created_time'
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    serializer_class = MessageListCreateSerializer

    def get_queryset(self):
        # Return a list of messages in thread.
        thread = self.kwargs['thread']
        queryset = Message.objects.all()
        if thread is not None:
            queryset = queryset.filter(thread=thread)

        # The request user is added in 'is_read' field
        cur_user = self.request.user
        for message in queryset:
            if cur_user not in message.is_read.all():
                message.is_read.add(cur_user)

        return queryset

    def post(self, request, thread):
        # The request user is set as sender and
        # added to thread as participator.
        serializer = self.get_serializer(data={**request.data})
        if serializer.is_valid():
            sender = self.request.user

            # Get the Thread instance with the given thread_id
            thread = Thread.objects.get(id=thread)

            # Add the sender to the participants list of the Thread instance
            thread.participants.add(sender)
            serializer.save(sender=sender, thread=thread)

            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # Thread and message api roots
        'thread-list-create': reverse('thread-list-create', request=request, format=format),
        'message-list-create': reverse('message-list-create', request=request, format=format),

        # User api roots
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'update': reverse('update', request=request, format=format),
    })
