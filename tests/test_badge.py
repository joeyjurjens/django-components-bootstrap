from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class BadgeTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            <h1>Example heading {% bootstrap5 "Badge" bg="secondary" %}New{% endbootstrap5 %}</h1>
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <h1>Example heading <span class="badge text-bg-secondary">New</span></h1>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_in_button(self):
        template = Template("""
            {% load bootstrap5 %}
            <button type="button" class="btn btn-primary">
              Notifications {% bootstrap5 "Badge" bg="secondary" %}4{% endbootstrap5 %}
            </button>
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button type="button" class="btn btn-primary">
              Notifications <span class="badge text-bg-secondary">4</span>
            </button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="primary" pill=True %}Primary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-primary">Primary</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="primary" %}Primary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-primary">Primary</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="secondary" %}Secondary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-secondary">Secondary</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="success" %}Success{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-success">Success</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="danger" %}Danger{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-danger">Danger</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="warning" %}Warning{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-warning">Warning</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="info" %}Info{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-info">Info</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="light" %}Light{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-light">Light</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_bg_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="dark" %}Dark{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge text-bg-dark">Dark</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="primary" pill=True %}Primary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-primary">Primary</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="secondary" pill=True %}Secondary{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-secondary">Secondary</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="success" pill=True %}Success{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-success">Success</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="danger" pill=True %}Danger{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-danger">Danger</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="warning" pill=True %}Warning{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-warning">Warning</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="info" pill=True %}Info{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-info">Info</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="light" pill=True %}Light{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-light">Light</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_pill_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Badge" bg="dark" pill=True %}Dark{% endbootstrap5 %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="badge rounded-pill text-bg-dark">Dark</span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
