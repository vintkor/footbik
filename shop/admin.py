from django.contrib import admin
from .models import (
    Category,
    Product,
)
from mptt.admin import DraggableMPTTAdmin


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    save_on_top = True
    list_display = ('tree_actions', 'indented_title')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
