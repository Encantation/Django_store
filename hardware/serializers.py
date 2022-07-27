from rest_framework import serializers
from .models import Category


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)

class GoodsSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.IntegerField()
    quantity = serializers.IntegerField()
    description = serializers.CharField(max_length=1000)
    category_id = serializers.IntegerField()
