from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import (
    Variant,
    Product,
    Category,
)


class CategoryListView(ListView):
    template_name = 'shop/main.html'
    context_object_name = 'categories'
    model = Category


class ProductListView(ListView):
    template_name = 'shop/category-list.html'
    context_object_name = 'products'

    def get_queryset(self):
        return Product.objects.filter(category__slug=self.kwargs.get('slug'))

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data()
        context['category'] = get_object_or_404(Category, slug=self.kwargs.get('slug'))
        return context


class ProductDetailView(DetailView):
    template_name = 'shop/product.html'
    context_object_name = 'product'
    model = Product
