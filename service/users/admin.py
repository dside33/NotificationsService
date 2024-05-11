from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from login.forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser
from userprofile.models import APIKey


class APIKeyInline(admin.TabularInline):
    model = APIKey
    extra = 1

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm 
    model = CustomUser

    inlines = [APIKeyInline]


admin.site.register(CustomUser, CustomUserAdmin)
