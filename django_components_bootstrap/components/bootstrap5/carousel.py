from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Carousel", registry=comp_registry)
class Carousel(Component):
    class Kwargs:
        fade: bool = False
        controls: bool = True
        indicators: bool = True
        ride: bool | Literal["carousel", "true"] = False
        interval: int | None = None
        keyboard: bool = True
        pause: Literal["hover", "false"] = "hover"
        touch: bool = True
        theme: Literal["dark", "light"] | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        carousel_id = f"carousel-{self.id}"

        classes = ["carousel", "slide"]
        if kwargs.fade:
            classes.append("carousel-fade")

        html_attrs = {}
        if kwargs.ride:
            html_attrs["data-bs-ride"] = "carousel" if kwargs.ride is True else kwargs.ride
        if kwargs.interval:
            html_attrs["data-bs-interval"] = kwargs.interval
        html_attrs["data-bs-keyboard"] = "true" if kwargs.keyboard else "false"
        html_attrs["data-bs-pause"] = kwargs.pause
        html_attrs["data-bs-touch"] = "true" if kwargs.touch else "false"
        if kwargs.theme:
            html_attrs["data-bs-theme"] = kwargs.theme

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        items = []

        return {
            "carousel_id": carousel_id,
            "classes": " ".join(classes),
            "controls": kwargs.controls,
            "show_indicators": kwargs.indicators,
            "attrs": final_attrs,
            "items": items,
        }

    template: types.django_html = """
        {% provide "carousel" carousel_id=carousel_id items=items %}
            {# First pass: collect items (hidden) #}
            <div style="display: none;">{% slot "default" required / %}</div>

            {# Second pass: render with indicators #}
            <div {% html_attrs attrs defaults:id=carousel_id class=classes %}>
                {% if show_indicators %}
                    <div class="carousel-indicators">
                        {% for i in items %}
                            <button type="button" data-bs-target="#{{ carousel_id }}" data-bs-slide-to="{{ forloop.counter0 }}" {% if i.active %}class="active" aria-current="true"{% endif %} aria-label="Slide {{ forloop.counter }}"></button>
                        {% endfor %}
                    </div>
                {% endif %}
                <div class="carousel-inner">
                    {% slot "default" required / %}
                </div>
                {% if controls %}
                    <button class="carousel-control-prev" type="button" data-bs-target="#{{ carousel_id }}" data-bs-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#{{ carousel_id }}" data-bs-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="visually-hidden">Next</span>
                    </button>
                {% endif %}
            </div>
        {% endprovide %}
    """


@register("CarouselItem", registry=comp_registry)
class CarouselItem(Component):
    class Kwargs:
        active: bool = False
        interval: int | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        carousel = self.inject("carousel")
        carousel.items.append({"active": kwargs.active})

        classes = ["carousel-item"]
        if kwargs.active:
            classes.append("active")

        return {
            "classes": " ".join(classes),
            "interval": kwargs.interval,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs class=classes defaults:data-bs-interval=interval %}>
            {% slot "default" / %}
        </div>
    """


@register("CarouselCaption", registry=comp_registry)
class CarouselCaption(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="carousel-caption d-none d-md-block" %}>
            {% slot "default" / %}
        </div>
    """


@register("CarouselIndicator", registry=comp_registry)
class CarouselIndicator(Component):
    class Kwargs:
        slide_to: int = 0
        active: bool = False
        aria_label: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        carousel_id = context.get("carousel_id", "")

        html_attrs = {}

        if kwargs.active:
            html_attrs["aria-current"] = "true"
            html_attrs["class"] = "active"

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "carousel_id": carousel_id,
            "slide_to": kwargs.slide_to,
            "aria_label": kwargs.aria_label or f"Slide {kwargs.slide_to + 1}",
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <button {% html_attrs attrs defaults:type="button" defaults:data-bs-target="#{{ carousel_id }}" defaults:data-bs-slide-to=slide_to defaults:aria-label=aria_label %}></button>
    """
