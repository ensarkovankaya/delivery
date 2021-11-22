from django.db.transaction import atomic

from rest_framework import serializers

from order.models import Order, OrderItem, OrderStatus
from restaurant.models import Restaurant, MenuItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['count', 'menu_item']


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'number', 'status', 'user', 'restaurant', 'items', 'created_at', 'modified_at']
        read_only_fields = ['id', 'number', 'status', 'user', 'created_at', 'modified_at']

    def create(self, validated_data: dict):
        restaurant: Restaurant = validated_data['restaurant']
        items: list[OrderItem] = validated_data['items']
        with atomic():
            for item in items:
                item.save()
            user = self._context['request'].user
            order = Order.objects.create(status=OrderStatus.CREATED, user=user, restaurant=restaurant)
            order.items.add(*items)
            return order

    def validate(self, attrs: dict) -> dict:
        # Validate requested order items are in restaurant menu
        restaurant: Restaurant = attrs['restaurant']
        restaurant_menu_items = {item_id for item_id in restaurant.menu.values_list('id', flat=True)}
        for order_item in attrs['items']:
            menu_item: MenuItem = order_item.menu_item
            if menu_item.id not in restaurant_menu_items:
                raise serializers.ValidationError(f'Item {menu_item} is not in restaurant menu')
        return attrs

    @staticmethod
    def validate_items(value: list[dict]) -> list[OrderItem]:
        if not value:
            raise serializers.ValidationError('At least one order item should be provided')
        return [OrderItem(count=item['count'], menu_item=item['menu_item']) for item in value]

    @staticmethod
    def get_status(instance: Order):
        return instance.get_status_display()
