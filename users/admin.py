from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'age', 'is_staff', 'password']


admin.site.register(CustomUser, CustomUserAdmin)
