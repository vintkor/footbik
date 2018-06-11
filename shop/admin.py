from django.contrib import admin
from .models import (
    Category,
    Product,
    Image,
)
from mptt.admin import DraggableMPTTAdmin
from modeltranslation.admin import TabbedTranslationAdmin


class ImageInline(admin.TabularInline):
    extra = 0
    model = Image


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, TabbedTranslationAdmin):
    save_on_top = True
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(TabbedTranslationAdmin):
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
    inlines = (ImageInline,)


@admin.register(Image)
class Image(admin.ModelAdmin):
    pass
