from django.utils import timezone
from django.db import models
from users.models import User


class Thread(models.Model):
    owner = models.ForeignKey(User, related_name='owner', on_delete=models.SET_NULL, null=True)
    header = models.TextField(max_length=50, blank=False)
    participants = models.ManyToManyField(User, related_name='participants')
    created_time = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']

    def __init__(self, *args, **kwargs):
        super(Thread, self).__init__(*args, **kwargs)
        self.created_time = self.created_time

    def save(self, *args, **kwargs):
        if not self.created_time and self.created_time:
            self.edited_date = timezone.now()
        super(Thread, self).save(*args, **kwargs)


class Message(models.Model):
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    text = models.TextField(max_length=2048, blank=False)
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE)
    is_read = models.ManyToManyField(User)
    created_time = models.DateTimeField(auto_now_add=True)
    edited_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_time']

    def __init__(self, *args, **kwargs):
        super(Message, self).__init__(*args, **kwargs)
        self.created_time = self.created_time

    def save(self, *args, **kwargs):
        if not self.created_time and self.created_time:
            self.edited_date = timezone.now()
        super(Message, self).save(*args, **kwargs)
