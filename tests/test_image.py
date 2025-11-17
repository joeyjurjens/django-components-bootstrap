from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class ImageTests(SimpleTestCase):
    maxDiff = None

    def test_fluid(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Responsive image" fluid=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="img-fluid" alt="Responsive image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_thumbnail(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Thumbnail image" thumbnail=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="img-thumbnail" alt="Thumbnail image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_rounded(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Rounded image" rounded=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="rounded" alt="Rounded image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_rounded_circle(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Circle image" rounded_circle=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="rounded-circle" alt="Circle image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_rounded_float_start(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Float start image" rounded=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="rounded" alt="Float start image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_rounded_float_end(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Float end image" rounded=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="rounded" alt="Float end image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_centered_block(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Centered image" rounded=True attrs:class="mx-auto d-block" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="rounded mx-auto d-block" alt="Centered image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_fluid_and_thumbnail(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Fluid thumbnail" fluid=True thumbnail=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="img-fluid img-thumbnail" alt="Fluid thumbnail">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_all_rounded_options(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Fluid rounded image" fluid=True rounded=True / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" class="img-fluid rounded" alt="Fluid rounded image">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_attrs(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" alt="Custom image" attrs:width="200" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" alt="Custom image" width="200">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_no_alt(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Image" src="https://placehold.net/600x400.png" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <img src="https://placehold.net/600x400.png" alt="">
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
