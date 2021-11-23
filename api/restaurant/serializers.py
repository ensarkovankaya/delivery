from restaurant.models import Restaurant, MenuItem, Category

from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'created_at', 'modified_at']
        read_only_fields = ['created_at', 'modified_at']


class MenuItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'category', 'created_at', 'modified_at']
        read_only_fields = ['created_at', 'modified_at']


class RestaurantSerializer(serializers.ModelSerializer):
    menu = MenuItemSerializer(many=True)

    class Meta:
        model = Restaurant
        fields = ['id', 'name', 'menu', 'created_at', 'modified_at']
