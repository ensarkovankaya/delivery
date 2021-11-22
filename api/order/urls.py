from django.urls import path

from order.views import OrderViewSet

urlpatterns = [
    path('', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='list-create'),
]
