from rest_framework import serializers
from .models import Category, Product, CartProduct, Cart, Order


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
        exclude = ("image",)


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


class ProductSerializer(serializers.ModelSerializer):
    """Добавление товара"""
    product = ProductDetailSerializer()

    class Meta:
        model = CartProduct
        fields = "__all__"


class CartSerializer(serializers.ModelSerializer):
    """отображение корзины"""
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
            'products'
        ]


class CreateCartSerializer(serializers.ModelSerializer):
    """добавление товара"""
    products = ProductSerializer(many=True)

    class Meta:
        model = Cart
        fields = [
           'owner', 'products'
        ]


class CreateOrderSerializer(serializers.ModelSerializer):
    """Создание заказа"""

    class Meta:
        model = Order
        exclude = ("customer", "status",)


class OrderSerializer(serializers.ModelSerializer):
    """Вывод заказа"""
    class Meta:
        model = Order
        fields = "__all__"
