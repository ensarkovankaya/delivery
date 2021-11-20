from enum import IntEnum

from django.db import models
from django.contrib.auth import get_user_model


class Cuisine(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to=Cuisine, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    menu = models.ManyToManyField(to=MenuItem)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrderStatus(IntEnum):
    CREATED = 1
    PREPARING = 2
    ON_THE_WAY = 3
    DELIVERED = 4

    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls.__iter__()]


class Order(models.Model):
    number = models.CharField(max_length=5)
    status = models.PositiveSmallIntegerField(choices=OrderStatus.choices())

    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    items = models.ManyToManyField(to=MenuItem)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.number
