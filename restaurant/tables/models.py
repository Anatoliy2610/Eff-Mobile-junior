from django.db import models


class Table(models.Model):
    table_number = models.IntegerField(unique=True, verbose_name="Номер стола")

    def __str__(self):
        return str(self.table_number)
