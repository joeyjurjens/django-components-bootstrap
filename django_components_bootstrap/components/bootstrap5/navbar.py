from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    AnchorOrSpan,
    Breakpoint,
    NavbarPlacement,
    ThemeVariant,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Navbar", registry=comp_registry)
class Navbar(Component):
    class Kwargs:
        expand: Breakpoint | None = None
        bg: str | None = None
        variant: ThemeVariant | None = None
        placement: NavbarPlacement | None = None
        container: Literal["sm", "md", "lg", "xl", "xxl", "fluid", True] | None = "fluid"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["navbar"]

        if kwargs.expand:
            classes.append(f"navbar-expand-{kwargs.expand}")

        if kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")

        if kwargs.placement:
            classes.append(kwargs.placement)

        container_class = None
        if kwargs.container is not None:
            if kwargs.container is True:
                container_class = "container"
            elif kwargs.container == "fluid":
                container_class = "container-fluid"
            else:
                container_class = f"container-{kwargs.container}"

        navbar_collapse_id = f"navbar-collapse-{self.id}"

        return {
            "classes": " ".join(classes),
            "theme": kwargs.variant,
            "container_class": container_class,
            "navbar_collapse_id": navbar_collapse_id,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "navbar" navbar_collapse_id=navbar_collapse_id %}
            <nav {% html_attrs attrs class=classes %} {% if theme %}data-bs-theme="{{ theme }}"{% endif %}>
                {% if container_class %}
                    <div class="{{ container_class }}">
                        {% slot "default" / %}
                    </div>
                {% else %}
                    {% slot "default" / %}
                {% endif %}
            </nav>
        {% endprovide %}
    """


@register("NavbarBrand", registry=comp_registry)
class NavbarBrand(Component):
    class Kwargs:
        as_: AnchorOrSpan = "a"
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "href": kwargs.href,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% if tag == "a" %}
            <a {% html_attrs attrs defaults:class="navbar-brand" defaults:href=href %}>
                {% slot "default" / %}
            </a>
        {% else %}
            <span {% html_attrs attrs defaults:class="navbar-brand" %}>
                {% slot "default" / %}
            </span>
        {% endif %}
    """


@register("NavbarToggler", registry=comp_registry)
class NavbarToggler(Component):
    class Kwargs:
        aria_label: str = "Toggle navigation"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        navbar = self.inject("navbar")
        target_id = navbar.navbar_collapse_id

        return {
            "target_id": target_id,
            "aria_label": kwargs.aria_label,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <button {% html_attrs attrs defaults:class="navbar-toggler" defaults:type="button" defaults:data-bs-toggle="collapse" defaults:data-bs-target="#{{ target_id }}" defaults:aria-controls=target_id defaults:aria-expanded="false" defaults:aria-label=aria_label %}>
            {% if slot_default_filled %}
                {% slot "default" / %}
            {% else %}
                <span class="navbar-toggler-icon"></span>
            {% endif %}
        </button>
    """


@register("NavbarCollapse", registry=comp_registry)
class NavbarCollapse(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        navbar = self.inject("navbar")
        collapse_id = navbar.navbar_collapse_id

        return {
            "collapse_id": collapse_id,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="collapse navbar-collapse" defaults:id=collapse_id %}>
            {% slot "default" / %}
        </div>
    """


@register("NavbarNav", registry=comp_registry)
class NavbarNav(Component):
    class Kwargs:
        scroll: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["navbar-nav"]
        if kwargs.scroll:
            classes.append("navbar-nav-scroll")

        return {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <ul {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </ul>
    """


@register("NavbarText", registry=comp_registry)
class NavbarText(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <span {% html_attrs attrs defaults:class="navbar-text" %}>
            {% slot "default" / %}
        </span>
    """
