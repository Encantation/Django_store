from .models import *

menu = [{'title': 'Магазин', 'url_name': 'index'},
{'title': 'Каталог', 'url_name': 'catalog'},
{'title': 'Корзина', 'url_name': 'cart'},
{'title': 'О сайте', 'url_name': 'about'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.all()
        context['menu'] = menu
        context['cats'] = cats
        return context