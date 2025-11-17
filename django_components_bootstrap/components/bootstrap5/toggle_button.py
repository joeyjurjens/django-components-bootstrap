from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import Size, ToggleButtonType, Variant
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("ToggleButtonGroup", registry=bs5_registry)
class ToggleButtonGroup(Component):
    class Kwargs:
        name: str
        type: ToggleButtonType = "radio"
        vertical: bool = False
        size: Size | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["btn-group-vertical" if kwargs.vertical else "btn-group"]
        if kwargs.size:
            classes.append(f"btn-group-{kwargs.size}")

        return {
            "classes": " ".join(classes),
            "type": kwargs.type,
            "name": kwargs.name,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class=classes role="group" %}>
            {% slot "default" / %}
        </div>
    """


@register("ToggleButton", registry=bs5_registry)
class ToggleButton(Component):
    class Kwargs:
        type: ToggleButtonType = "checkbox"
        name: str | None = None
        value: str | None = None
        checked: bool = False
        disabled: bool = False
        variant: Variant = "primary"
        outline: bool = True
        size: Size | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        toggle_id = f"toggle-button-{self.id}"

        input_attrs = {
            "type": kwargs.type,
            "class": "btn-check",
            "id": toggle_id,
            "autocomplete": "off",
        }

        if kwargs.name:
            input_attrs["name"] = kwargs.name
        if kwargs.value:
            input_attrs["value"] = kwargs.value
        if kwargs.checked:
            input_attrs["checked"] = True
        if kwargs.disabled:
            input_attrs["disabled"] = True

        if kwargs.outline:
            variant_class = f"btn-outline-{kwargs.variant}"
        else:
            variant_class = f"btn-{kwargs.variant}"

        label_classes = ["btn", variant_class]
        if kwargs.size:
            label_classes.append(f"btn-{kwargs.size}")

        return {
            "input_attrs": input_attrs,
            "label_classes": " ".join(label_classes),
            "id": toggle_id,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <input {% html_attrs input_attrs %} />
        <label {% html_attrs attrs class=label_classes for=id %}>
            {% slot "default" / %}
        </label>
    """
