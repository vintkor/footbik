from django.urls import path
from .views import (
    ProductListView,
    CategoryListView,
    ProductDetailView,
    CartItemListView,
    AddToCart,
    DeleteProductFromCartView,
)


app_name = 'shop'
urlpatterns = [
    path('', CategoryListView.as_view(), name='main-page'),
    path('cart/', CartItemListView.as_view(), name='cart'),
    path('cart/add/', AddToCart.as_view(), name='add-to-cart'),
    path('cart/delete/<int:cart_item_id>/', DeleteProductFromCartView.as_view(), name='delete-product-from-cart'),
    path('<slug:slug>/', ProductListView.as_view(), name='products-in-category'),
    path('<slug:category_slug>/<slug:slug>/', ProductDetailView.as_view(), name='product'),
]
