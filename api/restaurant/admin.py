from django.contrib import admin

from restaurant.models import Category, MenuItem, Restaurant


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'created_at', 'modified_at')


class MenuItemAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('category',)
    list_display = ('id', 'name', 'category', 'created_at', 'modified_at')


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name', 'created_at', 'modified_at')
    filter_horizontal = ('menu',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
