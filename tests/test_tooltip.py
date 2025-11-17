from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TooltipTestCase(SimpleTestCase):
    maxDiff = None

    def assertHTMLEqual(self, actual, expected):
        super().assertHTMLEqual(normalize_html(actual), normalize_html(expected))

    def test_tooltip_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Default tooltip" placement="top" %}
                <a href="#">inline links</a>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="tooltip" data-bs-title="Default tooltip" data-bs-placement="top" data-bs-trigger="hover">
                <a href="#">inline links</a>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_tooltip_placement_top(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Tooltip on top" placement="top" %}
                {% component "Button" variant="secondary" %}Top{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="tooltip" data-bs-title="Tooltip on top" data-bs-placement="top" data-bs-trigger="hover">
                <button class="btn btn-secondary" type="button">Top</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_tooltip_placement_right(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Tooltip on right" placement="right" %}
                {% component "Button" variant="secondary" %}Right{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="tooltip" data-bs-title="Tooltip on right" data-bs-placement="right" data-bs-trigger="hover">
                <button class="btn btn-secondary" type="button">Right</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_tooltip_placement_bottom(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Tooltip on bottom" placement="bottom" %}
                {% component "Button" variant="secondary" %}Bottom{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="tooltip" data-bs-title="Tooltip on bottom" data-bs-placement="bottom" data-bs-trigger="hover">
                <button class="btn btn-secondary" type="button">Bottom</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_tooltip_placement_left(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Tooltip on left" placement="left" %}
                {% component "Button" variant="secondary" %}Left{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="tooltip" data-bs-title="Tooltip on left" data-bs-placement="left" data-bs-trigger="hover">
                <button class="btn btn-secondary" type="button">Left</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_tooltip_with_button(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="This top tooltip is themed via CSS variables." placement="top" %}
                {% component "Button" variant="secondary" attrs:data-bs-custom-class="custom-tooltip" %}
                    Custom tooltip
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="tooltip" data-bs-title="This top tooltip is themed via CSS variables." data-bs-placement="top" data-bs-trigger="hover">
                <button type="button" class="btn btn-secondary" data-bs-custom-class="custom-tooltip">
                    Custom tooltip
                </button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_tooltip_disabled_button_wrapper(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Disabled tooltip" placement="top" %}
                <span class="d-inline-block" tabindex="0">
                    {% component "Button" variant="primary" type="button" disabled=True %}Disabled button{% endcomponent %}
                </span>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="tooltip" data-bs-title="Disabled tooltip" data-bs-placement="top" data-bs-trigger="hover">
                <span class="d-inline-block" tabindex="0">
                    <button class="btn btn-primary" type="button" disabled>Disabled button</button>
                </span>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)
