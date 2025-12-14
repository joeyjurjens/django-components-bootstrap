from django.template import Context
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import (
    AnchorOrSpan,
    Breakpoint,
    NavbarContainer,
    NavbarPlacement,
    ThemeVariant,
)


class Navbar(Component):
    class Kwargs:
        expand: Breakpoint | None = None
        bg: str | None = None
        variant: ThemeVariant | None = None
        placement: NavbarPlacement | None = None
        container: NavbarContainer | None = "fluid"
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
        if kwargs.container is not None and kwargs.container is not False:
            if kwargs.container is True:
                container_class = "container"
            elif kwargs.container == "fluid":
                container_class = "container-fluid"
            else:
                container_class = f"container-{kwargs.container}"

        navbar_collapse_id = (kwargs.attrs or {}).get("id") or f"navbar-collapse-{self.id}"

        return {
            "classes": " ".join(classes),
            "theme": kwargs.variant,
            "container_class": container_class,
            "navbar_collapse_id": navbar_collapse_id,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        {% if tag == "a" %}
            <a {% html_attrs attrs class="navbar-brand" href=href %}>
                {% slot "default" / %}
            </a>
        {% else %}
            <span {% html_attrs attrs class="navbar-brand" %}>
                {% slot "default" / %}
            </span>
        {% endif %}
    """


class NavbarToggler(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        navbar = self.inject("navbar")
        target_id = navbar.navbar_collapse_id

        return {
            "target_id": target_id,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <button {% html_attrs attrs class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#{{ target_id }}" defaults:aria-controls=target_id defaults:aria-expanded="false" defaults:aria-label="Toggle navigation" %}>
            {% if slot_default_filled %}
                {% slot "default" / %}
            {% else %}
                <span class="navbar-toggler-icon"></span>
            {% endif %}
        </button>
    """


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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <div {% html_attrs attrs class="collapse navbar-collapse" defaults:id=collapse_id %}>
            {% slot "default" / %}
        </div>
    """


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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <ul {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </ul>
    """


class NavbarText(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <span {% html_attrs attrs class="navbar-text" %}>
            {% slot "default" / %}
        </span>
    """
