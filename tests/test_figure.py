from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class FigureTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Figure" %}
                {% bootstrap5 "FigureImage" src="https://placehold.net/600x400.png" alt="Figure image" / %}
                {% bootstrap5 "FigureCaption" %}A caption for the above image.{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <figure class="figure">
              <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
              <figcaption class="figure-caption">A caption for the above image.</figcaption>
            </figure>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_caption_right_aligned(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Figure" %}
                {% bootstrap5 "FigureImage" src="https://placehold.net/600x400.png" alt="Figure image" / %}
                {% bootstrap5 "FigureCaption" %}A caption for the above image.{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <figure class="figure">
              <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
              <figcaption class="figure-caption">A caption for the above image.</figcaption>
            </figure>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_caption_center_aligned(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Figure" %}
                {% bootstrap5 "FigureImage" src="https://placehold.net/600x400.png" alt="Figure image" / %}
                {% bootstrap5 "FigureCaption" %}A caption for the above image.{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <figure class="figure">
              <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
              <figcaption class="figure-caption">A caption for the above image.</figcaption>
            </figure>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_without_rounded(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Figure" %}
                {% bootstrap5 "FigureImage" src="https://placehold.net/600x400.png" alt="Figure image" / %}
                {% bootstrap5 "FigureCaption" %}A caption for the above image.{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <figure class="figure">
              <img src="https://placehold.net/600x400.png" class="figure-img img-fluid" alt="Figure image">
              <figcaption class="figure-caption">A caption for the above image.</figcaption>
            </figure>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_not_fluid(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Figure" %}
                {% bootstrap5 "FigureImage" src="https://placehold.net/600x400.png" alt="Figure image" fluid=False / %}
                {% bootstrap5 "FigureCaption" %}A caption for the above image.{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <figure class="figure">
              <img src="https://placehold.net/600x400.png" class="figure-img" alt="Figure image">
              <figcaption class="figure-caption">A caption for the above image.</figcaption>
            </figure>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
