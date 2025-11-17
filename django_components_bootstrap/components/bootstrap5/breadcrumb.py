from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Breadcrumb", registry=bs5_registry)
class Breadcrumb(Component):
    class Kwargs:
        as_: str = "nav"
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

        <{{ tag }} {% html_attrs attrs defaults:aria-label="breadcrumb" %}>
            <ol class="breadcrumb">
                {% slot "default" / %}
            </ol>
        </{{ tag }}>
    """


@register("BreadcrumbItem", registry=bs5_registry)
class BreadcrumbItem(Component):
    class Kwargs:
        active: bool = False
        href: str | None = None
        as_: str = "li"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        css_classes = ["breadcrumb-item"]
        if kwargs.active:
            css_classes.append("active")

        aria_current = "page" if kwargs.active else None

        return {
            "tag": kwargs.as_,
            "css_class": " ".join(css_classes),
            "active": kwargs.active,
            "href": kwargs.href,
            "aria_current": aria_current,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs class=css_class aria-current=aria_current %}>
            {% if not active and href %}
                <a href="{{ href }}">{% slot "default" / %}</a>
            {% else %}
                {% slot "default" / %}
            {% endif %}
        </{{ tag }}>
    """
