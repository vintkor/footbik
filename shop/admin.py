from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductParameters,
    Parameter,
    Value,
    Variant,
    Cart,
    CartItem,
)
from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TabbedTranslationAdmin


# class ImageInline(admin.TabularInline):
#     extra = 0
#     model = Image


class ValueInline(admin.TabularInline):
    extra = 0
    model = Value


class VariantInline(admin.StackedInline):
    extra = 0
    model = Variant
    filter_horizontal = ('value',)


class ProductParametersInline(admin.TabularInline):
    extra = 0
    model = ProductParameters
    filter_horizontal = ('value',)


class ProductParametersAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, TabbedTranslationAdmin):
    save_on_top = True
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    inlines = (VariantInline, ProductParametersInline)


@admin.register(Parameter)
class ParameterAdmin(admin.ModelAdmin):
    inlines = (ValueInline,)


@admin.register(Value)
class ValueAdmin(admin.ModelAdmin):
    pass


@admin.register(Variant)
class VariantAdmin(admin.ModelAdmin):
    filter_horizontal = ('value',)


class CartItemAdmin(admin.ModelAdmin):
    pass


class CartItemInline(admin.TabularInline):
    extra = 0
    model = CartItem


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    inlines = (CartItemInline,)
