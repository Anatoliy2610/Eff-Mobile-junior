from django.contrib import admin

from .models import Table


@admin.register(Table)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "table_number",
    )
