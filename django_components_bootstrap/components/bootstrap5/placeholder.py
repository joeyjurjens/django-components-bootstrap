from django.template import Context
from django_components import Component, types

from django_components_bootstrap.components.bootstrap5.types import BgColor, Size, Variant


class Placeholder(Component):
    class Kwargs:
        as_: str = "span"
        size: Size | None = None
        bg: BgColor | None = None
        animation: str | None = None
        xs: int | None = None
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        classes = ["placeholder"]

        if kwargs.size:
            classes.append(f"placeholder-{kwargs.size}")

        if kwargs.bg:
            classes.append(f"bg-{kwargs.bg}")

        if kwargs.animation:
            classes.append(f"placeholder-{kwargs.animation}")

        if kwargs.xs:
            classes.append(f"col-{kwargs.xs}")

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <{{ tag }} {% html_attrs attrs class=classes %}></{{ tag }}>
    """


class PlaceholderButton(Component):
    class Kwargs:
        variant: Variant = "primary"
        xs: int | None = None
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        classes = ["btn", f"btn-{kwargs.variant}", "placeholder"]

        if kwargs.xs:
            classes.append(f"col-{kwargs.xs}")

        return {
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <button {% html_attrs attrs class=classes disabled=True defaults:aria-hidden="true" %}></button>
    """
