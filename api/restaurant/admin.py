from django.contrib import admin

from restaurant.models import Cuisine, MenuItem, Restaurant


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


admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
