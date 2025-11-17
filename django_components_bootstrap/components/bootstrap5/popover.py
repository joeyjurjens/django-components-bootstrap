from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import OverlayPlacement, TriggerEvent
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Popover", registry=bs5_registry)
class Popover(Component):
    class Kwargs:
        title: str
        content: str
        placement: OverlayPlacement = "top"
        trigger: TriggerEvent = "click"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "title": kwargs.title,
            "content": kwargs.content,
            "placement": kwargs.placement,
            "trigger": kwargs.trigger,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <span {% html_attrs attrs data-bs-toggle="popover" data-bs-title=title data-bs-content=content data-bs-placement=placement data-bs-trigger=trigger %}>
            {% slot "default" / %}
        </span>
    """
