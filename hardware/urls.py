from django.contrib import admin
from django.urls import path, include

from .views import *

urlpatterns = [
    path('', ShopIndex.as_view(), name='index'),
    path('catalog', CategoryView.as_view(), name='catalog'),
    path('catalog/<slug:cat_slug>', ShowCategory.as_view(), name='category'),
    path('item/<slug:item_slug>', ShowItem.as_view(), name='item'),
    path('cart/', ShopingCart.as_view(), name='cart'),
    path('about/', about, name='about'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),
]

