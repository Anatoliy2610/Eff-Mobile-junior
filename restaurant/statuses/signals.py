from django.db.models.signals import post_migrate
from django.dispatch import receiver

from .models import Status


@receiver(post_migrate)
def create_statuses(sender, **kwargs):
    if sender.name == "restaurant.statuses":
        Status.objects.get_or_create(name="В ожидании")
        Status.objects.get_or_create(name="Готово")
        Status.objects.get_or_create(name="Оплачено")
