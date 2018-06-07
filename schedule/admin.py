from django.contrib import admin
from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = (
        'group',
        'lesson',
        'date_start',
        'date_end',
    )
