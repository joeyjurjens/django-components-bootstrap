from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    ListGroupItemTag,
    ListGroupTag,
    ResponsiveBreakpoint,
    Variant,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("ListGroup", registry=comp_registry)
class ListGroup(Component):
    class Kwargs:
        as_: ListGroupTag = "ul"
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("ListGroupItem", registry=comp_registry)
class ListGroupItem(Component):
    class Kwargs:
        as_: ListGroupItemTag = "li"
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

        if kwargs.disabled and tag != "button":
            classes.append("disabled")

        aria_current = "true" if kwargs.active else None
        button_disabled = True if tag == "button" and kwargs.disabled else None
        aria_disabled = "true" if tag != "button" and kwargs.disabled else None
        button_type = "button" if tag == "button" else None

        return {
            "tag": tag,
            "classes": " ".join(classes),
            "href": kwargs.href,
            "aria_current": aria_current,
            "button_disabled": button_disabled,
            "button_type": button_type,
            "aria_disabled": aria_disabled,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% if tag == "a" and href %}
            <a {% html_attrs attrs href=href class=classes aria-current=aria_current aria-disabled=aria_disabled %}>
                {% slot "default" / %}
            </a>
        {% elif tag == "button" %}
            <button {% html_attrs attrs class=classes type=button_type aria-current=aria_current disabled=button_disabled %}>
                {% slot "default" / %}
            </button>
        {% else %}
            <{{ tag }} {% html_attrs attrs class=classes aria-current=aria_current aria-disabled=aria_disabled %}>
                {% slot "default" / %}
            </{{ tag }}>
        {% endif %}
    """
