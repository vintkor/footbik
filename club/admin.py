from django.contrib import admin
from .models import Club


@admin.register(Club)
class ClubAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('title', 'region', 'super_admin')
    prepopulated_fields = {'slug': ('title',)}
