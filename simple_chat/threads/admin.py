from django.contrib import admin
from .models import Thread, Message


class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'header', 'created_time', 'edited_date')
    list_filter = ('owner', 'created_time')
    search_fields = ('owner', 'header')


class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'thread', 'created_time', 'edited_date')
    list_filter = ('sender', 'thread', 'created_time')
    search_fields = ('sender', 'thread')


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Message, MessageAdmin)