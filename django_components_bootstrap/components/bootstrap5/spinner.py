from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import Size, SpinnerVariant, Variant
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Spinner", registry=comp_registry)
class Spinner(Component):
    class Kwargs:
        animation: SpinnerVariant = "border"
        size: Size | None = None
        variant: Variant | None = None
        label: str = "Loading..."
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        base_class = f"spinner-{kwargs.animation}"
        classes = [base_class]

        if kwargs.size:
            classes.append(f"{base_class}-{kwargs.size}")

        if kwargs.variant:
            classes.append(f"text-{kwargs.variant}")

        return {
            "classes": " ".join(classes),
            "label": kwargs.label,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class=classes role="status" %}>
            <span class="visually-hidden">{{ label }}</span>
        </div>
    """
