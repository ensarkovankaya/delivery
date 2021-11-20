from django.contrib import admin

from delivery.models import Cuisine, MenuItem, Restaurant, Order


class CuisineAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_at', 'modified_at')


class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('category',)
    list_display = ('name', 'category', 'created_at', 'modified_at')


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_at', 'modified_at')
    filter_horizontal = ('menu',)


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('number',)
    list_filter = ('restaurant',)
    list_display = ('number', 'user', 'restaurant', 'created_at', 'modified_at')
    filter_horizontal = ('items', )


admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Order, OrderAdmin)
