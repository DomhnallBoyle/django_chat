from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView

from django_chat.models import Room, User


class Dashboard(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            username = request.user.username
            context = {
                'rooms': User.objects.get(username=username).rooms.all().order_by('name'),
                'users': User.objects.exclude(username=username).order_by('first_name')
            }
            return self.render_to_response(context=context)
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        return HttpResponse('No')
