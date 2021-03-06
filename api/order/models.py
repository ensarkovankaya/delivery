from enum import IntEnum

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from restaurant.models import Restaurant, MenuItem
from utils.redis import Channel, pub_sub


class OrderStatus(IntEnum):
    CREATED = 1
    PREPARING = 2
    ON_THE_WAY = 3
    DELIVERED = 4

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls.__iter__()]


class OrderItem(models.Model):
    count = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])
    menu_item = models.ForeignKey(to=MenuItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.menu_item} ( x{self.count} )"


class Order(models.Model):
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices())

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    items = models.ManyToManyField(to=OrderItem)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=Order, dispatch_uid="order")
def publish_order(sender, instance, created, **kwargs):
    if created:
        pub_sub.publish(Channel.ORDER_CREATED, instance.id)
    else:
        pub_sub.publish(Channel.ORDER_UPDATED, instance.id)
