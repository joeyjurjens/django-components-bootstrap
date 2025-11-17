from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    AnchorOrButton,
    NavItemTag,
    NavTag,
    NavVariant,
)
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Nav", registry=bs5_registry)
class Nav(Component):
    class Kwargs:
        variant: NavVariant | None = None
        fill: bool = False
        justified: bool = False
        vertical: bool = False
        as_: NavTag = "nav"
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs class=classes defaults:role=role %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("NavItem", registry=bs5_registry)
class NavItem(Component):
    class Kwargs:
        as_: NavItemTag = "li"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs class="nav-item" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("NavLink", registry=bs5_registry)
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

        button_disabled = True if kwargs.as_ == "button" and kwargs.disabled else None
        aria_disabled = "true" if kwargs.as_ == "a" and kwargs.disabled else None
        aria_current = "page" if kwargs.active and kwargs.as_ == "a" else None

        link_href = None if kwargs.disabled else kwargs.href

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "href": link_href,
            "button_disabled": button_disabled,
            "aria_disabled": aria_disabled,
            "aria_current": aria_current,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% if tag == "a" %}
            <a {% html_attrs attrs href=href class=classes defaults:aria-disabled=aria_disabled defaults:aria-current=aria_current %}>
                {% slot "default" / %}
            </a>
        {% else %}
            <button {% html_attrs attrs defaults:type="button" class=classes disabled=button_disabled defaults:aria-current=aria_current %}>
                {% slot "default" / %}
            </button>
        {% endif %}
    """
