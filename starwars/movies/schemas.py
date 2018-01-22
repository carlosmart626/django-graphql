from graphene import relay, String, List, resolve_only_args
from graphene_django import DjangoObjectType

from .models import Movie


class MovieNode(DjangoObjectType):

    class Meta:
        model = Movie
        filter_fields = []
        interfaces = (relay.Node,)
