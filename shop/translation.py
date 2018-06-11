from modeltranslation.translator import TranslationOptions, register
from .models import (
    Category,
    Product,
)


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
