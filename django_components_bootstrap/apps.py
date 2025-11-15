from django.apps import AppConfig
from django.conf import settings


class DjangoComponentsBootstrapConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "django_components_bootstrap"

    def ready(self) -> None:
        if getattr(
            settings,
            "DJANGO_COMPONENTS_BOOTSTRAP_AUTO_REGISTER",
            True,
        ):
            from django_components_bootstrap.components import bootstrap5  # noqa: F401
