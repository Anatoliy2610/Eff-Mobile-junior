from django.test import TestCase

from restaurant.dishes.models import Dishes
from restaurant.tables.models import Table


class TestOrder(TestCase):
    def setUp(self):
        Dishes.objects.create(name="tea", price=100)
        Dishes.objects.create(name="coffee", price=200)
        Dishes.objects.create(name="water", price=30)
        Dishes.objects.create(name="beer", price=250)

        Table.objects.create(table_number=1)
        Table.objects.create(table_number=2)
        Table.objects.create(table_number=3)
        Table.objects.create(table_number=4)
        Table.objects.create(table_number=5)

        # order = Order.objects.get(pk=1)
        # order.table_number = 1
        # order = Order.objects.get(pk=1)
        # order.items.add([1, 2, 3])
