from dataclasses import fields
from abstract.serializers import BaseSerializer

from .models import Category, Product, Comment

class CategorySerializer(BaseSerializer): 
    class Meta: 
        fields = ['title']
        queryset = Category.objects

class ProductSerializer(BaseSerializer): 
    class Meta: 
        fields = ['title', 'price', 'desc', 'quantity']
        queryset = Product.objects

class CommentSerializer(BaseSerializer): 
    class Meta: 
        fields = ['body' 'created_at']
        queryset = Comment.objects