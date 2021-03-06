from django.contrib import admin
from .models import (
    Club,
    ClubImage,
    ClubAdministrator,
    ClubLesson,
    Group,
    Schedule,
)
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(Club)
class ClubAdmin(TabbedTranslationAdmin):
    save_on_top = True
    list_display = ('title', 'region', 'super_admin')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(ClubAdministrator)
class ClubAdministratorAdmin(admin.ModelAdmin):
    save_on_top = True


@admin.register(ClubImage)
class ClubImageAdmin(TabbedTranslationAdmin):
    save_on_top = True


@admin.register(ClubLesson)
class ClubLessonAdmin(TabbedTranslationAdmin):
    save_on_top = True


@admin.register(Group)
class GroupAdmin(TabbedTranslationAdmin):
    save_on_top = True
    filter_horizontal = ('children',)


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('lesson', 'group', 'date_start', 'date_end')
