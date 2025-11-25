from django.template import Context
from django_components import Component, SlotInput, types



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
        {% load component_tags %}

        <figure {% html_attrs attrs class="figure" %}>
            {% slot "default" / %}
        </figure>
    """


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
        {% load component_tags %}

        <img {% html_attrs attrs class=classes src=src alt=alt %} />
    """


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
    {% load component_tags %}

        <figcaption {% html_attrs attrs class="figure-caption" %}>
            {% slot "default" / %}
        </figcaption>
    """
