from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class CloseButtonTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close" aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_disabled(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" disabled=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close" disabled aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_white_variant(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" variant="white" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close btn-close-white" aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_white_variant_disabled(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" variant="white" disabled=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close btn-close-white" disabled aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_aria_label(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close" aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_attrs(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" attrs:class="custom-class" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close custom-class" aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_data_bs_dismiss(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" attrs:data-bs-dismiss="modal" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_data_bs_dismiss_alert(self):
        template = Template("""
            {% load component_tags %}
            {% component "CloseButton" attrs:data-bs-dismiss="alert" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
