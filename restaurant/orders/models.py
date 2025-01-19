from django.db import models

from restaurant.dishes.models import Dishes
from restaurant.statuses.models import Status
from restaurant.tables.models import Table


class Order(models.Model):
    table_number = models.OneToOneField(
        Table, on_delete=models.PROTECT, null=True, verbose_name="Номер стола"
    )

    items = models.ManyToManyField(
        Dishes, blank=True, verbose_name="Блюда", related_name="dishes"
    )
    total_price = models.BigIntegerField(
        verbose_name="Стоимость заказа", null=True, default=0
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        null=True,
        verbose_name="Статус заказа",
        related_name="status",
        default=1,
    )

    def __str__(self):
        return str(self.table_number)

    def total_price(self):
        return sum([item.price for item in self.items.all()])
