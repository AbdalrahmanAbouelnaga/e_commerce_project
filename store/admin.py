from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Category)
admin.site.register(models.SubCategory)


class ProductImagesInline(admin.TabularInline):
    model=models.ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImagesInline
    ]

admin.site.register(models.Product,ProductAdmin)