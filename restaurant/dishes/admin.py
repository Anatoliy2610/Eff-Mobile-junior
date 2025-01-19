from django.contrib import admin

from .models import Dishes


@admin.register(Dishes)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "price",
        "time_create",
    )
    list_display_links = (
        "id",
        "name",
        "price",
    )
