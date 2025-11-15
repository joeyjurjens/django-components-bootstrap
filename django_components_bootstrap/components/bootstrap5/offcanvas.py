from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
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
        backdrop: Literal["static", "true", "false"] | None = None
        scroll: bool = False
        keyboard: bool = True
        responsive: Breakpoint | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "offcanvas" offcanvas_id=offcanvas_id %}
            <div {% html_attrs attrs defaults:id=offcanvas_id class=classes defaults:tabindex="-1" defaults:aria-labelledby="{{ offcanvas_id }}-label" %} {% if backdrop %}data-bs-backdrop="{{ backdrop }}"{% endif %} data-bs-scroll="{% if scroll %}true{% else %}false{% endif %}" data-bs-keyboard="{% if keyboard %}true{% else %}false{% endif %}">
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("OffcanvasHeader", registry=comp_registry)
class OffcanvasHeader(Component):
    class Kwargs:
        close_button: bool = True
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "close_button": kwargs.close_button,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="offcanvas-header" %}>
            {% slot "default" / %}
            {% if close_button %}
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="offcanvas-body" %}>
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs defaults:class="offcanvas-title" defaults:id="{{ offcanvas_id }}-label" %}>
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs defaults:data-bs-toggle="offcanvas" defaults:data-bs-target="#{{ target_id }}" defaults:aria-controls=target_id %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
