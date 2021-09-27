from .models import Category, Product , CartProduct, Cart
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = '__all__'
    
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'

class CartCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cart
        exclude = ('created','status','count','summ')

class CartProductCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = CartProduct
        fields = "__all__" 