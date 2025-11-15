from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Popover", registry=comp_registry)
class Popover(Component):
    class Kwargs:
        content: str
        title: str | None = None
        placement: Literal["top", "bottom", "left", "right"] = "top"
        trigger: Literal["click", "hover", "focus", "manual"] = "click"
        as_: str = "button"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        html_attrs = {
            "data-bs-toggle": "popover",
            "data-bs-placement": kwargs.placement,
            "data-bs-content": kwargs.content,
            "data-bs-trigger": kwargs.trigger,
        }

        if kwargs.title:
            html_attrs["data-bs-title"] = kwargs.title

        if kwargs.as_ == "button":
            html_attrs["type"] = "button"

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
