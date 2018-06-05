from django.contrib import admin
from .models import Region
from mptt.admin import DraggableMPTTAdmin


@admin.register(Region)
class RegionAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'title', 'code')
    save_on_top = True
    prepopulated_fields = {'slug': ('title',)}
