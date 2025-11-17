from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class LayoutTestCase(SimpleTestCase):
    maxDiff = None

    def assertHTMLEqual(self, actual, expected):
        super().assertHTMLEqual(normalize_html(actual), normalize_html(expected))

    def test_basic_container(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" %}
                Content
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container">
                Content
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_container_fluid(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" fluid=True %}
                Content
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container-fluid">
                Content
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_container_fluid_breakpoint(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" fluid="md" %}
                Content
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container-md">
                Content
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_basic_row_with_cols(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" %}
                {% bootstrap5 "Row" %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container">
                <div class="row">
                    <div class="col">Column</div>
                    <div class="col">Column</div>
                    <div class="col">Column</div>
                </div>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_responsive_columns(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" %}
                {% bootstrap5 "Row" %}
                    {% bootstrap5 "Col" sm=8 %}col-sm-8{% endbootstrap5 %}
                    {% bootstrap5 "Col" sm=4 %}col-sm-4{% endbootstrap5 %}
                {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container">
                <div class="row">
                    <div class="col-sm-8">col-sm-8</div>
                    <div class="col-sm-4">col-sm-4</div>
                </div>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_mixed_responsive_columns(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" %}
                {% bootstrap5 "Row" %}
                    {% bootstrap5 "Col" md=8 %}.col-md-8{% endbootstrap5 %}
                    {% bootstrap5 "Col" col=6 md=4 %}.col-6 .col-md-4{% endbootstrap5 %}
                {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container">
                <div class="row">
                    <div class="col-md-8">.col-md-8</div>
                    <div class="col-6 col-md-4">.col-6 .col-md-4</div>
                </div>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_row_with_gutters(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" %}
                {% bootstrap5 "Row" gutter=3 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container">
                <div class="row g-3">
                    <div class="col">Column</div>
                    <div class="col">Column</div>
                </div>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_row_cols(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" %}
                {% bootstrap5 "Row" cols=2 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                    {% bootstrap5 "Col" %}Column{% endbootstrap5 %}
                {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container">
                <div class="row row-cols-2">
                    <div class="col">Column</div>
                    <div class="col">Column</div>
                    <div class="col">Column</div>
                    <div class="col">Column</div>
                </div>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_col_auto(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Container" %}
                {% bootstrap5 "Row" %}
                    {% bootstrap5 "Col" %}1 of 3{% endbootstrap5 %}
                    {% bootstrap5 "Col" col="auto" %}Variable width content{% endbootstrap5 %}
                    {% bootstrap5 "Col" %}3 of 3{% endbootstrap5 %}
                {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="container">
                <div class="row">
                    <div class="col">1 of 3</div>
                    <div class="col-auto">Variable width content</div>
                    <div class="col">3 of 3</div>
                </div>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)
