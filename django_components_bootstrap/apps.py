from django.apps import AppConfig


class DjangoComponentsBootstrapConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_components_bootstrap"

    def ready(self):
        from django_components_bootstrap.components import bootstrap5  # noqa: F401
