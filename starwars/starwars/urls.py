"""starwars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
import channels
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers
from channels.routing import route_class, route
from graphql_ws.django_channels import GraphQLSubscriptionConsumer

from characters.views import HumanCharacterViewSet, DroidCharacterViewSet, current_datetime
from movies.views import MovieViewSet
from characters.subscriptions import HumanCharacterSubscription, DroidCharacterSubscription
from graphene_django_subscriptions import GraphqlAPIDemultiplexer

from starwars.consumers import ws_GQLData, ws_GQL_connect

router = routers.DefaultRouter()
router.register(r'human-characters', HumanCharacterViewSet)
router.register(r'driod-characters', DroidCharacterViewSet)
router.register(r'movies', MovieViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api-rest/', include(router.urls)),
    url(r'^api-graphql/', include('api.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^date-test/', current_datetime)
]

class CustomAppDemultiplexer(GraphqlAPIDemultiplexer):
    consumers = {
        'humans': HumanCharacterSubscription.get_binding().consumer,
        'droids': DroidCharacterSubscription.get_binding().consumer
    }


app_routing = [
    route_class(CustomAppDemultiplexer)
]

project_routing = [
    channels.include("starwars.urls.app_routing",
            path=r"^/subscriptions"),
]
