from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    ResponsiveBreakpoint,
    Variant,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Table", registry=comp_registry)
class Table(Component):
    class Kwargs:
        striped: bool = False
        striped_columns: bool = False
        bordered: bool = False
        borderless: bool = False
        hover: bool = False
        small: bool = False
        variant: Variant | None = None
        responsive: ResponsiveBreakpoint | None = None
        caption_top: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["table"]

        if kwargs.striped:
            classes.append("table-striped")
        if kwargs.striped_columns:
            classes.append("table-striped-columns")
        if kwargs.bordered:
            classes.append("table-bordered")
        if kwargs.borderless:
            classes.append("table-borderless")
        if kwargs.hover:
            classes.append("table-hover")
        if kwargs.small:
            classes.append("table-sm")
        if kwargs.variant:
            classes.append(f"table-{kwargs.variant}")
        if kwargs.caption_top:
            classes.append("caption-top")

        responsive_class = None
        if kwargs.responsive is not None:
            if kwargs.responsive is True:
                responsive_class = "table-responsive"
            else:
                responsive_class = f"table-responsive-{kwargs.responsive}"

        return {
            "classes": " ".join(classes),
            "responsive_class": responsive_class,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% if responsive_class %}
            <div class="{{ responsive_class }}">
                <table {% html_attrs attrs class=classes %}>
                    {% slot "default" / %}
                </table>
            </div>
        {% else %}
            <table {% html_attrs attrs class=classes %}>
                {% slot "default" / %}
            </table>
        {% endif %}
    """
