import uuid as uuid
from django.db import models


class Room(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.TextField()
    created_by = models.ForeignKey('User', related_name='created_by')
    admin = models.ForeignKey('User', related_name='admin')

    def __unicode__(self):
        return self.name

    @property
    def get_messages(self):
        return self.messages.order_by('timestamp')

    @property
    def number_of_users(self):
        return self.user_set.count()

    @property
    def members(self):
        members = ""
        for user in self.user_set.all():
            members += str(user.username) + ','
        return members
