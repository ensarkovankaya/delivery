from enum import IntEnum

from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db import models

from restaurant.models import Restaurant, MenuItem


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


class Order(models.Model):
    number = models.CharField(max_length=5)
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices())

    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    items = models.ManyToManyField(to=OrderItem)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
