from graphene import relay, String, List, resolve_only_args
from graphene_django import DjangoObjectType

from .models import HumanCharacter, DroidCharacter
from movies.schemas import MovieNode


class HumanCharacterNode(DjangoObjectType):

    appears_in = relay.ConnectionField(MovieNode, description='Apariciones')

    @resolve_only_args
    def resolve_appears_in(self):
        return self.appears_in.all()

    class Meta:
        model = HumanCharacter
        interfaces = (relay.Node,)


class DroidCharacterNode(DjangoObjectType):

    class Meta:
        model = DroidCharacter
        interfaces = (relay.Node,)
