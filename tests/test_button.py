from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class ButtonTests(SimpleTestCase):
    maxDiff = None

    def test_variant_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" %}Primary{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary">Primary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="secondary" %}Secondary{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-secondary">Secondary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="success" %}Success{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-success">Success</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="danger" %}Danger{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-danger">Danger</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="warning" %}Warning{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-warning">Warning</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="info" %}Info{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-info">Info</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="light" %}Light{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-light">Light</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="dark" %}Dark{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-dark">Dark</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_link(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="link" %}Link{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-link">Link</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_outline_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" outline=True %}Primary{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-outline-primary">Primary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_outline_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="secondary" outline=True %}Secondary{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-outline-secondary">Secondary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_size_large(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" size="lg" %}Large button{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary btn-lg">Large button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_size_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" size="sm" %}Small button{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary btn-sm">Small button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_disabled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" disabled=True %}Disabled button{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary" disabled>Disabled button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_link_button(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" as_="a" href="#" %}Link{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <a class="btn btn-primary" href="#" role="button">Link</a>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_link_button_disabled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" as_="a" href="#" disabled=True %}Disabled link{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <a class="btn btn-primary disabled" href="#" aria-disabled="true" tabindex="-1" role="button">Disabled link</a>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_active_state(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" active=True %}Active button{% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary active" aria-pressed="true">Active button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
