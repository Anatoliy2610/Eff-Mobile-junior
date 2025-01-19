from django.apps import AppConfig


class StatusesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "restaurant.statuses"

    def ready(self):
        import restaurant.statuses.signals
