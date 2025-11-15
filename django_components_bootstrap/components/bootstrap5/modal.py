from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    ButtonTag,
    HeadingLevel,
    ResponsiveBreakpoint,
    SizeWithXl,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Modal", registry=comp_registry)
class Modal(Component):
    class Kwargs:
        size: SizeWithXl | None = None
        fullscreen: ResponsiveBreakpoint | None = None
        centered: bool = False
        scrollable: bool = False
        backdrop: Literal["static", "true", "false"] | None = None
        keyboard: bool = True
        fade: bool = True
        dialog_class: str | None = None
        content_class: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        modal_id = f"modal-{self.id}"

        modal_classes = ["modal"]
        if kwargs.fade:
            modal_classes.append("fade")

        dialog_classes = ["modal-dialog"]
        if kwargs.size:
            dialog_classes.append(f"modal-{kwargs.size}")
        if kwargs.fullscreen is not None:
            if kwargs.fullscreen is True:
                dialog_classes.append("modal-fullscreen")
            else:
                dialog_classes.append(f"modal-fullscreen-{kwargs.fullscreen}-down")
        if kwargs.centered:
            dialog_classes.append("modal-dialog-centered")
        if kwargs.scrollable:
            dialog_classes.append("modal-dialog-scrollable")
        if kwargs.dialog_class:
            dialog_classes.append(kwargs.dialog_class)

        content_classes = ["modal-content"]
        if kwargs.content_class:
            content_classes.append(kwargs.content_class)

        return {
            "modal_id": modal_id,
            "modal_classes": " ".join(modal_classes),
            "dialog_classes": " ".join(dialog_classes),
            "content_classes": " ".join(content_classes),
            "backdrop": kwargs.backdrop,
            "keyboard": kwargs.keyboard,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "modal" modal_id=modal_id %}
            <div {% html_attrs attrs defaults:id=modal_id class=modal_classes defaults:tabindex="-1" defaults:aria-labelledby="{{ modal_id }}-label" defaults:aria-hidden="true" %} {% if backdrop %}data-bs-backdrop="{{ backdrop }}"{% endif %} data-bs-keyboard="{% if keyboard %}true{% else %}false{% endif %}">
                <div class="{{ dialog_classes }}">
                    <div class="{{ content_classes }}">
                        {% slot "default" / %}
                    </div>
                </div>
            </div>
        {% endprovide %}
    """


@register("ModalHeader", registry=comp_registry)
class ModalHeader(Component):
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
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="modal-header" %}>
            {% slot "default" / %}
            {% if close_button %}
                {% component "CloseButton" aria_label=close_label variant=close_variant attrs={"data-bs-dismiss": "modal"} / %}
            {% endif %}
        </div>
    """


@register("ModalBody", registry=comp_registry)
class ModalBody(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="modal-body" %}>
            {% slot "default" / %}
        </div>
    """


@register("ModalFooter", registry=comp_registry)
class ModalFooter(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="modal-footer" %}>
            {% slot "default" / %}
        </div>
    """


@register("ModalTitle", registry=comp_registry)
class ModalTitle(Component):
    class Kwargs:
        as_: HeadingLevel = "h5"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        modal = self.inject("modal")
        modal_id = modal.modal_id

        return {
            "tag": kwargs.as_,
            "modal_id": modal_id,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs defaults:class="modal-title" defaults:id="{{ modal_id }}-label" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("ModalToggle", registry=comp_registry)
class ModalToggle(Component):
    class Kwargs:
        as_: ButtonTag = "button"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        modal = self.inject("modal")
        target_id = modal.modal_id

        return {
            "tag": kwargs.as_,
            "target_id": target_id,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs defaults:data-bs-toggle="modal" defaults:data-bs-target="#{{ target_id }}" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
