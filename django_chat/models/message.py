from __future__ import unicode_literals

import uuid as uuid
from django.db import models
from django.utils import timezone


class Message(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room = models.ForeignKey('Room', related_name='messages')
    sender = models.ForeignKey('User')
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    @property
    def handle(self):
        return self.sender.username

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%d/%m/%Y %H:%M %p')

    @property
    def as_dict(self):
        return {'handle': self.handle, 'message': self.message, 'timestamp': self.formatted_timestamp}
