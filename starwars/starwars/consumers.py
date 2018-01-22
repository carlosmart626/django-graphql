import json
import rx
from django.http import HttpResponse
from channels.handler import AsgiHandler
from api.schemas import schema
from channels.sessions import channel_session
from graphql.execution import execute


# In consumers.py
from channels import Group


# Connected to websocket.connect
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)


# Connected to websocket.receive
def ws_message(message):
    Group("chat").send({
        "text": message.content['text'],
    })


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)


def ws_GQL_connect(message):
    message.reply_channel.send({"accept": True})


def send(result, message):
    data = result.data
    message.reply_channel.send(
    {
        'text': str({'data': json.loads(json.dumps(data))})
    })


@channel_session
def ws_GQLData(message):
    clean = json.loads(message.content['text'])
    query = clean.get('query')
    foovar = clean.get('variables')
    # message.dataloaders = DataLoaders(get_language())
    kwargs = {'context_value': message}
    result = schema.execute(query, variable_values=foovar, allow_subscriptions=True, **kwargs)
    if isinstance(result, rx.Observable):
        class MyObserver(rx.Observer):
            def on_next(self, x):
                send(x, message)
            def on_error(self, e):
                pass
            def on_completed(self):                                                                                                                                                                                                                                                                                                                                                                                                   
                pass                                                                                                                                                                                                                                                                                                                                                                                                                 
        result.subscribe(MyObserver())                                                                                                                                                                                                                                                                                                                                                                                                
    else:                                                                                                                                                                                                                                                                                                                                                                                                                             
        send(result, message) 


def http_consumer(message):
    # Make standard HTTP response - access ASGI path attribute directly
    print(message)
    response = HttpResponse("Hello world! You asked for %s" % message.content['path'])
    # Encode that response into message format (ASGI)
    for chunk in AsgiHandler.encode_response(response):
        message.reply_channel.send(chunk)
