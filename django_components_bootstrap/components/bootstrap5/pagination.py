from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import Size
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Pagination", registry=comp_registry)
class Pagination(Component):
    class Kwargs:
        size: Size | None = None
        attrs: dict | None = None
        ul_attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["pagination"]
        if kwargs.size:
            classes.append(f"pagination-{kwargs.size}")

        return {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
            "ul_attrs": kwargs.ul_attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <nav {% html_attrs attrs defaults:aria-label="Page navigation" %}>
            <ul {% html_attrs ul_attrs class=classes %}>
                {% slot "default" / %}
            </ul>
        </nav>
    """


@register("PaginationItem", registry=comp_registry)
class PaginationItem(Component):
    class Kwargs:
        active: bool = False
        disabled: bool = False
        href: str = "#"
        aria_label: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["page-item"]
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        return {
            "classes": " ".join(classes),
            "active": kwargs.active,
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "aria_label": kwargs.aria_label,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <li {% html_attrs attrs class=classes %}>
            <a {% html_attrs class="page-link" href=href defaults:aria-label=aria_label %}{% if active %} aria-current="page"{% endif %}{% if disabled %} tabindex="-1" aria-disabled="true"{% endif %}>
                {% slot "default" / %}
            </a>
        </li>
    """


@register("PageItem", registry=comp_registry)
class PageItem(PaginationItem):
    pass


@register("PageLink", registry=comp_registry)
class PageLink(Component):
    class Kwargs:
        href: str = "#"
        aria_label: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "href": kwargs.href,
            "aria_label": kwargs.aria_label,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <a {% html_attrs attrs class="page-link" href=href defaults:aria-label=aria_label %}>
            {% slot "default" / %}
        </a>
    """


@register("PaginationFirst", registry=comp_registry)
class PaginationFirst(Component):
    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        return {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <li {% html_attrs attrs class=classes %}>
            <a class="page-link" href="{{ href }}"{% if disabled %} tabindex="-1" aria-disabled="true"{% endif %}>
                <span {% html_attrs defaults:aria-hidden="true" %}>{% slot "default" %}«{% endslot %}</span>
                <span class="visually-hidden">First</span>
            </a>
        </li>
    """


@register("PaginationPrev", registry=comp_registry)
class PaginationPrev(Component):
    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        return {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <li {% html_attrs attrs class=classes %}>
            <a class="page-link" href="{{ href }}"{% if disabled %} tabindex="-1" aria-disabled="true"{% endif %}>
                <span {% html_attrs defaults:aria-hidden="true" %}>{% slot "default" %}‹{% endslot %}</span>
                <span class="visually-hidden">Previous</span>
            </a>
        </li>
    """


@register("PaginationNext", registry=comp_registry)
class PaginationNext(Component):
    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        return {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <li {% html_attrs attrs class=classes %}>
            <a class="page-link" href="{{ href }}"{% if disabled %} tabindex="-1" aria-disabled="true"{% endif %}>
                <span {% html_attrs defaults:aria-hidden="true" %}>{% slot "default" %}›{% endslot %}</span>
                <span class="visually-hidden">Next</span>
            </a>
        </li>
    """


@register("PaginationLast", registry=comp_registry)
class PaginationLast(Component):
    class Kwargs:
        disabled: bool = False
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        return {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <li {% html_attrs attrs class=classes %}>
            <a class="page-link" href="{{ href }}"{% if disabled %} tabindex="-1" aria-disabled="true"{% endif %}>
                <span {% html_attrs defaults:aria-hidden="true" %}>{% slot "default" %}»{% endslot %}</span>
                <span class="visually-hidden">Last</span>
            </a>
        </li>
    """


@register("PaginationEllipsis", registry=comp_registry)
class PaginationEllipsis(Component):
    class Kwargs:
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["page-item"]
        if kwargs.disabled:
            classes.append("disabled")

        return {
            "classes": " ".join(classes),
            "disabled": kwargs.disabled,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <li {% html_attrs attrs class=classes %}>
            <span class="page-link">
                <span {% html_attrs defaults:aria-hidden="true" %}>{% slot "default" %}…{% endslot %}</span>
                <span class="visually-hidden">More</span>
            </span>
        </li>
    """
