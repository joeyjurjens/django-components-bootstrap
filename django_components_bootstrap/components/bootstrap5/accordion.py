from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Accordion", registry=bs5_registry)
class Accordion(Component):
    class Kwargs:
        flush: bool = False
        always_open: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        accordion_id = f"accordion-{self.id}"

        css_classes = ["accordion"]
        if kwargs.flush:
            css_classes.append("accordion-flush")

        return {
            "accordion_id": accordion_id,
            "css_class": " ".join(css_classes),
            "always_open": kwargs.always_open,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "accordion" accordion_id=accordion_id always_open=always_open %}
            <div {% html_attrs attrs class=css_class id=accordion_id %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("AccordionItem", registry=bs5_registry)
class AccordionItem(Component):
    class Kwargs:
        default_open: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        accordion = self.inject("accordion")

        heading_id = f"heading-{self.id}"
        collapse_id = f"collapse-{self.id}"
        data_bs_parent = f"#{accordion.accordion_id}"

        return {
            "heading_id": heading_id,
            "collapse_id": collapse_id,
            "is_open": kwargs.default_open,
            "data_bs_parent": data_bs_parent,
            "always_open": accordion.always_open,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "accordion_item" heading_id=heading_id collapse_id=collapse_id is_open=is_open data_bs_parent=data_bs_parent always_open=always_open %}
            <div {% html_attrs attrs class="accordion-item" %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("AccordionButton", registry=bs5_registry)
class AccordionButton(Component):
    class Kwargs:
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        accordion_item = self.inject("accordion_item")

        classes = ["accordion-button"]
        if not accordion_item.is_open:
            classes.append("collapsed")

        return {
            "button_classes": " ".join(classes),
            "collapse_id": accordion_item.collapse_id,
            "aria_expanded": "true" if accordion_item.is_open else "false",
            "disabled": kwargs.disabled,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <button {% html_attrs attrs class=button_classes type="button" data-bs-toggle="collapse" data-bs-target="#{{ collapse_id }}" defaults:aria-expanded=aria_expanded defaults:aria-controls=collapse_id disabled=disabled %}>
            {% slot "default" / %}
        </button>
    """


@register("AccordionHeader", registry=bs5_registry)
class AccordionHeader(Component):
    class Kwargs:
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        accordion_item = self.inject("accordion_item")

        return {
            "heading_id": accordion_item.heading_id,
            "disabled": kwargs.disabled,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <h2 {% html_attrs attrs class="accordion-header" id=heading_id %}>
            {% bootstrap5 "AccordionButton" disabled=disabled %}
                {% slot "default" / %}
            {% endbootstrap5 %}
        </h2>
    """


@register("AccordionBody", registry=bs5_registry)
class AccordionBody(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        accordion_item = self.inject("accordion_item")

        collapse_classes = ["accordion-collapse", "collapse"]
        if accordion_item.is_open:
            collapse_classes.append("show")

        return {
            "heading_id": accordion_item.heading_id,
            "collapse_id": accordion_item.collapse_id,
            "collapse_classes": " ".join(collapse_classes),
            "data_bs_parent": accordion_item.data_bs_parent,
            "always_open": accordion_item.always_open,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs id=collapse_id class=collapse_classes defaults:aria-labelledby=heading_id %} {% if not always_open %}data-bs-parent="{{ data_bs_parent }}"{% endif %}>
            <div {% html_attrs attrs class="accordion-body" %}>
                {% slot "default" / %}
            </div>
        </div>
    """
