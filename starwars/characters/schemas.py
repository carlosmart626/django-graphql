from graphene import relay, String, List, resolve_only_args
from graphene_django import DjangoObjectType

from .models import HumanCharacter, DroidCharacter


class HumanCharacterNode(DjangoObjectType):

    class Meta:
        model = HumanCharacter
        interfaces = (relay.Node,)


class DroidCharacterNode(DjangoObjectType):

    class Meta:
        model = DroidCharacter
        interfaces = (relay.Node,)
