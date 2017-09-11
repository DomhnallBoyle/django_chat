from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import TemplateView

from django_chat.forms import LoginForm


class Login(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('dashboard')
        else:
            return super(Login, self).get(request, args, kwargs)

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            login(request, form.user)
            return redirect('dashboard')
        else:
            return self.render_to_response({'form': form})
