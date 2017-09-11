import json

from django.http import HttpResponse
from django.views.generic import View

from django_chat.models import User as Member


class User(View):

    def get(self, request, *args, **kwargs):
        username = request.GET.get('term')

        # TODO: MUST CHECK IF MEMBER INSIDE ROOM
        users = Member.objects.filter(username__icontains=username)

        results = []
        for user in users:
            results.append({
                'id': user.id,
                'label': user.full_name,
                'value': user.username
            })
        data = json.dumps(results)

        return HttpResponse(data, 'application/json')
