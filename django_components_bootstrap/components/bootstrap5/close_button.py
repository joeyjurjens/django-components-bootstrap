from django.template import Context
from django_components import Component, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("CloseButton", registry=comp_registry)
class CloseButton(Component):
    class Kwargs:
        variant: str | None = None
        disabled: bool = False
        aria_label: str = "Close"
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        classes = ["btn-close"]
        if kwargs.variant:
            classes.append(f"btn-close-{kwargs.variant}")

        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "classes": " ".join(classes),
            "aria_label": kwargs.aria_label,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <button {% html_attrs attrs type="button" class=classes defaults:aria-label=aria_label %}></button>
    """
