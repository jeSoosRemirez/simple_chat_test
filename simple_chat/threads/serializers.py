from rest_framework import serializers
from threads.models import Thread, Message


class ThreadListCreateSerializer(serializers.ModelSerializer):
    """
    Shows when we see a list of threads
    or want to create one
    """
    class Meta:
        model = Thread
        fields = ['id', 'header', 'participants', 'created_time']
        extra_kwargs = {'participants': {'read_only': True}}


class ThreadDeleteSerializer(serializers.ModelSerializer):
    """
    Shows when we're deleting a thread
    """
    class Meta:
        model = Thread
        fields = ['id']


class MessageListCreateSerializer(serializers.ModelSerializer):
    """
    Shows when we see a list of messages in thread
    """
    class Meta:
        model = Message
        fields = ['thread', 'sender', 'text', 'is_read', 'created_time']
        extra_kwargs = {
            'is_read': {'read_only': True},
            'thread': {'read_only': True},
            'sender': {'read_only': True}
        }
