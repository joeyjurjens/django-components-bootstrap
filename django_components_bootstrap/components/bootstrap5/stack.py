from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import Breakpoint, StackDirection
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Stack", registry=bs5_registry)
class Stack(Component):
    class Kwargs:
        direction: StackDirection = "vertical"
        gap: int | None = None
        responsive: Breakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = []

        if kwargs.direction == "horizontal":
            if kwargs.responsive:
                classes.append(f"hstack-{kwargs.responsive}")
            else:
                classes.append("hstack")
        else:
            classes.append("vstack")

        if kwargs.gap is not None:
            classes.append(f"gap-{kwargs.gap}")

        return {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </div>
    """
