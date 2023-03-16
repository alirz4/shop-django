from django.contrib import admin
from django.contrib.auth.models import Group

from .models import User
from django.contrib.auth.admin import UserAdmin as BaserUserAdmin
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaserUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)
    readonly_fields = ('last_login',)

    fieldsets = (
        ('Main', {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('None',
         {'fields': ('is_active', 'is_admin', 'is_superuser', 'last_login')}),
    )

    add_fieldsets = (
        (None, {'fields': ('phone_number', 'email', 'full_name', 'password1', 'password2')}),
    )

    search_fields = ('is_admin', 'full_name')
    ordering = ('full_name',)


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
