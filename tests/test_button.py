from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class ButtonTests(SimpleTestCase):
    maxDiff = None

    def test_variant_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" %}Primary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary">Primary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="secondary" %}Secondary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-secondary">Secondary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="success" %}Success{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-success">Success</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="danger" %}Danger{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-danger">Danger</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="warning" %}Warning{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-warning">Warning</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="info" %}Info{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-info">Info</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="light" %}Light{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-light">Light</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="dark" %}Dark{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-dark">Dark</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_link(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="link" %}Link{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-link">Link</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_outline_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" outline=True %}Primary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-outline-primary">Primary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_outline_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="secondary" outline=True %}Secondary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-outline-secondary">Secondary</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_size_large(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" size="lg" %}Large button{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary btn-lg">Large button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_size_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" size="sm" %}Small button{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary btn-sm">Small button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_disabled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" disabled=True %}Disabled button{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary" disabled>Disabled button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_link_button(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" as_="a" href="#" %}Link{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <a class="btn btn-primary" href="#" role="button">Link</a>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_link_button_disabled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" as_="a" href="#" disabled=True %}Disabled link{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <a class="btn btn-primary disabled" href="#" aria-disabled="true" tabindex="-1" role="button">Disabled link</a>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_active_state(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Button" variant="primary" active=True %}Active button{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary active" aria-pressed="true">Active button</button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
