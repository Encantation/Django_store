"""webstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from hardware.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hardware.urls')),
    path('api/v1/drf-auth/', include('rest_framework.urls')), #session authentication
    path('api/v1/auth/', include('djoser.urls')),
    #re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('api/v1/goods/', GoodsAPIList.as_view()), #API view all goods
    path('api/v1/goods/<int:pk>/', GoodsAPIUpdate.as_view()), #API view for specific item
    path('api/v1/goodsdelete/<int:pk>/', GoodsAPIDestroy.as_view()), #API delete specific item
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)