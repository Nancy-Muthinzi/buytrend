from django.contrib import admin
from .models import Category, Image, Product, Produce

# Register your models here.

admin.site.register(Category)
admin.site.register(Image)
admin.site.register(Product)
admin.site.register(Produce)

