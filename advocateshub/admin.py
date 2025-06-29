
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin 
from .models import User as CustomUser 

@admin.register(CustomUser) 
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'name', 'phone')
    ordering = ('username',) 
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('name', 'phone', 'profile', 'role')}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('name', 'phone', 'profile', 'role')}),
    )

