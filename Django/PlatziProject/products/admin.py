from django.contrib import admin
from .models import Product, Favorite

# Register your models here.

# admin.site.register(Product)

@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'description', 'price',)
    list_filter = ('category',)

@admin.register(Favorite)
class AdminFavorites(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)
    