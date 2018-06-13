from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import (
    Product,
    Category,
    CartItem,
)


class CategoryListView(ListView):
    """
    Отображение главной страницы магазина (Кабинет)
    """
    template_name = 'shop/main.html'
    context_object_name = 'categories'
    model = Category


class ProductListView(ListView):
    """
    Список товаров в выбраной категории магазина (Кабинет)
    """
    template_name = 'shop/category-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return category.get_products()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return context


class ProductDetailView(DetailView):
    """
    Детальное отображение одного товара в магазине (кабинет)
    """
    template_name = 'shop/product.html'
    context_object_name = 'product'

    def get_object(self, queryset=None):
        try:
            product = Product.objects.prefetch_related(
                'variant_set__value',
                'variant_set__value__parameter',
            ).get(slug=self.kwargs.get('slug'))
        except Product.DoesNotExist:
            raise Http404('Page not found')

        return product


class CartItemListView(ListView):
    """
    Корзина пользователя
    """
    template_name = 'shop/cart.html'
    context_object_name = 'cart_items'

    def get_queryset(self):
        return CartItem.objects.filter(cart__user=self.request.user)

    def get_context_data(self, *args, **kwargs):
        context = super(CartItemListView, self).get_context_data()
        context['cart_total'] = self.get_queryset().first().cart.get_cart_total_sum()
        return context
