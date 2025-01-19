from django.contrib import admin

from .models import Order


@admin.register(Order)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "table_number",
        "total_price",
        "status",
    )
