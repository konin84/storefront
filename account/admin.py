from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import Account, Profile

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_superuser', 'is_staff', 'is_admin','is_webmaster' ,'is_active', 'date_joined','last_login',)
    search_fields = ('username', 'email')
    readonly_fields = ('is_admin', 'is_superuser', 'is_active', 'date_joined', 'last_login')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)

@admin.register(Profile)
class ViewAdmin(admin.ModelAdmin):
    pass

