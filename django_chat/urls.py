import os

from django.conf import settings
from django.conf.urls import include, url, patterns
from django.contrib import admin

from views import ChatRoom, CreateChatRoom, Dashboard, DeleteChatRoom, EditChatRoom, Login, Logout, User

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', Login.as_view(), name='login'),
    url(r'^logout/$', Logout.as_view(), name='logout'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),

    url(r'^room/$', ChatRoom.as_view(), name='chatroom'),
    url(r'^create_room/$', CreateChatRoom.as_view(), name='create_chatroom'),
    url(r'^delete_room/$', DeleteChatRoom.as_view(), name='delete_chatroom'),
    url(r'^edit_room/$', EditChatRoom.as_view(), name='edit_chatroom'),

    url(r'^user/$', User.as_view(), name='user'),

    # url(r'^new/$', views.new_room, name='new_room'),
    # url(r'^(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]
