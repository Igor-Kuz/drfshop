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
