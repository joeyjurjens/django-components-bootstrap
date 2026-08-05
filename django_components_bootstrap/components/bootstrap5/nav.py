from django.template import Context
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import (
    NOT_PROVIDED,
    AnchorOrButton,
    NavItemTag,
    NavTag,
    NavVariant,
)


class Nav(Component):
    class Kwargs:
        variant: NavVariant | None = None
        fill: bool = False
        justified: bool = False
        vertical: bool = False
        as_: NavTag = "nav"
        role: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["nav"]

        if kwargs.variant == "tabs":
            classes.append("nav-tabs")
        elif kwargs.variant == "pills":
            classes.append("nav-pills")
        elif kwargs.variant == "underline":
            classes.append("nav-underline")

        if kwargs.fill:
            classes.append("nav-fill")
        if kwargs.justified:
            classes.append("nav-justified")

        if kwargs.vertical:
            classes.append("flex-column")

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "role": kwargs.role,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <{{ tag }} {% html_attrs attrs class=classes defaults:role=role %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


class NavItem(Component):
    class Kwargs:
        as_: NavItemTag = "li"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags %}

        <{{ tag }} {% html_attrs attrs class="nav-item" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


class NavLink(Component):
    class Kwargs:
        as_: AnchorOrButton = "a"
        href: str = "#"
        event_key: str | None = None
        active: bool | None = None
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        tab_container = self.inject("tab_container", NOT_PROVIDED)

        is_active = kwargs.active
        is_tab = False
        generated_id = None
        generated_controls = None
        data_bs_target = None

        if kwargs.event_key is not None and tab_container is not NOT_PROVIDED:
            is_tab = True
            if is_active is None:
                is_active = kwargs.event_key == tab_container.active_key
            generated_id = f"{tab_container.id}-tab-{kwargs.event_key}"
            generated_controls = f"{tab_container.id}-pane-{kwargs.event_key}"
            data_bs_target = f"#{generated_controls}"

        is_active = bool(is_active)

        classes = ["nav-link"]
        if is_active:
            classes.append("active")
        if kwargs.disabled:
            classes.append("disabled")

        button_disabled = True if kwargs.as_ == "button" and kwargs.disabled else None
        aria_disabled = "true" if kwargs.as_ == "a" and kwargs.disabled else None
        aria_current = "page" if is_active and kwargs.as_ == "a" and not is_tab else None
        aria_selected = "true" if is_tab and is_active else "false" if is_tab else None
        role = "tab" if is_tab else None
        data_bs_toggle = "tab" if is_tab else None

        link_href = None if kwargs.disabled else kwargs.href

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "href": link_href,
            "button_disabled": button_disabled,
            "aria_disabled": aria_disabled,
            "aria_current": aria_current,
            "aria_selected": aria_selected,
            "role": role,
            "data_bs_toggle": data_bs_toggle,
            "data_bs_target": data_bs_target,
            "generated_id": generated_id,
            "generated_controls": generated_controls,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        {% if tag == "a" %}
            <a {% html_attrs attrs defaults:href=href class=classes defaults:aria-disabled=aria_disabled defaults:aria-current=aria_current defaults:id=generated_id defaults:role=role defaults:data-bs-toggle=data_bs_toggle defaults:data-bs-target=data_bs_target defaults:aria-controls=generated_controls defaults:aria-selected=aria_selected %}>
                {% slot "default" / %}
            </a>
        {% else %}
            <button {% html_attrs attrs defaults:type="button" class=classes defaults:disabled=button_disabled defaults:aria-current=aria_current defaults:id=generated_id defaults:role=role defaults:data-bs-toggle=data_bs_toggle defaults:data-bs-target=data_bs_target defaults:aria-controls=generated_controls defaults:aria-selected=aria_selected %}>
                {% slot "default" / %}
            </button>
        {% endif %}
    """
