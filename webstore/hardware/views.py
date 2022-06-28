from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import *
from django.views.generic import ListView, DetailView


menu = [{'title': 'Catalog', 'url_name': 'catalog'},
{'title': 'Shopping cart', 'url_name': 'cart'},
{'title': 'About', 'url_name': 'about'},
{'title': 'Log in', 'url_name': 'log_in'}
        ]

class ShopIndex(ListView):
    model = Goods
    template_name = 'hardware/index.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Main page'
        return context


# def index(request):
#     goods = Goods.objects.all()
#     context = {
#         'goods': goods,
#         'menu': menu,
#         'title': 'Main page'
#     }
#     return render(request, 'hardware/index.html', context=context)

class CategoryView(ListView):
    model = Category
    template_name = 'hardware/catalog.html'
    context_object_name = 'cats'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Catalog'
        return context

    def get_queryset(self):
        return Category.objects.order_by('name')



    # def catalog(request):
#     goods = Goods.objects.all()
#     context = {
#         'goods': goods,
#         'menu': menu,
#         'title': 'Catalog'
#     }
#     return render(request, 'hardware/catalog.html', context=context)

def cart(request):
    return render(request, 'hardware/catalog.html', {'menu': menu, 'title': 'Catalog'})

def about(request):
    return render(request, 'hardware/about.html', {'menu': menu, 'title': 'About'})

def log_in(request):
    return render(request, 'hardware/catalog.html', {'menu': menu, 'title': 'Catalog'})

class ShowItem(DetailView):
    model = Goods
    template_name = 'hardware/show_item.html'
    slug_url_kwarg = 'item_slug'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = context['item']
        return context


# def show_item(request, item_slug):
#     g = get_object_or_404(Goods, slug=item_slug)
#     context = {
#         'g': g,
#         'menu': menu,
#         'title': g.title
#     }
#     return render(request, 'hardware/show_item.html', context=context)

def show_category(request):

    return render(request, 'hardware/catalog.html', {'menu': menu, 'title': 'Catalog'})