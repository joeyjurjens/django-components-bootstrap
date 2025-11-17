from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import ButtonTag
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Collapse", registry=bs5_registry)
class Collapse(Component):
    class Kwargs:
        show: bool = False
        horizontal: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput
        toggle: SlotInput = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        collapse_id = f"collapse-{self.id}"

        classes = ["collapse"]
        if kwargs.horizontal:
            classes.append("collapse-horizontal")
        if kwargs.show:
            classes.append("show")

        return {
            "collapse_id": collapse_id,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "collapse" collapse_id=collapse_id %}
            {% slot "toggle" / %}
            <div {% html_attrs attrs id=collapse_id class=classes %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("CollapseToggle", registry=bs5_registry)
class CollapseToggle(Component):
    class Kwargs:
        as_: ButtonTag = "button"
        expanded: bool = False
        href: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        collapse = self.inject("collapse")
        target_id = collapse.collapse_id

        button_type = "button" if kwargs.as_ == "button" else None
        link_href = kwargs.href or f"#{target_id}" if kwargs.as_ != "button" else None
        link_role = "button" if kwargs.as_ != "button" else None

        return {
            "tag": kwargs.as_,
            "target_id": target_id,
            "expanded": "true" if kwargs.expanded else "false",
            "button_type": button_type,
            "link_href": link_href,
            "link_role": link_role,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        {% if tag == "button" %}
            <button {% html_attrs attrs type=button_type data-bs-toggle="collapse" data-bs-target="#{{ target_id }}" defaults:aria-expanded=expanded defaults:aria-controls=target_id %}>
                {% slot "default" / %}
            </button>
        {% else %}
            <a {% html_attrs attrs href=link_href data-bs-toggle="collapse" role=link_role defaults:aria-expanded=expanded defaults:aria-controls=target_id %}>
                {% slot "default" / %}
            </a>
        {% endif %}
    """
