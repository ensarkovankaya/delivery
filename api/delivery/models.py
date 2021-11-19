from django.db import models


class Cuisine(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Dinner(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(to=Cuisine, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    menu = models.ManyToManyField(to=Dinner)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
