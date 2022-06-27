from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *

menu = [{'title': 'Catalog', 'url_name': 'catalog'},
{'title': 'Shopping cart', 'url_name': 'cart'},
{'title': 'About', 'url_name': 'about'},
{'title': 'Log in', 'url_name': 'log_in'}
        ]

def index(request):
    goods = Goods.objects.all()
    context = {
        'goods': goods,
        'menu': menu,
        'title': 'Main page'
    }
    return render(request, 'hardware/index.html', context=context)


def catalog(request):
    goods = Goods.objects.all()
    context = {
        'goods': goods,
        'menu': menu,
        'title': 'Catalog'
    }
    return render(request, 'hardware/catalog.html', context=context)

def cart(request):
    return render(request, 'hardware/catalog.html', {'menu': menu, 'title': 'Catalog'})

def about(request):
    return render(request, 'hardware/about.html', {'menu': menu, 'title': 'About'})

def log_in(request):
    return render(request, 'hardware/catalog.html', {'menu': menu, 'title': 'Catalog'})

def show_item(request, item_slug):
    g = get_object_or_404(Goods, slug=item_slug)
    context = {
        'g': g,
        'menu': menu,
        'title': g.title
    }
    return render(request, 'hardware/show_item.html', context=context)

def category(request):
    return render(request, 'hardware/catalog.html', {'menu': menu, 'title': 'Catalog'})