from django.contrib import admin

from delivery.models import Cuisine, Dinner, Restaurant


class CuisineAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'created_at', 'modified_at')


class DinnerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_filter = ('category', )
    list_display = ('name', 'category', 'created_at', 'modified_at')


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ('name', )
    list_display = ('name', 'created_at', 'modified_at')
    filter_horizontal = ('menu',)


admin.site.register(Cuisine, CuisineAdmin)
admin.site.register(Dinner, DinnerAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
