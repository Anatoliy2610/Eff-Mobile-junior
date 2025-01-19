from django.test import TestCase
from django.urls import reverse

from restaurant.statuses.models import Status


class TestDishes(TestCase):
    def setUp(self):
        Status.objects.create(
            name="Не оплачено",
        )
        Status.objects.create(
            name="Возврат",
        )

    def test_statuses_home(self):
        response = self.client.get(reverse("statuses"))
        self.assertEqual(len(response.context["statuses"]), 5)
        status = Status.objects.get(id=2)
        self.assertEqual(status.name, "Готово")

    def test_statuses_create(self):
        response = self.client.get(reverse("status_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )
        response = self.client.post(
            reverse("status_create"),
            {
                "name": "Ушли не заплатили",
            },
        )

        response = self.client.get(reverse("statuses"))
        self.assertTrue(len(response.context["statuses"]), 6)

    def test_statuses_update(self):
        status = Status.objects.get(id=2)
        response = self.client.get(
            reverse("status_update", kwargs={"status_id": status.id})
        )
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )
        response = self.client.post(
            reverse("status_update", kwargs={"status_id": status.id}),
            {
                "name": "Go-go-go!",
            },
        )
        self.assertEqual(response.status_code, 302)
        status.refresh_from_db()
        self.assertEqual(status.name, "Go-go-go!")

    def test_statuses_delete(self):
        status = Status.objects.get(name="Не оплачено")
        response = self.client.get(
            reverse("status_delete", kwargs={"status_id": status.id})
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse("status_delete", kwargs={"status_id": status.id})
        )
        self.assertRedirects(response, reverse("statuses"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Status.objects.count(), 4)
