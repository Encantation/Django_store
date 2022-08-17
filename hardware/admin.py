from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    '''Settings for admin panel Goods model'''

    list_display = ('id', 'title', 'photo', 'price', 'quantity', 'description', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', )
    list_filter = ('category', )
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    '''Settings for admin panel Category model'''

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


class CartAdmin(admin.ModelAdmin):
    '''Settings for admin panel Category model'''

    list_display = ('user', 'item', 'quantity')
    list_display_links = ('user', 'item', 'quantity')
    search_fields = ('user',)


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(ShoppingCart, CartAdmin)