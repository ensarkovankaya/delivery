import logging

logger = logging.getLogger(__name__)


def consume_new_order(message: str):
    """
    :param message:
    :return:
    """
    logger.info(f'Consumer received a message: {message}')
