from django.template import Context
from django_components import Component, register, types

from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("CloseButton", registry=bs5_registry)
class CloseButton(Component):
    class Kwargs:
        variant: str | None = None
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        classes = ["btn-close"]
        if kwargs.variant:
            classes.append(f"btn-close-{kwargs.variant}")

        disabled = True if kwargs.disabled else None

        return {
            "classes": " ".join(classes),
            "disabled": disabled,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <button {% html_attrs attrs type="button" class=classes defaults:aria-label="Close" disabled=disabled %}></button>
    """
