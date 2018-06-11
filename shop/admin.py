from django.contrib import admin
from .models import (
    Category,
    Product,
)
from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, TabbedTranslationAdmin):
    save_on_top = True
    list_display = ('tree_actions', 'indented_title')


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
