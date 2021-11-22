from django.test import TestCase

from order.models import Order, OrderStatus
from order.consumers import consume_new_order

from utils.redis import Channel


class ConsumeNewOrderTest(TestCase):
    fixtures = ['cuisine', 'menu_item', 'restaurant', 'order_item', 'order', 'user']
    NONE_EXISTS_ORDER_ID = 3

    def test_order_not_found(self):
        self.assertRaises(Order.DoesNotExist, consume_new_order, self._get_consumer_message(self.NONE_EXISTS_ORDER_ID))

    def test_order_completed(self):
        # Set order status to created
        order = self.get_order()
        order.status = OrderStatus.CREATED
        order.save()

        consume_new_order(self._get_consumer_message(order.id))
        # validate order status changed
        order = self.get_order()
        self.assertEqual(order.status, OrderStatus.DELIVERED)

    @staticmethod
    def get_order():
        return Order.objects.get(id=1)

    @staticmethod
    def _get_consumer_message(data) -> dict:
        return {'type': 'message', 'pattern': None, 'channel': Channel.ORDER_CREATED, 'data': str(data)}
