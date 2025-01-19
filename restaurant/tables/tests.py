from django.test import TestCase
from django.urls import reverse

from restaurant.tables.models import Table


class TestTables(TestCase):
    def setUp(self):
        Table.objects.create(
            table_number=1,
        )
        Table.objects.create(
            table_number=2,
        )
        Table.objects.create(
            table_number=3,
        )

    def test_tables_home(self):
        response = self.client.get(reverse("tables"))
        self.assertEqual(len(response.context["tables"]), 3)

    def test_tables_create(self):
        response = self.client.get(reverse("table_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )
        response = self.client.post(
            reverse("table_create"),
            {
                "table_number": 4,
            },
        )

        response = self.client.get(reverse("tables"))
        self.assertTrue(len(response.context["tables"]), 4)

    def test_tables_update(self):
        tables = Table.objects.get(id=2)
        response = self.client.get(
            reverse("table_update", kwargs={"table_id": tables.id})
        )
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )
        response = self.client.post(
            reverse("table_update", kwargs={"table_id": tables.id}),
            {
                "table_number": 5,
            },
        )
        self.assertEqual(response.status_code, 302)
        tables.refresh_from_db()
        self.assertEqual(tables.table_number, 5)

    def test_tables_delete(self):
        tables = Table.objects.get(table_number=1)
        response = self.client.get(
            reverse("table_delete", kwargs={"table_id": tables.id})
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse("table_delete", kwargs={"table_id": tables.id})
        )
        self.assertRedirects(response, reverse("tables"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Table.objects.count(), 2)
