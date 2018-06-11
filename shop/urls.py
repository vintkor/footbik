from django.urls import path, include
from .views import (
    ProductListView,
    CategoryListView,
    ProductDetailView,
)


app_name = 'shop'
urlpatterns = [
    path('', CategoryListView.as_view(), name='main-page'),
    path('<slug:slug>/', ProductListView.as_view(), name='products-in-category'),
    path('<slug:category_slug>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
]
