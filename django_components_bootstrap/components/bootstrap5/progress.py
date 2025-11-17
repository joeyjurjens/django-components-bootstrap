from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import Variant
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Progress", registry=bs5_registry)
class Progress(Component):
    class Kwargs:
        height: str | None = None
        stacked: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["progress-stacked" if kwargs.stacked else "progress"]
        style = {}
        if kwargs.height:
            style["height"] = kwargs.height

        return {
            "classes": " ".join(classes),
            "style": style,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class=classes %} {% if style %}style="{% for key, value in style.items %}{{ key }}: {{ value }};{% endfor %}"{% endif %}>
            {% slot "default" / %}
        </div>
    """


@register("ProgressStacked", registry=bs5_registry)
class ProgressStacked(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class="progress-stacked" %}>
            {% slot "default" / %}
        </div>
    """


@register("ProgressBar", registry=bs5_registry)
class ProgressBar(Component):
    class Kwargs:
        now: int = 0
        min: int = 0
        max: int = 100
        variant: Variant | None = None
        striped: bool = False
        animated: bool = False
        label: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["progress-bar"]

        if kwargs.variant:
            classes.append(f"bg-{kwargs.variant}")
        if kwargs.striped or kwargs.animated:
            classes.append("progress-bar-striped")
        if kwargs.animated:
            classes.append("progress-bar-animated")

        percentage = 0
        if kwargs.max > kwargs.min:
            percentage = ((kwargs.now - kwargs.min) / (kwargs.max - kwargs.min)) * 100

        return {
            "classes": " ".join(classes),
            "percentage": percentage,
            "now": kwargs.now,
            "min": kwargs.min,
            "max": kwargs.max,
            "label": kwargs.label,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class=classes %} style="width: {{ percentage }}%">
            {% if label %}{{ label }}{% endif %}
            {% slot "default" default / %}
        </div>
    """
