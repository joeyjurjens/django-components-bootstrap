from django.template import Context
from django.utils.safestring import mark_safe
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    CarouselPause,
    CarouselRide,
    ThemeVariant,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Carousel", registry=comp_registry)
class Carousel(Component):
    class Kwargs:
        fade: bool = False
        controls: bool = True
        indicators: bool = True
        ride: CarouselRide = False
        interval: int | None = None
        keyboard: bool = True
        pause: CarouselPause = "hover"
        touch: bool = True
        theme: ThemeVariant | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        carousel_id = f"carousel-{self.id}"
        items = []

        return {
            "carousel_id": carousel_id,
            "fade": kwargs.fade,
            "controls": kwargs.controls,
            "indicators": kwargs.indicators,
            "ride": kwargs.ride,
            "interval": kwargs.interval,
            "keyboard": kwargs.keyboard,
            "pause": kwargs.pause,
            "touch": kwargs.touch,
            "theme": kwargs.theme,
            "attrs": kwargs.attrs,
            "items": items,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "carousel" carousel_id=carousel_id items=items %}
            {% slot "default" required / %}
        {% endprovide %}
    """

    def on_render_after(self, context, template, content):
        items: list[dict] = context["items"]

        return CarouselRenderer.render(
            kwargs={
                "carousel_id": context["carousel_id"],
                "fade": context["fade"],
                "controls": context["controls"],
                "indicators": context["indicators"],
                "ride": context["ride"],
                "interval": context["interval"],
                "keyboard": context["keyboard"],
                "pause": context["pause"],
                "touch": context["touch"],
                "theme": context["theme"],
                "attrs": context["attrs"],
                "items": items,
            },
            slots={"default": mark_safe(content)},
            render_dependencies=False,
        )


@register("CarouselRenderer", registry=comp_registry)
class CarouselRenderer(Component):
    class Kwargs:
        carousel_id: str
        fade: bool
        controls: bool
        indicators: bool
        ride: CarouselRide
        interval: int | None
        keyboard: bool
        pause: CarouselPause
        touch: bool
        theme: ThemeVariant | None
        items: list[dict]
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["carousel", "slide"]
        if kwargs.fade:
            classes.append("carousel-fade")

        data_bs_ride = "carousel" if kwargs.ride is True else kwargs.ride if kwargs.ride else None
        data_bs_interval = kwargs.interval
        data_bs_keyboard = "false" if not kwargs.keyboard else None
        data_bs_pause = kwargs.pause if kwargs.pause != "hover" else None
        data_bs_touch = "false" if not kwargs.touch else None
        data_bs_theme = kwargs.theme

        return {
            "carousel_id": kwargs.carousel_id,
            "classes": " ".join(classes),
            "controls": kwargs.controls,
            "show_indicators": kwargs.indicators,
            "data_bs_ride": data_bs_ride,
            "data_bs_interval": data_bs_interval,
            "data_bs_keyboard": data_bs_keyboard,
            "data_bs_pause": data_bs_pause,
            "data_bs_touch": data_bs_touch,
            "data_bs_theme": data_bs_theme,
            "attrs": kwargs.attrs,
            "items": kwargs.items,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "carousel" carousel_id=carousel_id %}
            <div {% html_attrs attrs id=carousel_id class=classes data-bs-ride=data_bs_ride data-bs-interval=data_bs_interval data-bs-keyboard=data_bs_keyboard data-bs-pause=data_bs_pause data-bs-touch=data_bs_touch data-bs-theme=data_bs_theme %}>
                {% if show_indicators %}
                    <div class="carousel-indicators">
                        {% for item in items %}
                            {% component "CarouselIndicator" slide_to=forloop.counter0 active=item.active / %}
                        {% endfor %}
                    </div>
                {% endif %}
            <div class="carousel-inner">
                {% slot "default" required / %}
            </div>
            {% if controls %}
                <button class="carousel-control-prev" type="button" data-bs-target="#{{ carousel_id }}" data-bs-slide="prev">
                    <span {% html_attrs class="carousel-control-prev-icon" defaults:aria-hidden="true" %}></span>
                    <span class="visually-hidden">Previous</span>
                </button>
                <button class="carousel-control-next" type="button" data-bs-target="#{{ carousel_id }}" data-bs-slide="next">
                    <span {% html_attrs class="carousel-control-next-icon" defaults:aria-hidden="true" %}></span>
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

        classes = ["carousel-item"]
        if kwargs.active:
            classes.append("active")

        return {
            "parent_items": carousel.items,
            "active": kwargs.active,
            "classes": " ".join(classes),
            "interval": kwargs.interval,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class=classes data-bs-interval=interval %}>
            {% slot "default" / %}
        </div>
    """

    def on_render_after(self, context, template, content):
        parent_items: list[dict] = context["parent_items"]
        parent_items.append(
            {
                "active": context["active"],
            }
        )
        return None


@register("CarouselCaption", registry=comp_registry)
class CarouselCaption(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
    {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs class="carousel-caption" %}>
            {% slot "default" / %}
        </div>
    """


@register("CarouselIndicator", registry=comp_registry)
class CarouselIndicator(Component):
    class Kwargs:
        slide_to: int = 0
        active: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        carousel_data = self.inject("carousel", None)
        carousel_id = carousel_data.carousel_id if carousel_data else ""

        classes = []
        if kwargs.active:
            classes.append("active")

        aria_label = f"Slide {kwargs.slide_to + 1}"

        return {
            "carousel_id": carousel_id,
            "slide_to": kwargs.slide_to,
            "aria_label": aria_label,
            "active": kwargs.active,
            "classes": " ".join(classes) if classes else None,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <button {% html_attrs attrs type="button" data-bs-target="#{{ carousel_id }}" data-bs-slide-to=slide_to defaults:aria-label=aria_label %}{% if classes %} class="{{ classes }}"{% endif %}{% if active %} aria-current="true"{% endif %}></button>
    """
