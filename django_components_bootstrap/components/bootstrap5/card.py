from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    Alignment,
    CardImgVariant,
    HeadingLevel,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Card", registry=comp_registry)
class Card(Component):
    class Kwargs:
        as_: str = "div"
        bg: str | None = None
        text: str | None = None
        border: str | None = None
        text_align: Alignment | None = None
        body: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["card"]
        if kwargs.bg and not kwargs.text:
            classes.append(f"text-bg-{kwargs.bg}")
        elif kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")

        if kwargs.text:
            classes.append(f"text-{kwargs.text}")
        if kwargs.border:
            classes.append(f"border-{kwargs.border}")
        if kwargs.text_align:
            classes.append(f"text-{kwargs.text_align}")

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "body": kwargs.body,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """

        <{{ tag }} {% html_attrs attrs class=classes %}>
            {% if body %}
                {% component "CardBody" %}
                    {% slot "default" / %}
                {% endcomponent %}
            {% else %}
                {% slot "default" / %}
            {% endif %}
        </{{ tag }}>
    """


@register("CardHeader", registry=comp_registry)
class CardHeader(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <div {% html_attrs attrs class="card-header" %}>
            {% slot "default" / %}
        </div>
    """


@register("CardBody", registry=comp_registry)
class CardBody(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <div {% html_attrs attrs class="card-body" %}>
            {% slot "default" / %}
        </div>
    """


@register("CardFooter", registry=comp_registry)
class CardFooter(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <div {% html_attrs attrs class="card-footer" %}>
            {% slot "default" / %}
        </div>
    """


@register("CardTitle", registry=comp_registry)
class CardTitle(Component):
    class Kwargs:
        as_: HeadingLevel = "h5"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class="card-title" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("CardSubtitle", registry=comp_registry)
class CardSubtitle(Component):
    class Kwargs:
        as_: HeadingLevel = "h6"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class="card-subtitle" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("CardText", registry=comp_registry)
class CardText(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <p {% html_attrs attrs class="card-text" %}>
            {% slot "default" / %}
        </p>
    """


@register("CardLink", registry=comp_registry)
class CardLink(Component):
    class Kwargs:
        href: str = "#"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "href": kwargs.href,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <a {% html_attrs attrs href=href class="card-link" %}>
            {% slot "default" / %}
        </a>
    """


@register("CardImg", registry=comp_registry)
class CardImg(Component):
    class Kwargs:
        src: str
        alt: str = ""
        position: CardImgVariant | None = None
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        if kwargs.position == "top":
            img_class = "card-img-top"
        elif kwargs.position == "bottom":
            img_class = "card-img-bottom"
        else:
            img_class = "card-img"

        return {
            "src": kwargs.src,
            "alt": kwargs.alt,
            "img_class": img_class,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <img {% html_attrs attrs src=src alt=alt class=img_class %} />
    """


@register("CardImgOverlay", registry=comp_registry)
class CardImgOverlay(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <div {% html_attrs attrs class="card-img-overlay" %}>
            {% slot "default" / %}
        </div>
    """


@register("CardGroup", registry=comp_registry)
class CardGroup(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <div {% html_attrs attrs class="card-group" %}>
            {% slot "default" / %}
        </div>
    """
