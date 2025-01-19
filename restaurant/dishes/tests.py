from django.test import TestCase
from django.urls import reverse

from restaurant.dishes.models import Dishes


class TestDishes(TestCase):
    def setUp(self):
        Dishes.objects.create(
            name="coffee",
            price=200,
        )
        Dishes.objects.create(
            name="tea",
            price=100,
        )
        Dishes.objects.create(
            name="water",
            price=50,
        )

    def test_dishes_home(self):
        response = self.client.get(reverse("dishes"))
        self.assertEqual(len(response.context["dishes"]), 3)

    def test_dishes_create(self):
        response = self.client.get(reverse("dishes_create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )
        response = self.client.post(
            reverse("dishes_create"),
            {
                "name": "beer",
                "price": 300,
            },
        )

        response = self.client.get(reverse("dishes"))
        self.assertTrue(len(response.context["dishes"]), 4)

    def test_dishes_update(self):
        dishes = Dishes.objects.get(id=2)
        response = self.client.get(
            reverse("dishes_update", kwargs={"dishes_id": dishes.id})
        )
        self.assertTemplateUsed(
            response, template_name="actions/create_or_update.html"
        )
        response = self.client.post(
            reverse("dishes_update", kwargs={"dishes_id": dishes.id}),
            {
                "name": "cola",
                "price": 150,
            },
        )
        self.assertEqual(response.status_code, 302)
        dishes.refresh_from_db()
        self.assertEqual(dishes.name, "cola")
        self.assertEqual(dishes.price, 150)

    def test_dishes_delete(self):
        dishes = Dishes.objects.get(name="water")
        response = self.client.get(
            reverse("dishes_delete", kwargs={"dishes_id": dishes.id})
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.post(
            reverse("dishes_delete", kwargs={"dishes_id": dishes.id})
        )
        self.assertRedirects(response, reverse("dishes"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dishes.objects.count(), 2)
