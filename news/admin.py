from django.contrib import admin
from .models import News
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'created', 'region')
    list_filter = ('region',)
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
