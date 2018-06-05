from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'region')
    list_filter = ('region',)
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
