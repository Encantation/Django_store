from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Goods(models.Model):
    '''Goods model describing SQL table for items sold in the store'''

    title = models.CharField(max_length=255) #item name
    photo = models.ImageField(upload_to="media/photos", blank=True) #item picture
    price = models.IntegerField() #item price
    quantity = models.IntegerField() #number of items for sale
    description = models.CharField(max_length=1000) #general description
    category = models.ForeignKey('Category', on_delete=models.PROTECT) #item category
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL") #URL slug
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE) #user ID of entry creator

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})


class Category(models.Model):
    '''Category model for grouping items'''

    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
