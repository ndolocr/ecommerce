from django.contrib import admin
from product.models import Product
from product.models import Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)