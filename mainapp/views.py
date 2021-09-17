from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from django_filters import rest_framework as filters
from rest_framework import generics, permissions
from rest_framework.pagination import PageNumberPagination
from .models import *
from .serializers import ProductListSerializer,  ProductDetailSerializer, CategoryListSerializer, \
                            CreateCartSerializer, CategoryCreateSerializer, CartSerializer, ProductSerializer, \
                            CreateOrderSerializer, OrderSerializer


class ProductListView(generics.ListAPIView):
    """Вывод списка продуктов"""
    serializer_class = ProductListSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        products = Product.objects.all()
        return products


class ProductDetailView(generics.RetrieveAPIView):
    """вывод отдельного продукта"""
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    """Поиск продукта"""
    min_price = filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = filters.NumberFilter(field_name='price', lookup_expr='lte')
    category = CharFilterInFilter(field_name='category__name', lookup_expr='in')
    title = CharFilterInFilter(field_name='title', lookup_expr='in')  # iexact, icontains?

    class Meta:
        model = Product
        fields = ['category', 'title', 'min_price', 'max_price']


class ProductsList(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter


class CategoryPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 10
#  remember ordering!


class CategoryList(generics.ListAPIView):
    """отображение категорий"""
    serializer_class = CategoryListSerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()


class CreateCategoryAPIView(ListCreateAPIView, RetrieveUpdateAPIView):
    """Добавление категории"""
    serializer_class = CategoryCreateSerializer
    pagination_class = CategoryPagination
    queryset = Category.objects.all()
    lookup_field = 'id'
    # int : id?


class CartListAPIView(generics.ListAPIView):
    """Отображение корзины"""
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(owner=self.request.user.customer, in_order=False)


class CartCreateAPIView(generics.CreateAPIView):
    """добавление товара в корзину"""
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer


class CartProductCreateAPIView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    """Работем с классом cart product"""
    serializer_class = ProductSerializer
    queryset = CartProduct.objects.all()
    lookup_field = 'pk'


class CreatOrderAPIView(generics.ListCreateAPIView):
    """создание нового заказа"""
    serializer_class = CreateOrderSerializer
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer)

    def perform_create(self, serializer):
        cart = Cart.objects.get(owner=self.request.user.customer, in_order=False, total_products__gte=1)
        # products not null
        serializer.save(cart=cart, customer=self.request.user.customer)
        cart.in_order = True
        cart.save()
        Cart.objects.create(owner=self.request.user.customer)  # Создаёт объекты админке в Cart и Order
        # Order.objects.create(customer=self.request.user.customer)  # создаёт 2 обекта в админке в поле Orders один
        # с данными заказа, второй пустой с незаполнеными полями
        # или в модели задать условие что cart null=False в модели Order


class OrderAPIView(generics.RetrieveAPIView):
    """Отображение заказа"""
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(customer=self.request.user.customer)


# в заказе не должно быть нулевых пролдуктов
