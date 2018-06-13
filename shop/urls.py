from django.urls import path, include
from .views import (
    ProductListView,
    CategoryListView,
    ProductDetailView,
    CartItemListView,
)


app_name = 'shop'
urlpatterns = [
    path('', CategoryListView.as_view(), name='main-page'),
    path('cart/', CartItemListView.as_view(), name='cart'),
    path('<slug:slug>/', ProductListView.as_view(), name='products-in-category'),
    path('<slug:category_slug>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
]
