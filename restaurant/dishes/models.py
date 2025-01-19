from django.db import models


class Dishes(models.Model):
    name = models.CharField(
        max_length=255, unique=True, verbose_name="Название блюда"
    )
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Цена блюда"
    )
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )

    def __str__(self):
        return str(self.name) + " " + str(self.price) + " рублей"
