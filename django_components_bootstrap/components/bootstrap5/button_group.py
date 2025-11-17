from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import Size
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("ButtonGroup", registry=bs5_registry)
class ButtonGroup(Component):
    class Kwargs:
        size: Size | None = None
        vertical: bool = False
        role: str = "group"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["btn-group-vertical" if kwargs.vertical else "btn-group"]
        if kwargs.size:
            classes.append(f"btn-group-{kwargs.size}")

        return {
            "classes": " ".join(classes),
            "role": kwargs.role,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class=classes defaults:role=role %}>
            {% slot "default" / %}
        </div>
    """


@register("ButtonToolbar", registry=bs5_registry)
class ButtonToolbar(Component):
    class Kwargs:
        role: str = "toolbar"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "role": kwargs.role,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class="btn-toolbar" defaults:role=role %}>
            {% slot "default" / %}
        </div>
    """
