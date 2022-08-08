from rest_framework import serializers
from .models import Category, Goods


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    slug = serializers.SlugField(max_length=255)

class GoodsSerializer(serializers.ModelSerializer):
    '''API serializer for Goods model'''
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    '''Meta class to get all database entries and return all fields to serializer'''
    class Meta:
        model = Goods
        fields = ("__all__")