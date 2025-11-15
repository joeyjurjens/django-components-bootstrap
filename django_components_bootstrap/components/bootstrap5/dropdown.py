from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    AnchorOrButton,
    AutoClose,
    Breakpoint,
    DropdownDirection,
    HeadingLevel,
    Size,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Dropdown", registry=comp_registry)
class Dropdown(Component):
    class Kwargs:
        direction: DropdownDirection = "down"
        centered: bool = False
        auto_close: AutoClose | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        dropdown_id = f"dropdown-{self.id}"

        if kwargs.centered:
            if kwargs.direction == "up":
                wrapper_class = "dropup dropup-center"
            else:
                wrapper_class = "dropdown dropdown-center"
        else:
            if kwargs.direction == "up":
                wrapper_class = "dropup"
            elif kwargs.direction == "end":
                wrapper_class = "dropend"
            elif kwargs.direction == "start":
                wrapper_class = "dropstart"
            else:
                wrapper_class = "dropdown"

        return {
            "dropdown_id": dropdown_id,
            "wrapper_class": wrapper_class,
            "auto_close": kwargs.auto_close,
            "direction": kwargs.direction,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "dropdown" dropdown_id=dropdown_id direction=direction auto_close=auto_close %}
            <div {% html_attrs attrs class=wrapper_class %} {% if auto_close %}data-bs-auto-close="{{ auto_close }}"{% endif %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("DropdownToggle", registry=comp_registry)
class DropdownToggle(Component):
    class Kwargs:
        variant: Literal[
            "primary",
            "secondary",
            "success",
            "danger",
            "warning",
            "info",
            "light",
            "dark",
            "link",
        ] = "primary"
        split: bool = False
        size: Size | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["btn", f"btn-{kwargs.variant}", "dropdown-toggle"]
        if kwargs.split:
            classes.append("dropdown-toggle-split")
        if kwargs.size:
            classes.append(f"btn-{kwargs.size}")

        return {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <button {% html_attrs attrs class=classes defaults:type="button" defaults:data-bs-toggle="dropdown" defaults:aria-expanded="false" %}>
            {% slot "default" / %}
        </button>
    """


@register("DropdownMenu", registry=comp_registry)
class DropdownMenu(Component):
    class Kwargs:
        align: Literal["start", "end"] | None = None
        align_responsive: dict[Breakpoint, Literal["start", "end"]] | None = None
        align_sm: Literal["start", "end"] | None = None
        align_md: Literal["start", "end"] | None = None
        align_lg: Literal["start", "end"] | None = None
        align_xl: Literal["start", "end"] | None = None
        align_xxl: Literal["start", "end"] | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["dropdown-menu"]

        if kwargs.align == "end":
            classes.append("dropdown-menu-end")

        if kwargs.align_responsive:
            for breakpoint, alignment in kwargs.align_responsive.items():
                classes.append(f"dropdown-menu-{breakpoint}-{alignment}")

        if kwargs.align_sm:
            classes.append(f"dropdown-menu-sm-{kwargs.align_sm}")
        if kwargs.align_md:
            classes.append(f"dropdown-menu-md-{kwargs.align_md}")
        if kwargs.align_lg:
            classes.append(f"dropdown-menu-lg-{kwargs.align_lg}")
        if kwargs.align_xl:
            classes.append(f"dropdown-menu-xl-{kwargs.align_xl}")
        if kwargs.align_xxl:
            classes.append(f"dropdown-menu-xxl-{kwargs.align_xxl}")

        if kwargs.dark:
            classes.append("dropdown-menu-dark")

        return {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <ul {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </ul>
    """


@register("DropdownItem", registry=comp_registry)
class DropdownItem(Component):
    class Kwargs:
        as_: AnchorOrButton = "a"
        href: str = "#"
        active: bool = False
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["dropdown-item"]
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        html_attrs = {}

        if kwargs.active:
            html_attrs["aria-current"] = "true"

        if kwargs.as_ == "button" and kwargs.disabled:
            html_attrs["disabled"] = True

        if kwargs.as_ == "a":
            html_attrs["aria-disabled"] = "true" if kwargs.disabled else "false"
            if kwargs.disabled:
                html_attrs["tabindex"] = "-1"

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "href": kwargs.href,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <li>
            {% if tag == "a" %}
                <a {% html_attrs attrs defaults:href=href class=classes %}>
                    {% slot "default" / %}
                </a>
            {% else %}
                <button {% html_attrs attrs defaults:type="button" class=classes %}>
                    {% slot "default" / %}
                </button>
            {% endif %}
        </li>
    """


@register("DropdownDivider", registry=comp_registry)
class DropdownDivider(Component):
    class Kwargs:
        attrs: dict | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <li><hr {% html_attrs attrs defaults:class="dropdown-divider" %}></li>
    """


@register("DropdownHeader", registry=comp_registry)
class DropdownHeader(Component):
    class Kwargs:
        as_: HeadingLevel = "h6"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <li>
            <{{ tag }} {% html_attrs attrs defaults:class="dropdown-header" %}>
                {% slot "default" / %}
            </{{ tag }}>
        </li>
    """


@register("DropdownItemText", registry=comp_registry)
class DropdownItemText(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <li>
            <span {% html_attrs attrs defaults:class="dropdown-item-text" %}>
                {% slot "default" / %}
            </span>
        </li>
    """
