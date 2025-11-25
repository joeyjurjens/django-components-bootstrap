from typing import NamedTuple

from django.template import Context
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from django_components import Component, SlotInput, types

from django_components_bootstrap.components.bootstrap5.types import NOT_PROVIDED, NavVariant


class TabContext(NamedTuple):
    id: str
    tab_data: list[dict]
    enabled: bool


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
        {% load component_tags %}

        {% provide "tab_container" id=container_id %}
            <div {% html_attrs attrs %}>
                {% slot "default" / %}
            </div>
        {% endprovide %}
    """


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
        {% load component_tags %}

        <{{ tag }} {% html_attrs attrs defaults:class="tab-content" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


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
        {% load component_tags %}

        <{{ tag }} {% html_attrs attrs class=classes defaults:role="tabpanel" defaults:tabindex="0" %}>
            {% slot "default" / %}
        </{{ tag }}>
    """


class TabsRenderer(Component):
    class Kwargs:
        tabs_id: str
        variant: NavVariant
        fill: bool
        justified: bool
        tab_data: list[dict]
        attrs: dict | None

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        return {
            "tabs_id": kwargs.tabs_id,
            "variant": kwargs.variant,
            "fill": kwargs.fill,
            "justified": kwargs.justified,
            "tab_data": kwargs.tab_data,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% load component_tags %}

        <div {% html_attrs attrs %}>
            {% component "Nav" variant=variant fill=fill justified=justified as_="ul" attrs:id=tabs_id attrs:role="tablist" %}
                {% for tab in tab_data %}
                    {% component "NavItem" as_="li" attrs:role="presentation" %}
                        {% component "NavLink" as_="button" active=tab.is_active disabled=tab.disabled attrs:id=tab.nav_tab_id attrs:data-bs-toggle="tab" attrs:data-bs-target="#{{ tab.pane_id }}" attrs:role="tab" attrs:aria-controls=tab.pane_id attrs:aria-selected=tab.aria_selected %}
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


class Tabs(Component):
    class Kwargs:
        id: str | None = None
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
            "variant": kwargs.variant,
            "fill": kwargs.fill,
            "justified": kwargs.justified,
            "tab_data": tab_data,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% load component_tags %}

        {% provide "_tabs" id=tabs_id tab_data=tab_data enabled=True %}
            {% slot "default" / %}
        {% endprovide %}
    """

    def on_render_after(self, context, template, content):
        tab_data: list[dict] = context["tab_data"]

        if tab_data and not any(tab["is_active"] for tab in tab_data):
            tab_data[0]["is_active"] = True
            tab_data[0]["aria_selected"] = "true"

        return TabsRenderer.render(
            kwargs={
                "tabs_id": context["tabs_id"],
                "variant": context["variant"],
                "fill": context["fill"],
                "justified": context["justified"],
                "tab_data": tab_data,
                "attrs": context["attrs"],
            },
            render_dependencies=False,
        )


class Tab(Component):
    class Kwargs:
        title: str
        tab_id: str | None = None
        active: bool = False
        disabled: bool = False

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

        tab_index = len(tabs_ctx.tab_data)
        tab_id = kwargs.tab_id or slugify(kwargs.title) or f"tab-{tab_index}"
        slugs = (slugify(tabs_ctx.id), tab_id)
        nav_tab_id = f"{slugs[0]}-tab-{slugs[1]}"
        pane_id = f"{slugs[0]}-pane-{slugs[1]}"

        return {
            "parent_tabs": tabs_ctx.tab_data,
            "nav_tab_id": nav_tab_id,
            "pane_id": pane_id,
            "tab_id": tab_id,
            "title": kwargs.title,
            "active": kwargs.active,
            "disabled": kwargs.disabled,
            "empty_tab_data": [],
        }

    template: types.django_html = """
        {% load component_tags %}

        {% provide "_tabs" id="" tab_data=empty_tab_data enabled=False %}
            {% slot "default" / %}
        {% endprovide %}
    """

    def on_render_after(self, context, template, content):
        parent_tabs: list[dict] = context["parent_tabs"]
        is_active = context["active"]

        parent_tabs.append(
            {
                "nav_tab_id": context["nav_tab_id"],
                "pane_id": context["pane_id"],
                "tab_id": context["tab_id"],
                "title": context["title"],
                "disabled": context["disabled"],
                "is_active": is_active,
                "aria_selected": "true" if is_active else "false",
                "content": mark_safe(content.strip()),
            }
        )
        return None
