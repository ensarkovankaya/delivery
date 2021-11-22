from django.apps import AppConfig


class OrderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'order'

    def ready(self):
        """Register consumers to pub sub client
        """
        from order.consumers import consume_new_order
        from utils.redis import Channel, pub_sub
        pub_sub.register(Channel.ORDER_CREATED, consume_new_order)
