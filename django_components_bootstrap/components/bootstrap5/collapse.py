from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import ButtonTag
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Collapse", registry=comp_registry)
class Collapse(Component):
    class Kwargs:
        show: bool = False
        horizontal: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "collapse" collapse_id=collapse_id %}
            <div {% html_attrs attrs defaults:id=collapse_id class=classes %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("CollapseToggle", registry=comp_registry)
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

        return {
            "tag": kwargs.as_,
            "target_id": target_id,
            "expanded": "true" if kwargs.expanded else "false",
            "href": kwargs.href or f"#{target_id}",
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% if tag == "button" %}
            <button {% html_attrs attrs defaults:type="button" defaults:data-bs-toggle="collapse" defaults:data-bs-target="#{{ target_id }}" defaults:aria-expanded=expanded defaults:aria-controls=target_id %}>
                {% slot "default" / %}
            </button>
        {% else %}
            <a {% html_attrs attrs defaults:href=href defaults:data-bs-toggle="collapse" defaults:role="button" defaults:aria-expanded=expanded defaults:aria-controls=target_id %}>
                {% slot "default" / %}
            </a>
        {% endif %}
    """
