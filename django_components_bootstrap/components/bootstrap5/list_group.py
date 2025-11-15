from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    ResponsiveBreakpoint,
    Variant,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("ListGroup", registry=comp_registry)
class ListGroup(Component):
    class Kwargs:
        as_: Literal["ul", "ol", "div"] = "ul"
        flush: bool = False
        numbered: bool = False
        horizontal: ResponsiveBreakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["list-group"]
        if kwargs.flush:
            classes.append("list-group-flush")
        if kwargs.numbered:
            classes.append("list-group-numbered")
        if kwargs.horizontal is not None:
            if kwargs.horizontal is True:
                classes.append("list-group-horizontal")
            else:
                classes.append(f"list-group-horizontal-{kwargs.horizontal}")

        tag = "ol" if kwargs.numbered else kwargs.as_

        return {
            "tag": tag,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("ListGroupItem", registry=comp_registry)
class ListGroupItem(Component):
    class Kwargs:
        as_: Literal["li", "a", "button", "div"] = "li"
        variant: Variant | None = None
        active: bool = False
        disabled: bool = False
        action: bool = False
        href: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["list-group-item"]

        if kwargs.href:
            tag = "a"
        else:
            tag = kwargs.as_

        if kwargs.action or tag in ("a", "button"):
            classes.append("list-group-item-action")

        if kwargs.variant:
            classes.append(f"list-group-item-{kwargs.variant}")
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        html_attrs = {}

        if kwargs.active:
            html_attrs["aria-current"] = "true"

        if tag == "button" and kwargs.disabled:
            html_attrs["disabled"] = True

        if tag != "button":
            html_attrs["aria-disabled"] = "true" if kwargs.disabled else "false"

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "tag": tag,
            "classes": " ".join(classes),
            "href": kwargs.href,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        {% if tag == "a" and href %}
            <a {% html_attrs attrs defaults:href=href class=classes %}>
                {% slot "default" / %}
            </a>
        {% else %}
            <{{ tag }} {% html_attrs attrs class=classes %}>
                {% slot "default" / %}
            </{{ tag }}>
        {% endif %}
    """
