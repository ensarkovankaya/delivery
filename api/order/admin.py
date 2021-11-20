from django.contrib import admin

from order.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('number',)
    list_display = ('number', 'status', 'user', 'restaurant')
    filter_horizontal = ('items',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
