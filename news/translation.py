from modeltranslation.translator import TranslationOptions, register
from .models import (
    News,
)


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'meta_keywords',
        'meta_description',
        'excerpt',
        'text',
    )
