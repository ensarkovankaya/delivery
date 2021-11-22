import time
import random
import logging

from order.models import Order, OrderStatus

logger = logging.getLogger(__name__)


def consume_new_order(message: dict):
    """This consumer emulates an order lifecycle by changing order status
    CREATED -> PREPARING -> ON_THE_WAY -> DELIVERED
    :param dict message:
    """
    logger.info(f'Consumer received a message: {message}')
    order_id = int(message['data'])
    try:
        order = Order.objects.get(id=order_id)
    except Order.DoesNotExist:
        logger.error(f'Order not found with id: {order_id}')
        raise

    for status in [OrderStatus.PREPARING, OrderStatus.ON_THE_WAY, OrderStatus.DELIVERED]:
        time.sleep(random.randint(3, 5))  # wait between 3 to 5 second
        order.status = status.value
        order.save()
        logger.info(f'Order<{order_id}> status changed to {status.name}')
