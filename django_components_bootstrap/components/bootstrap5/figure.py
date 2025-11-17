from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Figure", registry=comp_registry)
class Figure(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <figure {% html_attrs attrs class="figure" %}>
            {% slot "default" / %}
        </figure>
    """


@register("FigureImage", registry=comp_registry)
class FigureImage(Component):
    class Kwargs:
        src: str
        alt: str = ""
        fluid: bool = True
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        classes = ["figure-img"]
        if kwargs.fluid:
            classes.append("img-fluid")

        return {
            "src": kwargs.src,
            "alt": kwargs.alt,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <img {% html_attrs attrs class=classes src=src alt=alt %} />
    """


@register("FigureCaption", registry=comp_registry)
class FigureCaption(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <figcaption {% html_attrs attrs class="figure-caption" %}>
            {% slot "default" / %}
        </figcaption>
    """
