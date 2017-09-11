from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from django_chat.models import Room, User


class ChatRoom(TemplateView):
    template_name = 'room.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            room_name = request.GET.get('room_name')
            room = Room.objects.get(name=room_name)

            return self.render_to_response({
                'room': room
            })
        else:
            return redirect('login')


class CreateChatRoom(TemplateView):
    template_name = 'dashboard_room_list.html'

    def post(self, request):
        room_name = request.POST.get('room_name')
        if any(room.name == room_name for room in Room.objects.all()):
            return HttpResponse('Chatroom name already exists', status=500)

        created_by = User.objects.get(username=request.user.username)
        room = Room.objects.create(name=room_name, created_by=created_by, admin=created_by)

        users = request.POST.getlist('users[]', [])

        for username in users:
            user = User.objects.get(username=username)
            user.rooms.add(room)
        created_by.rooms.add(room)

        return self.render_to_response(
            {'rooms': created_by.rooms.all().order_by('name'), 'request': request}
        )


class DeleteChatRoom(TemplateView):
    template_name = 'dashboard_room_list.html'

    def post(self, request):
        room_name = request.POST.get('room_name')
        user = User.objects.get(username=request.user.username)
        Room.objects.get(name=room_name).delete()

        return self.render_to_response(
            {'rooms': user.rooms.all().order_by('name'), 'request': request}
        )


class EditChatRoom(TemplateView):
    template_name = 'dashboard_room_list.html'

    def post(self, request):
        old_room_name = request.POST.get('old_room_name')
        new_room_name = request.POST.get('new_room_name')
        admin_username = request.POST.get('admin')
        members = request.POST.getlist('members[]')

        room = Room.objects.get(name=old_room_name)
        logged_in_as = User.objects.get(username=request.user.username)

        if admin_username not in members:
            return HttpResponse('Admin not a member of the group.', status=500)

        # change members
        room.user_set.clear()
        for member in members:
            User.objects.get(username=member).rooms.add(room)

        # change room name
        if room.name != new_room_name:
            room.name = new_room_name

        # change admin
        if room.admin.username != admin_username:
            room.admin = User.objects.get(username=admin_username)

        room.save()

        return self.render_to_response(
            {'rooms': logged_in_as.rooms.all().order_by('name'), 'request': request}
        )
