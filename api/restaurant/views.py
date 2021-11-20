from rest_framework import generics

from restaurant.models import Restaurant
from restaurant.serializers import RestaurantSerializer


class RestaurantListView(generics.ListAPIView):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
