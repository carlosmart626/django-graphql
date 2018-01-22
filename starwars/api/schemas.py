
import graphene
import asyncio
import rx
from rx import Observable
from channels import Group
from graphene import ObjectType, Schema, relay, String, List, Int
from graphene_django.filter import DjangoFilterConnectionField
from graphene.utils.resolve_only_args import resolve_only_args
from django.conf import settings

from characters.schemas import HumanCharacterNode, DroidCharacterNode
from characters.mutations import UpdateHumanCharacter
from movies.schemas import MovieNode
from graphene_django.debug import DjangoDebug


def make_sub(info, gid):
    inst = relay.Node.get_node_from_global_id(info, gid)
    try:
        gp_name = 'gqp.{0}-updated.{1}'.format(str.lower(inst.__class__.__name__), inst.pk)
        Group(gp_name).add(info.context.reply_channel)
        info.context.channel_session['Groups'] = ','.join(
            (gp_name, info.context.channel_session['Groups']))
    except:
        pass
    return iter([inst])


class GlobalQuery(ObjectType):
    human = relay.Node.Field(HumanCharacterNode)
    humans_characters = DjangoFilterConnectionField(HumanCharacterNode)
    droid = relay.Node.Field(DroidCharacterNode)
    droid_characters = DjangoFilterConnectionField(DroidCharacterNode)
    movie = relay.Node.Field(MovieNode)
    movies = DjangoFilterConnectionField(MovieNode)
    if settings.DEBUG:
        debug = graphene.Field(DjangoDebug, name='__debug')
    node = relay.Node.Field()

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


class Subscription(graphene.ObjectType):

    sub_character = graphene.Field(HumanCharacterNode, description='subscribe to updated product', id=graphene.Int())

    def resolve_sub_character(self, info, **input):
        print("Resolve characters!!!")
        # return Observable.from_iterable(make_sub(info, input.get('sub_character')))

        # async def compat(result, delay):
        #     yield result
        #     await asyncio.sleep(delay)
        # return compat(make_sub(info, input.get('product')), .1)
        return Observable.interval(1000)\
                         .map(lambda i: "{0}".format(i))\
                         .take_while(lambda i: int(i) <= up_to)


schema = graphene.Schema(query=GlobalQuery, mutation=MutationRoot, subscription=Subscription)
