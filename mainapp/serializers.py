from rest_framework import serializers
from .models import Category, Product, CartProduct, Cart, Customer, Order


class ProductListSerializer(serializers.ModelSerializer):
    """ Список товаров"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class ProductDetailSerializer(serializers.ModelSerializer):
    """вывод одного товара"""
    category = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Product
        fields = "__all__"


class CategoryListSerializer(serializers.ModelSerializer):
    """отображение категорий"""
    name = serializers.CharField(required=True)
    slug = serializers.SlugField

    class Meta:
        model = Category
        fields = [
            'id', 'name', 'slug'
        ]


class CategoryCreateSerializer(serializers.ModelSerializer):
    """добавление категории"""

    class Meta:
        model = Category
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    """отображение корзины"""

    class Meta:
        model = Cart
        fields = [
            'category', 'title', 'description', 'price'
        ]


class CreateCartSerializer(serializers.ModelSerializer):
    """добавление товара"""
    class Meta:
        model = Cart
        fields = [
           'owner', 'products'
        ]


class ProductSerializer(serializers.ModelSerializer):
    """Добавление товара"""
    class Meta:
        model = CartProduct
        fields = "__all__"


class CreateOrderSerializer(serializers.ModelSerializer):
    """Создание заказа"""
    class Meta:
        model = Order
        exclude = ("customer", "status", 'cart')


class OrderSerializer(serializers.ModelSerializer):
    """Вывод заказа"""
    class Meta:
        model = Order
        fields = "__all__"
