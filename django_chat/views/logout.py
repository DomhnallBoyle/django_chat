from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import View


class Logout(View):

    def get(self, request):
        logout(request)

        return redirect('login')
