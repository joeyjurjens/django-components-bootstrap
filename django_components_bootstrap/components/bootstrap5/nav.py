from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    AnchorOrButton,
    NavVariant,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Nav", registry=comp_registry)
class Nav(Component):
    class Kwargs:
        variant: NavVariant | None = None
        fill: bool = False
        justified: bool = False
        vertical: bool = False
        as_: Literal["nav", "ul"] = "nav"
        role: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["nav"]

        if kwargs.variant == "tabs":
            classes.append("nav-tabs")
        elif kwargs.variant == "pills":
            classes.append("nav-pills")
        elif kwargs.variant == "underline":
            classes.append("nav-underline")

        if kwargs.fill:
            classes.append("nav-fill")
        if kwargs.justified:
            classes.append("nav-justified")

        if kwargs.vertical:
            classes.append("flex-column")

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "role": kwargs.role,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class=classes defaults:role=role %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("NavItem", registry=comp_registry)
class NavItem(Component):
    class Kwargs:
        as_: Literal["li", "div"] = "li"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs defaults:class="nav-item" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("NavLink", registry=comp_registry)
class NavLink(Component):
    class Kwargs:
        as_: AnchorOrButton = "a"
        href: str = "#"
        active: bool = False
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["nav-link"]
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        html_attrs = {}

        if kwargs.as_ == "button" and kwargs.disabled:
            html_attrs["disabled"] = True

        if kwargs.as_ == "a":
            html_attrs["aria-disabled"] = "true" if kwargs.disabled else "false"
            if kwargs.disabled:
                html_attrs["tabindex"] = "-1"

        if kwargs.active:
            html_attrs["aria-current"] = "page"

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "href": kwargs.href,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        {% if tag == "a" %}
            <a {% html_attrs attrs defaults:href=href class=classes %}>
                {% slot "default" / %}
            </a>
        {% else %}
            <button {% html_attrs attrs defaults:type="button" class=classes %}>
                {% slot "default" / %}
            </button>
        {% endif %}
    """
