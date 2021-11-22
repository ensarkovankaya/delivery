from django.contrib import admin

from order.models import Order, OrderItem


class OrderAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_display = ('id', 'status', 'user', 'restaurant')
    filter_horizontal = ('items',)


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
