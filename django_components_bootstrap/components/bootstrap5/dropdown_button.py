from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import AutoClose, Size, VariantWithLink
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("DropdownButton", registry=comp_registry)
class DropdownButton(Component):
    class Kwargs:
        title: str
        variant: VariantWithLink = "primary"
        size: Size | None = None
        disabled: bool = False
        href: str | None = None
        auto_close: AutoClose | None = None
        align: str | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        dropdown_id = f"dropdown-button-{self.id}"

        return {
            "dropdown_id": dropdown_id,
            "title": kwargs.title,
            "variant": kwargs.variant,
            "size": kwargs.size,
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "auto_close": kwargs.auto_close,
            "align": kwargs.align,
            "dark": kwargs.dark,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """

        {% component "Dropdown" auto_close=auto_close attrs=attrs %}
            {% component "DropdownToggle" variant=variant size=size attrs:id=dropdown_id attrs:disabled=disabled attrs:href=href %}
                {{ title }}
            {% endcomponent %}
            {% component "DropdownMenu" align=align dark=dark %}
                {% slot "default" / %}
            {% endcomponent %}
        {% endcomponent %}
    """


@register("SplitButton", registry=comp_registry)
class SplitButton(Component):
    class Kwargs:
        title: str
        variant: VariantWithLink = "primary"
        size: Size | None = None
        disabled: bool = False
        href: str | None = None
        target: str | None = None
        type: str = "button"
        toggle_label: str = "Toggle dropdown"
        auto_close: AutoClose | None = None
        align: str | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        dropdown_id = f"split-button-{self.id}"

        return {
            "dropdown_id": dropdown_id,
            "title": kwargs.title,
            "variant": kwargs.variant,
            "size": kwargs.size,
            "disabled": kwargs.disabled,
            "href": kwargs.href,
            "target": kwargs.target,
            "type": kwargs.type,
            "toggle_label": kwargs.toggle_label,
            "auto_close": kwargs.auto_close,
            "align": kwargs.align,
            "dark": kwargs.dark,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """

        {% component "Dropdown" auto_close=auto_close %}
            {% component "ButtonGroup" attrs=attrs %}
                {% component "Button" variant=variant size=size disabled=disabled href=href attrs:target=target attrs:type=type %}
                    {{ title }}
                {% endcomponent %}
                {% component "DropdownToggle" split=True variant=variant size=size attrs:id=dropdown_id attrs:disabled=disabled %}
                    <span class="visually-hidden">{{ toggle_label }}</span>
                {% endcomponent %}
                {% component "DropdownMenu" align=align dark=dark %}
                    {% slot "default" / %}
                {% endcomponent %}
            {% endcomponent %}
        {% endcomponent %}
    """
