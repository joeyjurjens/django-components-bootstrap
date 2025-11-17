from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    AlignmentStartEnd,
    AnchorOrButton,
    AutoClose,
    Breakpoint,
    DropdownDirection,
    HeadingLevel,
    Size,
    VariantWithLink,
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
            "attrs": kwargs.attrs,
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
        variant: VariantWithLink = "primary"
        split: bool = False
        size: Size | None = None
        disabled: bool = False
        href: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["btn", f"btn-{kwargs.variant}", "dropdown-toggle"]
        if kwargs.split:
            classes.append("dropdown-toggle-split")
        if kwargs.size:
            classes.append(f"btn-{kwargs.size}")

        disabled = True if kwargs.disabled else None

        return {
            "classes": " ".join(classes),
            "disabled": disabled,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <button {% html_attrs attrs class=classes type="button" data-bs-toggle="dropdown" defaults:aria-expanded="false" disabled=disabled %}>
            {% slot "default" / %}
        </button>
    """


@register("DropdownMenu", registry=comp_registry)
class DropdownMenu(Component):
    class Kwargs:
        align: AlignmentStartEnd | None = None
        align_responsive: dict[Breakpoint, AlignmentStartEnd] | None = None
        align_sm: AlignmentStartEnd | None = None
        align_md: AlignmentStartEnd | None = None
        align_lg: AlignmentStartEnd | None = None
        align_xl: AlignmentStartEnd | None = None
        align_xxl: AlignmentStartEnd | None = None
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
            "attrs": kwargs.attrs,
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

        aria_current = "true" if kwargs.active else None
        button_disabled = True if kwargs.as_ == "button" and kwargs.disabled else None
        link_aria_disabled = "true" if kwargs.as_ == "a" and kwargs.disabled else None
        link_tabindex = "-1" if kwargs.as_ == "a" and kwargs.disabled else None

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "href": kwargs.href,
            "aria_current": aria_current,
            "button_disabled": button_disabled,
            "link_aria_disabled": link_aria_disabled,
            "link_tabindex": link_tabindex,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <li>
            {% if tag == "a" %}
                <a {% html_attrs attrs href=href class=classes aria-current=aria_current aria-disabled=link_aria_disabled tabindex=link_tabindex %}>
                    {% slot "default" / %}
                </a>
            {% else %}
                <button {% html_attrs attrs type="button" class=classes aria-current=aria_current disabled=button_disabled %}>
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <li><hr {% html_attrs attrs class="dropdown-divider" %}></li>
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <li>
            <{{ tag }} {% html_attrs attrs class="dropdown-header" %}>
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
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <li>
            <span {% html_attrs attrs class="dropdown-item-text" %}>
                {% slot "default" / %}
            </span>
        </li>
    """
