from django.template import Context
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import Size


class InputGroup(Component):
    class Kwargs:
        size: Size | None = None
        nowrap: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["input-group"]
        if kwargs.size:
            classes.append(f"input-group-{kwargs.size}")
        if kwargs.nowrap:
            classes.append("flex-nowrap")

        return {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <div {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </div>
    """


class InputGroupText(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <span {% html_attrs attrs class="input-group-text" %}>
            {% slot "default" / %}
        </span>
    """


class InputGroupRadio(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags %}

        <div class="input-group-text">
            <input {% html_attrs attrs type="radio" class="form-check-input mt-0" %} />
        </div>
    """


class InputGroupCheckbox(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags %}

        <div class="input-group-text">
            <input {% html_attrs attrs type="checkbox" class="form-check-input mt-0" %} />
        </div>
    """


class FloatingLabel(Component):
    class Kwargs:
        label: str
        control_id: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "control_id": kwargs.control_id,
            "label": kwargs.label,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        {% provide "formgroup" control_id=control_id %}
            <div {% html_attrs attrs class="form-floating" %}>
                {% slot "default" / %}
                <label{% if control_id %} for="{{ control_id }}"{% endif %}>{{ label }}</label>
            </div>
        {% endprovide %}
    """
