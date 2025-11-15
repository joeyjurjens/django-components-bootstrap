from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Accordion", registry=comp_registry)
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "accordion" accordion_id=accordion_id always_open=always_open %}
            <div {% html_attrs attrs class=css_class defaults:id=accordion_id %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("AccordionItem", registry=comp_registry)
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "accordion_item" heading_id=heading_id collapse_id=collapse_id is_open=is_open data_bs_parent=data_bs_parent always_open=always_open %}
            <div {% html_attrs attrs defaults:class="accordion-item" %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("AccordionButton", registry=comp_registry)
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
            "collapse_id": accordion_item.collapse_id,
            "is_open": accordion_item.is_open,
            "disabled": kwargs.disabled,
            "button_classes": " ".join(classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """

        <button {% html_attrs attrs class=button_classes defaults:type="button" defaults:data-bs-toggle="collapse" defaults:data-bs-target="#{{ collapse_id }}" defaults:aria-expanded=is_open defaults:aria-controls=collapse_id defaults:disabled=disabled %}>
            {% slot "default" / %}
        </button>
    """


@register("AccordionHeader", registry=comp_registry)
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """

        <h2 {% html_attrs attrs defaults:class="accordion-header" defaults:id=heading_id %}>
            {% component "AccordionButton" disabled=disabled %}
                {% slot "default" / %}
            {% endcomponent %}
        </h2>
    """


@register("AccordionBody", registry=comp_registry)
class AccordionBody(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        accordion_item = self.inject("accordion_item")

        return {
            "heading_id": accordion_item.heading_id,
            "collapse_id": accordion_item.collapse_id,
            "is_open": accordion_item.is_open,
            "data_bs_parent": accordion_item.data_bs_parent,
            "always_open": accordion_item.always_open,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div id="{{ collapse_id }}"
             class="accordion-collapse collapse{% if is_open %} show{% endif %}"
             aria-labelledby="{{ heading_id }}"
             {% if not always_open %}data-bs-parent="{{ data_bs_parent }}"{% endif %}>
            <div {% html_attrs attrs defaults:class="accordion-body" %}>
                {% slot "default" / %}
            </div>
        </div>
    """
