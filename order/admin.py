from .models import Order,OrderItem
from django.contrib import admin


class ItemInline(admin.TabularInline):
    model=OrderItem


class OrderAdmin(admin.ModelAdmin):
    inlines = [
        ItemInline,
    ]

admin.site.register(Order,OrderAdmin)