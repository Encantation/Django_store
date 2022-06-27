from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('catalog/', catalog, name='catalog'),
    path('cart/', cart, name='cart'),
    path('about/', about, name='about'),
    path('log_in/', log_in, name='log_in'),
    path('item/<slug:item_slug>', show_item, name='item'),
    path('category/', category, name='category'),
]
