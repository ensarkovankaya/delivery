from restaurant.models import Restaurant, MenuItem, Cuisine

from rest_framework import serializers


class CuisineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuisine
        fields = ['id', 'name', 'created_at', 'modified_at']
        read_only_fields = ['created_at', 'modified_at']


class MenuItemSerializer(serializers.ModelSerializer):
    category = CuisineSerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'category', 'created_at', 'modified_at']
        read_only_fields = ['created_at', 'modified_at']


class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuItemSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'menu', 'created_at', 'modified_at']
