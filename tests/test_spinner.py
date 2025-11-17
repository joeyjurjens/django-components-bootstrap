from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class SpinnerTests(SimpleTestCase):
    maxDiff = None

    def test_border(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="primary" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-primary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="secondary" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-secondary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="success" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-success" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="danger" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-danger" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="warning" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-warning" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="info" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-info" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="light" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-light" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" variant="dark" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border text-dark" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="primary" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-primary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="secondary" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-secondary" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="success" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-success" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="danger" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-danger" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="warning" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-warning" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="info" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-info" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="light" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-light" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" variant="dark" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow text-dark" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_border_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" size="sm" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border spinner-border-sm" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_grow_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="grow" size="sm" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-grow spinner-grow-sm" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_label(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" label="Please wait..." / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border" role="status">
              <span class="visually-hidden">Please wait...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_attrs(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" attrs:class="custom-class" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border custom-class" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_with_margin(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_size_style(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Spinner" animation="border" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="spinner-border" role="status">
              <span class="visually-hidden">Loading...</span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
