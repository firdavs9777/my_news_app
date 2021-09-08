from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','age','is_staff',]
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
    add_fieldsets = UserAdmin.fieldsets + (
        (None,{'fields':('age',)}),
    )
admin.site.register(CustomUser,CustomUserAdmin)