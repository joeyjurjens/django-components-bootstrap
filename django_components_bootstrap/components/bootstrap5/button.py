from django.template import Context
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import (
    ButtonType,
    Size,
    VariantWithLink,
)


class Button(Component):
    class Kwargs:
        as_: str | None = None
        variant: VariantWithLink = "primary"
        outline: bool = False
        size: Size | None = None
        active: bool = False
        disabled: bool = False
        type: ButtonType = "button"
        href: str | None = None
        target: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        if kwargs.as_:
            tag = kwargs.as_
            is_link = tag == "a"
        elif kwargs.href is not None:
            tag = "a"
            is_link = True
        else:
            tag = "button"
            is_link = False

        if kwargs.variant == "link":
            variant_class = "btn-link"
        elif kwargs.outline:
            variant_class = f"btn-outline-{kwargs.variant}"
        else:
            variant_class = f"btn-{kwargs.variant}"

        size_class = f"btn-{kwargs.size}" if kwargs.size else None

        classes = ["btn", variant_class]
        if size_class:
            classes.append(size_class)
        if kwargs.active:
            classes.append("active")
        if kwargs.disabled and is_link:
            classes.append("disabled")

        button_type = kwargs.type if tag == "button" else None
        button_disabled = kwargs.disabled if tag == "button" else None
        aria_pressed = "true" if kwargs.active else None
        link_href = kwargs.href or "#" if is_link else None
        link_target = kwargs.target if is_link else None
        link_role = "button" if is_link else None
        link_aria_disabled = "true" if is_link and kwargs.disabled else None
        link_tabindex = "-1" if is_link and kwargs.disabled else None

        return {
            "tag": tag,
            "classes": " ".join(classes),
            "button_type": button_type,
            "button_disabled": button_disabled,
            "aria_pressed": aria_pressed,
            "link_href": link_href,
            "link_target": link_target,
            "link_role": link_role,
            "link_aria_disabled": link_aria_disabled,
            "link_tabindex": link_tabindex,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <{{ tag }} {% html_attrs attrs class=classes type=button_type disabled=button_disabled aria-pressed=aria_pressed href=link_href target=link_target role=link_role aria-disabled=link_aria_disabled tabindex=link_tabindex %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
