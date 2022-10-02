from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "first_name",
        "middle_name",
        "last_name"
    )
