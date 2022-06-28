from django.db import models
from django.urls import reverse


class Goods(models.Model):
    title = models.CharField(max_length=255)
    photo = models.ImageField(upload_to="media/photos")
    price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.CharField(max_length=1000)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('cat', kwargs={'cat_slug': self.slug})
