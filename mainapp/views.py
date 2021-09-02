from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import rest_framework as filters
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import ProductListSerializer,  ProductDetailSerializer, CategoryListSerializer, \
                            CreateCartSerializer, CategoryCreateSerializer, CartSerializer, ProductSerializer

class ProductListView(APIView):
    """Вывод списка товаров"""
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetailView(APIView):
    """вывод отдельного продукта"""
    def get(self, request, pk):
        product = Product.objects.get(id=pk, )
        serializer = ProductDetailSerializer(product)
        return Response(serializer.data)


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')

    class Meta:
        model = Product
        fields = ['category', 'min_price', 'max_price']


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class CategoryPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10


class CategoryList(ListAPIView):
    """отображение категорий"""
    serializer_class = CategoryListSerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()


class CategoryCreateAPIView(APIView):
    """Добавление категории"""
    def post(self, request):
        category = CategoryCreateSerializer(data=request.data)
        if category.is_valid():
            category.save()
        return Response(status=201)


class ListCreateCategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):
    """Добавление категории через generics"""
    serializer_class = CategoryCreateSerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()
    lookup_field = 'id'


class CartListAPIView(APIView):
    """Отображение корзины"""
    def get(self, request):
        cart_list = Cart.objects.all()
        serializer = CartSerializer(cart_list, many=True)
        return Response(serializer.data)


# class CartCreateAPIView(APIView):
#     """добавление товара в корзину"""
#     def post(self, request):
#         cartproduct = CreateCartSerializer(data=request.data)
#         if cartproduct.is_valid():
#             cartproduct.save()
#         return Response(status=201)


class CartCreateAPIView(generics.CreateAPIView):
    """добавление товара в корзину"""
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer
    # def post(self, request):
    #     cartproduct = CreateCartSerializer(data=request.data)
    #     if cartproduct.is_valid():
    #         cartproduct.save()
    #     return Response(status=201)


class CartProductCreateAPIView(ListCreateAPIView, RetrieveUpdateAPIView):
    """Работем с классом cart product"""
    serializer_class = ProductSerializer
    queryset = CartProduct.objects.all()
    lookup_field = 'pk'