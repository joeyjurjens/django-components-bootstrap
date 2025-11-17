from typing import NamedTuple

from django.template import Context
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import NOT_PROVIDED, NavVariant
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


class TabContext(NamedTuple):
    id: str
    tab_data: list[dict]
    enabled: bool


@register("TabContainer", registry=comp_registry)
class TabContainer(Component):
    class Kwargs:
        id: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        container_id = kwargs.id or f"tab-container-{self.id}"

        return {
            "container_id": container_id,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "tab_container" id=container_id %}
            <div {% html_attrs attrs %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


@register("TabContent", registry=comp_registry)
class TabContent(Component):
    class Kwargs:
        as_: str = "div"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs defaults:class="tab-content" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("TabPane", registry=comp_registry)
class TabPane(Component):
    class Kwargs:
        active: bool = False
        fade: bool = True
        as_: str = "div"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["tab-pane"]
        if kwargs.fade:
            classes.append("fade")
        if kwargs.active:
            classes.append("show active")

        return {
            "tag": kwargs.as_,
            "classes": " ".join(classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <{{ tag }} {% html_attrs attrs class=classes defaults:role="tabpanel" defaults:tabindex="0" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


@register("TabsRenderer", registry=comp_registry)
class TabsRenderer(Component):
    class Kwargs:
        tabs_id: str
        variant: NavVariant
        fill: bool
        justified: bool
        default_active_tab: str | None
        tab_data: list[dict]
        attrs: dict | None

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        first_key = kwargs.tab_data[0]["tab_id"] if kwargs.tab_data else None
        active_key = kwargs.default_active_tab or first_key

        return {
            "tabs_id": kwargs.tabs_id,
            "variant": kwargs.variant,
            "fill": kwargs.fill,
            "justified": kwargs.justified,
            "active_key": active_key,
            "tab_data": kwargs.tab_data,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        <div {% html_attrs attrs %}>
            {% component "Nav" variant=variant fill=fill justified=justified as_="ul" attrs:id=tabs_id attrs:role="tablist" %}
                {% for tab in tab_data %}
                    {% component "NavItem" as_="li" attrs:role="presentation" %}
                        {% component "NavLink" as_="button" active=tab.is_active disabled=tab.disabled attrs:id=tab.nav_tab_id attrs:data-bs-toggle="tab" attrs:data-bs-target="#{{ tab.pane_id }}" attrs:role="tab" attrs:aria-controls=tab.pane_id attrs:aria-selected=tab.aria_selected attrs:class=tab.tab_class %}
                            {{ tab.title }}
                        {% endcomponent %}
                    {% endcomponent %}
                {% endfor %}
            {% endcomponent %}
            {% component "TabContent" %}
                {% for tab in tab_data %}
                    {% component "TabPane" active=tab.is_active attrs:id=tab.pane_id attrs:aria-labelledby=tab.nav_tab_id %}
                        {{ tab.content }}
                    {% endcomponent %}
                {% endfor %}
            {% endcomponent %}
        </div>
    """


@register("Tabs", registry=comp_registry)
class Tabs(Component):
    class Kwargs:
        id: str | None = None
        default_active_tab: str | None = None
        variant: NavVariant = "tabs"
        fill: bool = False
        justified: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        tabs_id = kwargs.id or f"tabs-{self.id}"
        tab_data: list[dict] = []

        return {
            "tabs_id": tabs_id,
            "default_active_tab": kwargs.default_active_tab,
            "variant": kwargs.variant,
            "fill": kwargs.fill,
            "justified": kwargs.justified,
            "tab_data": tab_data,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "_tabs" id=tabs_id tab_data=tab_data default_active_tab=default_active_tab enabled=True %}
            {% slot "default" / %}
        {% endprovide %}
    """

    def on_render_after(self, context, template, content):
        tab_data: list[dict] = context["tab_data"]

        return TabsRenderer.render(
            kwargs={
                "tabs_id": context["tabs_id"],
                "variant": context["variant"],
                "fill": context["fill"],
                "justified": context["justified"],
                "default_active_tab": context["default_active_tab"],
                "tab_data": tab_data,
                "attrs": context["attrs"],
            },
            render_dependencies=False,
        )


@register("Tab", registry=comp_registry)
class Tab(Component):
    class Kwargs:
        tab_id: str
        title: str
        disabled: bool = False
        tab_class: str | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        tabs_ctx: TabContext = self.inject("_tabs", NOT_PROVIDED)
        if tabs_ctx is NOT_PROVIDED:
            raise RuntimeError(
                f"'{self.registered_name}' must be used as a child of 'Tabs' component"
            )

        if not tabs_ctx.enabled:
            raise RuntimeError(
                f"'{self.registered_name}' must be a direct child of 'Tabs' component"
            )

        slugs = (slugify(tabs_ctx.id), slugify(kwargs.tab_id))
        nav_tab_id = f"{slugs[0]}-tab-{slugs[1]}"
        pane_id = f"{slugs[0]}-pane-{slugs[1]}"

        is_active = (
            kwargs.tab_id == tabs_ctx.default_active_tab
            if tabs_ctx.default_active_tab
            else len(tabs_ctx.tab_data) == 0
        )

        return {
            "parent_tabs": tabs_ctx.tab_data,
            "nav_tab_id": nav_tab_id,
            "pane_id": pane_id,
            "tab_id": kwargs.tab_id,
            "title": kwargs.title,
            "disabled": kwargs.disabled,
            "tab_class": kwargs.tab_class or "",
            "is_active": is_active,
            "empty_tab_data": [],
        }

    template: types.django_html = """
        {% load component_tags bootstrap5 %}

        {% provide "_tabs" id="" tab_data=empty_tab_data default_active_tab="" enabled=False %}
            {% slot "default" / %}
        {% endprovide %}
    """

    def on_render_after(self, context, template, content):
        parent_tabs: list[dict] = context["parent_tabs"]
        is_active = context["is_active"]
        parent_tabs.append(
            {
                "nav_tab_id": context["nav_tab_id"],
                "pane_id": context["pane_id"],
                "tab_id": context["tab_id"],
                "title": context["title"],
                "disabled": context["disabled"],
                "tab_class": context["tab_class"],
                "is_active": is_active,
                "aria_selected": "true" if is_active else "false",
                "content": mark_safe(content.strip()),
            }
        )
        return None
