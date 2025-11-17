from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import AutoClose
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("NavDropdown", registry=comp_registry)
class NavDropdown(Component):
    class Kwargs:
        title: str
        active: bool = False
        disabled: bool = False
        auto_close: AutoClose | None = None
        align: str | None = None
        dark: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        dropdown_id = f"nav-dropdown-{self.id}"

        # Merge default attrs with user-provided attrs
        # User attrs override defaults
        default_attrs = {
            "id": dropdown_id,
            "class": "dropdown-toggle",
            "data-bs-toggle": "dropdown",
            "aria-expanded": "false",
        }
        merged_attrs = {**default_attrs, **(kwargs.attrs or {})}

        return {
            "dropdown_id": dropdown_id,
            "title": kwargs.title,
            "active": kwargs.active,
            "disabled": kwargs.disabled,
            "auto_close": kwargs.auto_close,
            "align": kwargs.align,
            "dark": kwargs.dark,
            "merged_attrs": merged_attrs,
        }

    template: types.django_html = """
        <li class="nav-item dropdown">
            {% component "NavLink" as_="button" disabled=disabled attrs=merged_attrs %}
                {{ title }}
            {% endcomponent %}
            {% component "DropdownMenu" align=align dark=dark %}
                {% slot "default" / %}
            {% endcomponent %}
        </li>
    """
