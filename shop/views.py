from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import (
    Product,
    Category,
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
        return Product.objects.filter(category__slug=self.kwargs.get('slug'))

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
