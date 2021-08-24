from rest_framework import serializers
from .models import Category, Product, CartProduct, Cart, Customer, Order


class ProductListSerializer(serializers.ModelSerializer):
	""" Список товаров"""

	class Meta:
		model = Product
		fields = "__all__"