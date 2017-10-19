import graphene
from graphene import ObjectType, Schema, relay, String, List, Int
from graphene_django.filter import DjangoFilterConnectionField
from graphene.utils.resolve_only_args import resolve_only_args

from characters.schemas import HumanCharacterNode, DroidCharacterNode
from characters.mutations import UpdateHumanCharacter
from movies.schemas import MovieNode


class GlobalQuery(ObjectType):
    human = relay.Node.Field(HumanCharacterNode)
    humans_characters = DjangoFilterConnectionField(HumanCharacterNode)
    driod = relay.Node.Field(DroidCharacterNode)
    driod_characters = DjangoFilterConnectionField(DroidCharacterNode)
    movie = relay.Node.Field(MovieNode)
    movies = DjangoFilterConnectionField(MovieNode)

    it_works = graphene.String()
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    @resolve_only_args
    def resolve_it_works(self):
        return 'It works!'

    def resolve_hello(root, args, context, info):
        print(args)
        return 'Hello, {}'.format(args.get('name'))


class MutationRoot(ObjectType):
    """
    MutationRoot
    """
    update_human = UpdateHumanCharacter.Field()


schema = graphene.Schema(query=GlobalQuery, mutation=MutationRoot)
