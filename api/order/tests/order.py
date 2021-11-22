import json
from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse

from restaurant.models import Restaurant, MenuItem


class OrderCreateTest(TestCase):
    fixtures = ['cuisine', 'menu_item', 'restaurant', 'order_item', 'order', 'user']
    ENDPOINT = reverse('order:list-create')
    FILED_REQUIRED_MESSAGE = 'This field is required.'
    ITEM_NOT_PROVIDED_MESSAGE = 'At least one order item should be provided'

    def test_restaurant_field_required(self):
        request_payload = self._get_request_payload()
        request_payload.pop('restaurant')
        response = self._call(payload=request_payload)
        self._validate_error_response(response=response, field='restaurant', message=self.FILED_REQUIRED_MESSAGE)

    def test_items_field_required(self):
        request_payload = self._get_request_payload()
        request_payload.pop('items')
        response = self._call(payload=request_payload)
        self._validate_error_response(response=response, field='items', message=self.FILED_REQUIRED_MESSAGE)

    def test_ordered_item_not_in_restaurant_menu(self):
        # Remove item from restaurant menu
        restaurant = Restaurant.objects.get(id=1)
        menu_item = MenuItem.objects.get(id=1)
        restaurant.menu.remove(menu_item)

        response = self._call(payload=self._get_request_payload())
        message = f'Item {menu_item} is not in restaurant menu'
        self._validate_error_response(response=response, field='non_field_errors', message=message)

    def test_no_item_ordered(self):
        request_payload = self._get_request_payload()
        request_payload['items'] = []
        response = self._call(payload=request_payload)
        self._validate_error_response(response=response, field='items', message=self.ITEM_NOT_PROVIDED_MESSAGE)

    def test_order_successful(self):
        response = self._call(payload=self._get_request_payload())
        self._validate_response_headers(response=response, status_code=HTTPStatus.OK)

    def _validate_error_response(self, response, field: str, message: str):
        self._validate_response_headers(response=response, status_code=HTTPStatus.BAD_REQUEST)
        payload = response.json()
        self.assertIs(type(payload), dict, msg='response content type not valid')
        self.assertIn(field, payload, msg=f'Field {field} not found in response payload')
        self.assertIs(type(payload[field]), list, msg=f'{field} not expected type')
        self.assertIn(message, payload[field])

    def _validate_response_headers(self, response, status_code: int):
        self.assertEqual(response.status_code, status_code, msg='response code not matched')
        self.assertEqual(response.headers.get('Content-Type'), 'application/json', msg='invalid content-type')

    def _call(self, payload):
        """Makes api call to testing endpoint
        :param payload: Request body content
        """
        return self.client.post(path=self.ENDPOINT, data=json.dumps(payload), content_type='application/json')

    @staticmethod
    def _get_request_payload() -> dict:
        return {
            'restaurant': 1,
            'items': [
                {
                    'count': 1,
                    'menu_item': 1,
                }
            ]
        }
