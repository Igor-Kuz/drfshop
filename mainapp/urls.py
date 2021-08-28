from django.urls import path
from . views import *

urlpatterns = [
    path("product/", ProductListView.as_view()),
    path("product/<int:pk>/", ProductDetailView.as_view()),
    path("product-filter/", ProductsList.as_view()),
    path("categorys/", CategoryList.as_view()),
    path("categories/", CategoryCreateAPIView.as_view()),
]