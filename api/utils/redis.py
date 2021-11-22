import time
from typing import Callable

import redis
from django.conf import settings

from utils.singleton import Singleton


class PubSubClient(metaclass=Singleton):
    INTERVAL = 1000

    def __init__(self):
        self.redis_client = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIS_PORT)
        self.pub_sub_client = self.redis_client.pubsub()

    def register(self, channel: str, func: Callable):
        self.pub_sub_client.subscribe(**{channel: func})

    def publish(self, channel: str, message):
        self.redis_client.publish(channel=channel, message=message)

    def listen(self):
        while True:
            self.pub_sub_client.get_message()
            time.sleep(self.INTERVAL)


pub_sub = PubSubClient()
