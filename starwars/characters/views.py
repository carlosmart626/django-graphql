from django.shortcuts import render
from rest_framework import viewsets

from django.http import HttpResponse
import datetime
from channels import Group

from .models import HumanCharacter, DroidCharacter
from .serializers import HumanCharacterSerializer, DroidCharacterSerializer


class HumanCharacterViewSet(viewsets.ModelViewSet):
    queryset = HumanCharacter.objects.all()
    serializer_class = HumanCharacterSerializer


class DroidCharacterViewSet(viewsets.ModelViewSet):
    queryset = DroidCharacter.objects.all()
    serializer_class = DroidCharacterSerializer


def current_datetime(request):
    now = datetime.datetime.now()
    Group("chat").send({
        "text": "Send from view!",
    })
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
