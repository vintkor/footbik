from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, DetailView
from .models import (
    Product,
    Category,
    CartItem,
    Variant,
    Cart)
from django.contrib import messages
from django.utils.translation import ugettext as _


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
        return CartItem.objects.filter(cart__user=self.request.user, cart__is_complete=False)

    def get_context_data(self, *args, **kwargs):
        context = super(CartItemListView, self).get_context_data()
        try:
            context['cart_total'] = self.get_queryset().first().cart.get_cart_total_sum()
        except:
            pass
        return context


class AddToCart(View):
    """
    Добавление товара в корзину
    """

    def post(self, request):
        variant_id = int(self.request.POST.get('variant'))
        quantity = int(self.request.POST.get('quantity'))
        variant = get_object_or_404(Variant, pk=variant_id)
        user = self.request.user

        try:
            cart = Cart.objects.get(user=user, is_complete=False)
        except Cart.DoesNotExist:
            cart = Cart(user=user)
            cart.save()

        try:
            cart_item = CartItem.objects.get(
                cart__user=user,
                variant=variant,
            )
            cart_item.quantity = cart_item.quantity + quantity
        except CartItem.DoesNotExist:
            cart_item = CartItem()
            cart_item.quantity = quantity

        cart_item.cart = cart
        cart_item.variant = variant
        cart_item.save()

        messages.success(request, _('Товар успешно добавлен в корзину'))
        return redirect(self.request.META.get('HTTP_REFERER'))
