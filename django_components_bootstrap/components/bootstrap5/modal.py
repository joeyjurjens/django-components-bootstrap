from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    BackdropBehavior,
    ButtonTag,
    HeadingLevel,
    ResponsiveBreakpoint,
    SizeWithXl,
)
from django_components_bootstrap.templatetags.bootstrap5 import bs5_registry


@register("Modal", registry=bs5_registry)
class Modal(Component):
    class Kwargs:
        size: SizeWithXl | None = None
        fullscreen: ResponsiveBreakpoint | None = None
        centered: bool = False
        scrollable: bool = False
        backdrop: BackdropBehavior | None = None
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "modal" modal_id=modal_id %}
            <div {% html_attrs attrs id=modal_id class=modal_classes tabindex="-1" defaults:aria-labelledby="{{ modal_id }}-label" defaults:aria-hidden="true" %} {% if backdrop %}data-bs-backdrop="{{ backdrop }}"{% endif %}{% if not keyboard %} data-bs-keyboard="false"{% endif %}>
                <div class="{{ dialog_classes }}">
                    <div class="{{ content_classes }}">
                        {% slot "default" / %}
                    </div>
                </div>
            </div>
        {% endprovide %}
    """


@register("ModalHeader", registry=bs5_registry)
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class="modal-header" %}>
            {% slot "default" / %}
            {% if close_button %}
                {% bootstrap5 "CloseButton" variant=close_variant attrs:aria-label=close_label attrs:data-bs-dismiss="modal" / %}
            {% endif %}
        </div>
    """


@register("ModalBody", registry=bs5_registry)
class ModalBody(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class="modal-body" %}>
            {% slot "default" / %}
        </div>
    """


@register("ModalFooter", registry=bs5_registry)
class ModalFooter(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class="modal-footer" %}>
            {% slot "default" / %}
        </div>
    """


@register("ModalTitle", registry=bs5_registry)
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs class="modal-title" id="{{ modal_id }}-label" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("ModalToggle", registry=bs5_registry)
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs data-bs-toggle="modal" data-bs-target="#{{ target_id }}" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
