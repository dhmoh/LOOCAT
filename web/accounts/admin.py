from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import AdminChangeForm, AdminCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):
    form = AdminChangeForm
    add_form = AdminCreationForm

    list_display = ('id', 'email', 'name', 'money', 'date_joined', 'last_login', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name', 'money',)}),
        ('Permissions', {'fields': ('is_active', 'is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'money', 'password1', 'password2')}
         ),
    )
    search_fields = ('email', 'name',)
    ordering = ('email', 'name')
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)