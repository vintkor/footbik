from django.contrib import admin
from django.contrib.postgres.fields import JSONField
from .models import Currency, SystemSetting
from jsoneditor.forms import JSONEditor


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'code',
        'course',
        'is_active',
    )


@admin.register(SystemSetting)
class SystemSettingAdmin(admin.ModelAdmin):
    formfield_overrides = {
        JSONField: {'widget': JSONEditor},
    }
