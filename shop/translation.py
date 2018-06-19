from modeltranslation.translator import TranslationOptions, register
from .models import (
    Category,
    Product,
    Parameter,
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
        'text',
    )


@register(Parameter)
class ParameterTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
