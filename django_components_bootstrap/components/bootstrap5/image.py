from django.template import Context
from django_components import Component, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Image", registry=comp_registry)
class Image(Component):
    class Kwargs:
        src: str
        alt: str = ""
        fluid: bool = False
        rounded: bool = False
        rounded_circle: bool = False
        thumbnail: bool = False
        attrs: dict | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        classes = []
        if kwargs.fluid:
            classes.append("img-fluid")
        if kwargs.rounded:
            classes.append("rounded")
        if kwargs.rounded_circle:
            classes.append("rounded-circle")
        if kwargs.thumbnail:
            classes.append("img-thumbnail")

        return {
            "src": kwargs.src,
            "alt": kwargs.alt,
            "classes": " ".join(classes) if classes else None,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <img {% html_attrs attrs defaults:src=src defaults:alt=alt class=classes %} />
    """
