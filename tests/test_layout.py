from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class LayoutTestCase(SimpleTestCase):
    maxDiff = None

    def assertHTMLEqual(self, actual, expected):
        super().assertHTMLEqual(normalize_html(actual), normalize_html(expected))

    def test_basic_container(self):
        template = Template("""
            {% load component_tags %}
            {% component "Container" %}
                Content
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" fluid=True %}
                Content
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" fluid="md" %}
                Content
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" %}
                {% component "Row" %}
                    {% component "Col" %}Column{% endcomponent %}
                    {% component "Col" %}Column{% endcomponent %}
                    {% component "Col" %}Column{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" %}
                {% component "Row" %}
                    {% component "Col" sm=8 %}col-sm-8{% endcomponent %}
                    {% component "Col" sm=4 %}col-sm-4{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" %}
                {% component "Row" %}
                    {% component "Col" md=8 %}.col-md-8{% endcomponent %}
                    {% component "Col" col=6 md=4 %}.col-6 .col-md-4{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" %}
                {% component "Row" gutter=3 %}
                    {% component "Col" %}Column{% endcomponent %}
                    {% component "Col" %}Column{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" %}
                {% component "Row" cols=2 %}
                    {% component "Col" %}Column{% endcomponent %}
                    {% component "Col" %}Column{% endcomponent %}
                    {% component "Col" %}Column{% endcomponent %}
                    {% component "Col" %}Column{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Container" %}
                {% component "Row" %}
                    {% component "Col" %}1 of 3{% endcomponent %}
                    {% component "Col" col="auto" %}Variable width content{% endcomponent %}
                    {% component "Col" %}3 of 3{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
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
