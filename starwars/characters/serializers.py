from rest_framework import serializers

from .models import HumanCharacter, DroidCharacter


class HumanCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HumanCharacter
        fields = ('name', 'friends', 'appears_in', 'home_planet')


class DroidCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroidCharacter
        fields = ('name', 'appears_in', 'primary_function')
