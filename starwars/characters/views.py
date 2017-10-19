from django.shortcuts import render
from rest_framework import viewsets

from .models import HumanCharacter, DroidCharacter
from .serializers import HumanCharacterSerializer, DroidCharacterSerializer


class HumanCharacterViewSet(viewsets.ModelViewSet):
    queryset = HumanCharacter.objects.all()
    serializer_class = HumanCharacterSerializer


class DroidCharacterViewSet(viewsets.ModelViewSet):
    queryset = DroidCharacter.objects.all()
    serializer_class = DroidCharacterSerializer
