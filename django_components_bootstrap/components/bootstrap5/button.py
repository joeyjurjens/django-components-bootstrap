from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import ButtonType, Size, Variant
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Button", registry=comp_registry)
class Button(Component):
    class Kwargs:
        as_: str | None = None
        variant: Variant | Literal["link"] = "primary"
        outline: bool = False
        size: Size | None = None
        active: bool = False
        disabled: bool = False
        type: ButtonType = "button"
        href: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        if kwargs.as_:
            tag = kwargs.as_
            is_link = tag == "a"
        elif kwargs.href is not None:
            tag = "a"
            is_link = True
        elif kwargs.variant == "link":
            tag = "a"
            is_link = True
        else:
            tag = "button"
            is_link = False

        if kwargs.variant == "link":
            variant_class = "btn-link"
        elif kwargs.outline:
            variant_class = f"btn-outline-{kwargs.variant}"
        else:
            variant_class = f"btn-{kwargs.variant}"

        size_class = f"btn-{kwargs.size}" if kwargs.size else None

        classes = ["btn", variant_class]
        if size_class:
            classes.append(size_class)
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled and is_link:
            classes.append("disabled")

        html_attrs = {}

        if tag == "button":
            html_attrs["type"] = kwargs.type
            if kwargs.disabled:
                html_attrs["disabled"] = True

        if is_link:
            html_attrs["href"] = kwargs.href or "#"
            html_attrs["role"] = "button"
            if kwargs.disabled:
                html_attrs["aria-disabled"] = "true"
                html_attrs["tabindex"] = "-1"

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "tag": tag,
            "classes": " ".join(classes),
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
