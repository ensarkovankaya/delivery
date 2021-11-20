from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('restaurant/', include(('restaurant.urls', 'restaurant'), namespace='restaurant')),
    path('admin/', admin.site.urls),
]
