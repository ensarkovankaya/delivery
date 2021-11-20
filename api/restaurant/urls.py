from django.urls import path

from restaurant.views import RestaurantListView

urlpatterns = [
    path('', RestaurantListView.as_view(), name='list')
]
