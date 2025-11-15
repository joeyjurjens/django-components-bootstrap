from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Alert", registry=comp_registry)
class Alert(Component):
    class Kwargs:
        variant: str = "primary"
        dismissible: bool = False
        close_label: str = "Close alert"
        close_variant: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        css_classes = ["alert", f"alert-{kwargs.variant}"]

        if kwargs.dismissible:
            css_classes.extend(["alert-dismissible", "fade", "show"])

        return {
            "css_class": " ".join(css_classes),
            "dismissible": kwargs.dismissible,
            "close_label": kwargs.close_label,
            "close_variant": kwargs.close_variant,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs class=css_class defaults:role="alert" %}>
            {% slot "default" / %}
            {% if dismissible %}
                {% component "CloseButton" aria_label=close_label variant=close_variant attrs={"data-bs-dismiss": "alert"} / %}
            {% endif %}
        </div>
    """


@register("AlertLink", registry=comp_registry)
class AlertLink(Component):
    class Kwargs:
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "href": kwargs.href,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <a {% html_attrs attrs defaults:href=href defaults:class="alert-link" %}>
            {% slot "default" / %}
        </a>
    """


@register("AlertHeading", registry=comp_registry)
class AlertHeading(Component):
    class Kwargs:
        as_: str = "h4"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs defaults:class="alert-heading" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
