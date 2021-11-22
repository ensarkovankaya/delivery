from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('restaurant/', include(('restaurant.urls', 'restaurant'), namespace='restaurant')),
    path('order/', include(('order.urls', 'order'), namespace='order')),
    path('admin/', admin.site.urls),
]
