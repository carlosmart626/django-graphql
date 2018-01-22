from graphene import relay, String, resolve_only_args
from graphene_django import DjangoObjectType

from .models import HumanCharacter, DroidCharacter
from movies.schemas import MovieNode
from movies.models import Movie


class MovieConnection(relay.Connection):

    class Meta:
        node = MovieNode

    class Edge:
        other = String()


class HumanCharacterNode(DjangoObjectType):

    appears_in = relay.ConnectionField(MovieConnection, description='Apariciones')

    @resolve_only_args
    def resolve_appears_in(self):
        return self.appears_in.all()

    class Meta:
        model = HumanCharacter
        filter_fields = []
        interfaces = (relay.Node,)


class DroidCharacterNode(DjangoObjectType):

    class Meta:
        model = DroidCharacter
        filter_fields = []
        interfaces = (relay.Node,)
