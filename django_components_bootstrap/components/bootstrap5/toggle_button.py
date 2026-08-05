from django.template import Context
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import (
    NOT_PROVIDED,
    Size,
    ToggleButtonType,
    Variant,
)


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
            "group_name": kwargs.name,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        {% provide "toggle_button_group" type=type group_name=group_name %}
            <div {% html_attrs attrs class=classes role="group" %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


class ToggleButton(Component):
    class Kwargs:
        type: ToggleButtonType | None = None
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
        group = self.inject("toggle_button_group", NOT_PROVIDED)

        # A group's `type` is authoritative for all its buttons (Bootstrap's
        # `.btn-group` toggle pattern doesn't support mixing radio/checkbox
        # inputs); a button's own `name` still wins over the group's.
        if group is not NOT_PROVIDED:
            toggle_type = group.type
            toggle_name = kwargs.name if kwargs.name is not None else group.group_name
        else:
            toggle_type = kwargs.type if kwargs.type is not None else "checkbox"
            toggle_name = kwargs.name

        toggle_id = (kwargs.attrs or {}).get("id") or f"toggle-button-{self.id}"

        input_attrs = {
            "type": toggle_type,
            "class": "btn-check",
            "id": toggle_id,
            "autocomplete": "off",
        }

        if toggle_name:
            input_attrs["name"] = toggle_name
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

        # Exclude id from label attrs since it's used for the input
        label_attrs = {k: v for k, v in (kwargs.attrs or {}).items() if k != "id"}

        return {
            "input_attrs": input_attrs,
            "label_classes": " ".join(label_classes),
            "id": toggle_id,
            "label_attrs": label_attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <input {% html_attrs input_attrs %} />
        <label {% html_attrs label_attrs class=label_classes for=id %}>
            {% slot "default" / %}
        </label>
    """
