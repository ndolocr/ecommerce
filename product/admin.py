from django.contrib import admin
from product.models import Restock
from product.models import Product
from product.models import Category

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
	readonly_fields = ('stock_level',)

admin.site.register(Restock)
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)