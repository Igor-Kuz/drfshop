from django.urls import path
from .views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#    path("product/", ProductListView.as_view()),
    path("product/", ProductGListView.as_view()),
#    path("product/<int:pk>/", ProductDetailView.as_view()),
    path("product/<int:pk>/", ProductGDetailView.as_view()),
    path("product-filter/", ProductsList.as_view()),
    path("categorys/", CategoryList.as_view()),
    path("categories/", CategoryCreateAPIView.as_view()),
    path("create-categories/<str:id>/", ListCreateCategoryAPIView.as_view()),
    path("cart-list/", CartListAPIView.as_view()),
    path("cart-list2/<int:pk>/", CartListGAPIView.as_view()),
    path("cartproduct/", CartCreateAPIView.as_view()),
    path("newcartproduct/<int:pk>/", CartProductCreateAPIView.as_view()),
    path("create-order/", CreatOrderAPIView.as_view()),
    path("order/<int:pk>", OrderAPIView.as_view())
]
