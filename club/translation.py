from modeltranslation.translator import TranslationOptions, register
from .models import (
    Club,
    ClubImage,
    ClubLesson,
    Group,
)


@register(Club)
class ClubTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'meta_keywords',
        'meta_description',
    )


@register(ClubImage)
class ClubImageTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'alt',
    )


@register(ClubLesson)
class ClubLessonTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'description',
    )


@register(Group)
class GroupTranslationOptions(TranslationOptions):
    fields = (
        'title',
    )
