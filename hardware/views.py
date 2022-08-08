from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


from .permissions import *
from .utils import *
from .forms import *
from rest_framework import generics
from .serializers import GoodsSerializer

class ShopIndex(DataMixin, ListView):
    '''Index page of the store'''

    model = Goods
    template_name = 'hardware/index.html'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))


class CategoryView(DataMixin, ListView):
    '''Shows store catalog with all categories available'''

    model = Category
    template_name = 'hardware/catalog.html'
    context_object_name = 'cats'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Каталог")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Category.objects.order_by('name')


class ShowCategory(DataMixin, ListView):
    '''Shows all items that belong to selected category'''

    model = Goods
    template_name = 'hardware/show_category.html'
    slug_url_kwarg = 'cat_slug'
    context_object_name = 'goods'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Категория')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Goods.objects.filter(category__slug=self.kwargs['cat_slug'])


class ShowItem(DataMixin, DetailView):
    '''Detailed view for specific item'''

    model = Goods
    template_name = 'hardware/show_item.html'
    slug_url_kwarg = 'item_slug'
    context_object_name = 'item'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['item'])
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    '''New user registration form'''

    form_class = RegisterUserForm
    template_name = 'hardware/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

class LoginUser(DataMixin, LoginView):
    '''User login form'''

    form_class = LoginUserForm
    template_name = 'hardware/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')

def logout_user(request):
    logout(request)
    return redirect('login')


def cart(request):
    return render(request, 'hardware/catalog.html', {'menu': menu, 'title': 'Catalog'})

def about(request):
    return render(request, 'hardware/about.html', {'menu': menu, 'title': 'About'})



class GoodsAPIList(generics.ListCreateAPIView):
    '''API list for view purposes'''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class GoodsAPIUpdate(generics.RetrieveUpdateAPIView):
    '''API class for database entries update'''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAuthenticated, )


class GoodsAPIDestroy(generics.RetrieveDestroyAPIView):
    '''API class for databse entry deletion'''
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    permission_classes = (IsAdminOrReadOnly, )