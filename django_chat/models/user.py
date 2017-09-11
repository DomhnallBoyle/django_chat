from django.contrib.auth.models import User
from django.db import models


class User(User):

    rooms = models.ManyToManyField('Room')

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    @property
    def rooms_to_dict(self):
        to_dict = {}
        for room in self.rooms.all():
            to_dict[room.name] = [room.created_by, room.number_of_users]

        return to_dict
