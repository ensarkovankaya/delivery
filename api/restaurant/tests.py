from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from restaurant.models import Restaurant, MenuItem, Cuisine


class RestaurantListViewTest(TestCase):
    fixtures = ['cuisine', 'menu_item', 'restaurant']
    ENDPOINT = reverse('restaurant:list')

    def test_list_restaurants(self):
        response = self.client.get(self.ENDPOINT)
        self.assertEqual(response.status_code, HTTPStatus.OK, msg=f'invalid response status code')

        payload = response.json()
        self.assertIs(type(payload), list, msg='invalid payload type')
        self.assertEqual(len(payload), 1, msg=f'expected one restaurant item but got {len(payload)}')

        for restaurant_data in payload:
            self.validate_restaurant(restaurant_data=restaurant_data)

    def validate_restaurant(self, restaurant_data: dict):
        self.assertIs(type(restaurant_data), dict, msg='invalid restaurant data type')
        self._assert_fields(fields=['id', 'name', 'menu', 'created_at', 'modified_at'], data=restaurant_data)

        restaurant = Restaurant.objects.get(id=restaurant_data['id'])
        self.assertEqual(restaurant.name, restaurant_data['name'])

        menu_data = restaurant_data['menu']
        self.assertIsInstance(menu_data, list, msg='invalid restaurant menu data')
        self.assertEqual(restaurant.menu.count(), len(menu_data))
        for menu_item_data in menu_data:
            self.validate_menu_item(item_data=menu_item_data)

    def validate_menu_item(self, item_data: dict):
        self.assertIs(type(item_data), dict, msg='invalid item data type')
        self._assert_fields(fields=['id', 'name', 'category', 'created_at', 'modified_at'], data=item_data)

        menu_item = MenuItem.objects.get(id=item_data['id'])
        self.assertEqual(menu_item.name, item_data['name'])
        self.validate_cuisine(cuisine_data=item_data['category'])

    def validate_cuisine(self, cuisine_data):
        self.assertIs(type(cuisine_data), dict, msg='invalid cuisine data type')
        self._assert_fields(fields=['id', 'name', 'created_at', 'modified_at'], data=cuisine_data)

        cuisine = Cuisine.objects.get(id=cuisine_data['id'])
        self.assertEqual(cuisine.name, cuisine_data['name'])

    def _assert_fields(self, fields, data: dict):
        for field in fields:
            self.assertIn(field, data, msg=f'expected data to have field: {field}')
