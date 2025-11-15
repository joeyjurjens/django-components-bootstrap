from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Tooltip", registry=comp_registry)
class Tooltip(Component):
    class Kwargs:
        text: str
        placement: Literal["top", "bottom", "left", "right"] = "top"
        as_: str = "span"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        html_attrs = {
            "data-bs-toggle": "tooltip",
            "data-bs-placement": kwargs.placement,
            "title": kwargs.text,
        }

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "tag": kwargs.as_,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
