
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
from characters.subscriptions import HumanCharacterSubscription, DroidCharacterSubscription


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


class Subscriptions(graphene.ObjectType):
    human_subscription = HumanCharacterSubscription.Field()
    droid_subscription = DroidCharacterSubscription.Field()


schema = graphene.Schema(
    query=GlobalQuery, mutation=MutationRoot, subscription=Subscriptions)
