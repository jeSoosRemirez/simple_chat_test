from django.urls import path
from threads.views import (
    ThreadListCreateView, ThreadDeleteView,
    MessageListCreateView,
    api_root
)
from rest_framework.urlpatterns import format_suffix_patterns


# API endpoints
urlpatterns = format_suffix_patterns([
    path('', api_root),

    # Threads
    path('threads/', ThreadListCreateView.as_view(), name='thread-list-create'),
    path('threads/<int:id>/', ThreadDeleteView.as_view(), name='thread-delete'),

    # Messages
    path('threads/<int:thread>/messages/', MessageListCreateView.as_view(), name='message-list-create'),
])

