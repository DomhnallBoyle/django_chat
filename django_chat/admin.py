from django.contrib import admin
from django_chat.models import Message, Room, User

admin.site.register(Message)
admin.site.register(Room)
admin.site.register(User)
