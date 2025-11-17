from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import (
    BreakpointOrAuto,
    ContainerFluid,
)
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Container", registry=comp_registry)
class Container(Component):
    class Kwargs:
        as_: str = "div"
        fluid: ContainerFluid | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        if kwargs.fluid is True:
            container_class = "container-fluid"
        elif kwargs.fluid:
            container_class = f"container-{kwargs.fluid}"
        else:
            container_class = "container"

        return {
            "tag": kwargs.as_,
            "container_class": container_class,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class=container_class %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("Row", registry=comp_registry)
class Row(Component):
    class Kwargs:
        as_: str = "div"
        cols: int | None = None
        cols_sm: int | None = None
        cols_md: int | None = None
        cols_lg: int | None = None
        cols_xl: int | None = None
        cols_xxl: int | None = None
        gutter: int | None = None
        gutter_x: int | None = None
        gutter_y: int | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["row"]

        if kwargs.cols is not None:
            classes.append(f"row-cols-{kwargs.cols}")
        if kwargs.cols_sm is not None:
            classes.append(f"row-cols-sm-{kwargs.cols_sm}")
        if kwargs.cols_md is not None:
            classes.append(f"row-cols-md-{kwargs.cols_md}")
        if kwargs.cols_lg is not None:
            classes.append(f"row-cols-lg-{kwargs.cols_lg}")
        if kwargs.cols_xl is not None:
            classes.append(f"row-cols-xl-{kwargs.cols_xl}")
        if kwargs.cols_xxl is not None:
            classes.append(f"row-cols-xxl-{kwargs.cols_xxl}")

        if kwargs.gutter is not None:
            classes.append(f"g-{kwargs.gutter}")
        if kwargs.gutter_x is not None:
            classes.append(f"gx-{kwargs.gutter_x}")
        if kwargs.gutter_y is not None:
            classes.append(f"gy-{kwargs.gutter_y}")

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("Col", registry=comp_registry)
class Col(Component):
    class Kwargs:
        as_: str = "div"
        col: BreakpointOrAuto | None = None  # Base col without breakpoint
        xs: BreakpointOrAuto | None = None
        sm: BreakpointOrAuto | None = None
        md: BreakpointOrAuto | None = None
        lg: BreakpointOrAuto | None = None
        xl: BreakpointOrAuto | None = None
        xxl: BreakpointOrAuto | None = None
        auto: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = []

        has_breakpoint = any(
            [kwargs.col, kwargs.xs, kwargs.sm, kwargs.md, kwargs.lg, kwargs.xl, kwargs.xxl]
        )

        if not has_breakpoint and not kwargs.auto:
            classes.append("col")
        else:
            if kwargs.col is not None:
                if kwargs.col == "auto":
                    classes.append("col-auto")
                else:
                    classes.append(f"col-{kwargs.col}")

            if kwargs.xs is not None:
                if kwargs.xs == "auto":
                    classes.append("col-auto")
                else:
                    classes.append(f"col-{kwargs.xs}")
            if kwargs.sm is not None:
                if kwargs.sm == "auto":
                    classes.append("col-sm-auto")
                else:
                    classes.append(f"col-sm-{kwargs.sm}")
            if kwargs.md is not None:
                if kwargs.md == "auto":
                    classes.append("col-md-auto")
                else:
                    classes.append(f"col-md-{kwargs.md}")
            if kwargs.lg is not None:
                if kwargs.lg == "auto":
                    classes.append("col-lg-auto")
                else:
                    classes.append(f"col-lg-{kwargs.lg}")
            if kwargs.xl is not None:
                if kwargs.xl == "auto":
                    classes.append("col-xl-auto")
                else:
                    classes.append(f"col-xl-{kwargs.xl}")
            if kwargs.xxl is not None:
                if kwargs.xxl == "auto":
                    classes.append("col-xxl-auto")
                else:
                    classes.append(f"col-xxl-{kwargs.xxl}")
            if kwargs.auto:
                classes.append("col-auto")

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes) if classes else "col",
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        <{{ tag }} {% html_attrs attrs class=classes %}>
            {% slot "default" / %}
        </{{ tag }}>
    """
