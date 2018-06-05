from django.contrib import admin
from .models import (
    User,
    Investor,
    Parent,
    Child,
)


class ChildInline(admin.TabularInline):
    extra = 0
    model = Child


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_admin',
    )
    readonly_fields = ('created', 'updated', 'password')
    list_filter = ('is_admin',)
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions')


@admin.register(Investor)
class InvestorAdmin(admin.ModelAdmin):
    pass


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    inlines = (ChildInline,)


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    pass
