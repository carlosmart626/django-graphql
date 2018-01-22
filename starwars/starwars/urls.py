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
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework import routers

from channels.routing import route_class, route
from graphql_ws.django_channels import GraphQLSubscriptionConsumer

from characters.views import HumanCharacterViewSet, DroidCharacterViewSet, current_datetime
from movies.views import MovieViewSet

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

channel_routing = [
    route_class(GraphQLSubscriptionConsumer, path=r"^/subscriptions"),
    route("http.request", "starwars.consumers.http_consumer", path=r"^/test"),
    # route("websocket.connect", "starwars.consumers.ws_add", path=r"^/test2"),
    # route("websocket.receive", "starwars.consumers.ws_message", path=r"^/test2"),
    # route("websocket.disconnect", "starwars.consumers.ws_disconnect", path=r"^/test2"),
    route('http.request', ws_GQLData, path=r"^/gql"),
    route('websocket.connect', ws_GQL_connect, path=r"^/gql"),
    route('websocket.receive', ws_GQLData, path=r"^/gql")

]
