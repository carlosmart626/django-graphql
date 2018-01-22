from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from jwt_auth.mixins import JSONWebTokenAuthMixin


from .schemas import schema


class AuthGraphQLView(JSONWebTokenAuthMixin, GraphQLView):
    pass


urlpatterns = [
  url(r'^require-auth/', csrf_exempt(AuthGraphQLView.as_view(schema=schema, graphiql=True))),
  url(r'^', csrf_exempt(GraphQLView.as_view(schema=schema, graphiql=True))),
]
