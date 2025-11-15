from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import Size
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("InputGroup", registry=comp_registry)
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </div>
    """


@register("InputGroupText", registry=comp_registry)
class InputGroupText(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <span {% html_attrs attrs defaults:class="input-group-text" %}>
            {% slot "default" / %}
        </span>
    """


@register("InputGroupRadio", registry=comp_registry)
class InputGroupRadio(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div class="input-group-text">
            <input {% html_attrs attrs defaults:type="radio" defaults:class="form-check-input mt-0" %} />
        </div>
    """


@register("InputGroupCheckbox", registry=comp_registry)
class InputGroupCheckbox(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div class="input-group-text">
            <input {% html_attrs attrs defaults:type="checkbox" defaults:class="form-check-input mt-0" %} />
        </div>
    """


@register("FloatingLabel", registry=comp_registry)
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "formgroup" control_id=control_id %}
            <div {% html_attrs attrs defaults:class="form-floating" %}>
                {% slot "default" / %}
                <label{% if control_id %} for="{{ control_id }}"{% endif %}>{{ label }}</label>
            </div>
        {% endprovide %}
    """
