from django.template import Context
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import BgColor, Placement


class ToastContainer(Component):
    class Kwargs:
        position: Placement | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["toast-container"]

        if kwargs.position:
            classes.append("position-fixed")
            if kwargs.position == "top":
                classes.append("top-0 start-50 translate-middle-x")
            elif kwargs.position == "bottom":
                classes.append("bottom-0 start-50 translate-middle-x")
            elif kwargs.position == "start":
                classes.append("top-0 start-0")
            elif kwargs.position == "end":
                classes.append("top-0 end-0")

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


class Toast(Component):
    class Kwargs:
        show: bool = False
        autohide: bool = True
        delay: int = 5000
        bg: BgColor | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["toast"]

        if kwargs.show:
            classes.append("show")

        if kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")
            if kwargs.bg in [
                "primary",
                "secondary",
                "success",
                "danger",
                "warning",
                "info",
                "dark",
            ]:
                classes.append("text-white")

        autohide_attr = "false" if not kwargs.autohide else None
        delay_attr = str(kwargs.delay) if kwargs.autohide and kwargs.delay != 5000 else None

        toast_id = (kwargs.attrs or {}).get("id") or f"toast-{self.id}"

        return {
            "toast_id": toast_id,
            "classes": " ".join(classes),
            "autohide_attr": autohide_attr,
            "delay_attr": delay_attr,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <div {% html_attrs attrs defaults:id=toast_id class=classes role="alert" defaults:aria-live="assertive" defaults:aria-atomic="true" data-bs-autohide=autohide_attr data-bs-delay=delay_attr %}>
            {% slot "default" / %}
        </div>
    """


class ToastHeader(Component):
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
        {% load component_tags %}

        <div {% html_attrs attrs class="toast-header" %}>
            {% slot "default" / %}
            {% if close_button %}
                {% component "CloseButton" variant=close_variant attrs:aria-label=close_label attrs:data-bs-dismiss="toast" / %}
            {% endif %}
        </div>
    """


class ToastBody(Component):
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

        <div {% html_attrs attrs class="toast-body" %}>
            {% slot "default" / %}
        </div>
    """
