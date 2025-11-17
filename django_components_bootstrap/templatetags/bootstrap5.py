from django.template import Library
from django_components import ComponentRegistry, RegistrySettings

register = library = Library()
bs5_registry = ComponentRegistry(
    library=library,
    settings=RegistrySettings(
        context_behavior="isolated",
        tag_formatter="django_components_bootstrap.tag_formatter.bootstrap5_formatter",
    ),
)
