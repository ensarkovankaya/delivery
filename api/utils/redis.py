import enum
from typing import Callable

import redis
from django.conf import settings

from utils.singleton import Singleton


class Channel(enum.Enum):
    ORDER = 'order'
    ORDER_CREATED = ORDER + '.created'
    ORDER_UPDATED = ORDER + '.updated'


class PubSubClient(metaclass=Singleton):

    def __init__(self):
        self.redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
        self.pub_sub_client = self.redis_client.pubsub()

    def register(self, channel: Channel, func: Callable):
        self.pub_sub_client.subscribe(**{channel.value: func})

    def publish(self, channel: Channel, message):
        self.redis_client.publish(channel=channel.value, message=message)

    def listen(self, *args, **kwargs):
        return self.pub_sub_client.listen(*args, **kwargs)


pub_sub = PubSubClient()
