from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Badge", registry=comp_registry)
class Badge(Component):
    class Kwargs:
        bg: str = "primary"
        text: str | None = None
        pill: bool = False
        as_: str = "span"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        css_classes = ["badge"]

        if kwargs.bg and not kwargs.text:
            css_classes.append(f"text-bg-{kwargs.bg}")
        elif kwargs.bg:
            css_classes.append(f"bg-{kwargs.bg}")

        if kwargs.pill:
            css_classes.append("rounded-pill")
        if kwargs.text:
            css_classes.append(f"text-{kwargs.text}")

        return {
            "tag": kwargs.as_,
            "css_class": " ".join(css_classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class=css_class %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
