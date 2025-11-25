from django.template import Context
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import OverlayPlacement, TriggerEvent


class Tooltip(Component):
    class Kwargs:
        text: str
        placement: OverlayPlacement = "top"
        trigger: TriggerEvent = "hover"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "text": kwargs.text,
            "placement": kwargs.placement,
            "trigger": kwargs.trigger,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <span {% html_attrs attrs data-bs-toggle="tooltip" data-bs-title=text data-bs-placement=placement data-bs-trigger=trigger %}>
            {% slot "default" / %}
        </span>
    """
