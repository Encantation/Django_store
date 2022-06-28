from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ShopIndex.as_view(), name='index'),
    path('catalog', CategoryView.as_view(), name='catalog'),
    path('catalog/<slug:cat_slug>', CategoryView.as_view(), name='cat'),
    path('item/<slug:item_slug>', ShowItem.as_view(), name='item'),
    path('cart/', cart, name='cart'),
    path('about/', about, name='about'),
    path('log_in/', log_in, name='log_in'),

]

