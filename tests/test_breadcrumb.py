from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class BreadcrumbTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" %}
                {% bootstrap5 "BreadcrumbItem" href="#" %}Home{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" active=True %}Library{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Library</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_single_item_active(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" %}
                {% bootstrap5 "BreadcrumbItem" active=True %}Home{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item active" aria-current="page">Home</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_three_items(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" %}
                {% bootstrap5 "BreadcrumbItem" href="#" %}Home{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" href="#" %}Library{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" active=True %}Data{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item"><a href="#">Library</a></li>
                <li class="breadcrumb-item active" aria-current="page">Data</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_divider_greater_than(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" attrs:style="--bs-breadcrumb-divider: '>';" %}
                {% bootstrap5 "BreadcrumbItem" href="#" %}Home{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" active=True %}Library{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav style="--bs-breadcrumb-divider: '>';" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Library</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_no_divider(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" attrs:style="--bs-breadcrumb-divider: '';" %}
                {% bootstrap5 "BreadcrumbItem" href="#" %}Home{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" active=True %}Library{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav style="--bs-breadcrumb-divider: '';" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Library</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_label(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" %}
                {% bootstrap5 "BreadcrumbItem" href="#" %}Home{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" active=True %}Library{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Library</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_attrs(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" attrs:class="custom-class" %}
                {% bootstrap5 "BreadcrumbItem" href="#" %}Home{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" active=True %}Library{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav class="custom-class" aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item"><a href="#">Home</a></li>
                <li class="breadcrumb-item active" aria-current="page">Library</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_item_custom_attrs(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Breadcrumb" %}
                {% bootstrap5 "BreadcrumbItem" href="#" attrs:data-test="home" %}Home{% endbootstrap5 %}
                {% bootstrap5 "BreadcrumbItem" active=True attrs:class="highlighted" %}Library{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="breadcrumb">
              <ol class="breadcrumb">
                <li class="breadcrumb-item" data-test="home"><a href="#">Home</a></li>
                <li class="breadcrumb-item active highlighted" aria-current="page">Library</li>
              </ol>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
