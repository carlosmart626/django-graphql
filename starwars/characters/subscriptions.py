import graphene
from graphene_django_subscriptions import Subscription
from .serializers import HumanCharacterSerializer, DroidCharacterSerializer


class HumanCharacterSubscription(Subscription):
    class Meta:
        serializer_class = HumanCharacterSerializer
        stream = 'humans'
        description = 'Human Character Subscription'


class DroidCharacterSubscription(Subscription):
    class Meta:
        serializer_class = DroidCharacterSerializer
        stream = 'droids'
        description = 'Droid Character Subscription'
