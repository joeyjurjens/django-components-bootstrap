from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    BackdropBehavior,
    Breakpoint,
    ButtonTag,
    HeadingLevel,
    OffcanvasPlacement,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Offcanvas", registry=comp_registry)
class Offcanvas(Component):
    class Kwargs:
        placement: OffcanvasPlacement = "start"
        backdrop: BackdropBehavior | None = None
        scroll: bool = False
        keyboard: bool = True
        responsive: Breakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput
        toggle: SlotInput = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        offcanvas_id = f"offcanvas-{self.id}"

        if kwargs.responsive:
            classes = [f"offcanvas-{kwargs.responsive}", f"offcanvas-{kwargs.placement}"]
        else:
            classes = ["offcanvas", f"offcanvas-{kwargs.placement}"]

        return {
            "offcanvas_id": offcanvas_id,
            "classes": " ".join(classes),
            "backdrop": kwargs.backdrop,
            "scroll": kwargs.scroll,
            "keyboard": kwargs.keyboard,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% provide "offcanvas" offcanvas_id=offcanvas_id %}
            {% slot "toggle" / %}
            <div {% html_attrs attrs id=offcanvas_id class=classes tabindex="-1" defaults:aria-labelledby="{{ offcanvas_id }}-label" %} {% if backdrop %}data-bs-backdrop="{{ backdrop }}"{% endif %}{% if scroll %} data-bs-scroll="true"{% endif %}{% if not keyboard %} data-bs-keyboard="false"{% endif %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("OffcanvasHeader", registry=comp_registry)
class OffcanvasHeader(Component):
    class Kwargs:
        close_button: bool = True
        close_label: str = "Close"
        close_variant: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "close_button": kwargs.close_button,
            "close_label": kwargs.close_label,
            "close_variant": kwargs.close_variant,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <div {% html_attrs attrs class="offcanvas-header" %}>
            {% slot "default" / %}
            {% if close_button %}
                {% component "CloseButton" variant=close_variant attrs:aria-label=close_label attrs:data-bs-dismiss="offcanvas" / %}
            {% endif %}
        </div>
    """


@register("OffcanvasBody", registry=comp_registry)
class OffcanvasBody(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <div {% html_attrs attrs class="offcanvas-body" %}>
            {% slot "default" / %}
        </div>
    """


@register("OffcanvasTitle", registry=comp_registry)
class OffcanvasTitle(Component):
    class Kwargs:
        as_: HeadingLevel = "h5"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        offcanvas = self.inject("offcanvas")
        offcanvas_id = offcanvas.offcanvas_id

        return {
            "tag": kwargs.as_,
            "offcanvas_id": offcanvas_id,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class="offcanvas-title" id="{{ offcanvas_id }}-label" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("OffcanvasToggle", registry=comp_registry)
class OffcanvasToggle(Component):
    class Kwargs:
        as_: ButtonTag = "button"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        offcanvas = self.inject("offcanvas")
        target_id = offcanvas.offcanvas_id

        return {
            "tag": kwargs.as_,
            "target_id": target_id,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs data-bs-toggle="offcanvas" data-bs-target="#{{ target_id }}" defaults:aria-controls=target_id %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
