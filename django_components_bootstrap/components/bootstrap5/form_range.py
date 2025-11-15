from django.template import Context
from django_components import Component, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("FormRange", registry=comp_registry)
class FormRange(Component):
    class Kwargs:
        min: int | float = 0
        max: int | float = 100
        step: int | float = 1
        value: int | float | None = None
        disabled: bool = False
        id: str | None = None
        name: str | None = None
        attrs: dict | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "min": kwargs.min,
            "max": kwargs.max,
            "step": kwargs.step,
            "value": kwargs.value,
            "id": kwargs.id,
            "name": kwargs.name,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <input {% html_attrs attrs type="range" class="form-range" defaults:min=min defaults:max=max defaults:step=step defaults:value=value defaults:id=id defaults:name=name %} />
    """
