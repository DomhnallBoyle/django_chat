from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20)

    user = None
    error = None

    def is_valid(self):

        username = self.data['username']
        password = self.data['password']

        if username == '' or password == '':
            self.error = 'Username and Password are required.'

            return False

        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            self.error = 'User does not exist.'

            return False

        self.user = authenticate(username=username, password=password)

        if self.user:
            return True
        else:
            self.error = 'Incorrect password.'

            return False
