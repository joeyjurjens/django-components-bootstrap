from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class PlaceholderTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            <p class="card-text placeholder-glow">
                {% bootstrap5 "Placeholder" xs=7 / %}
                {% bootstrap5 "Placeholder" xs=4 / %}
                {% bootstrap5 "Placeholder" xs=4 / %}
                {% bootstrap5 "Placeholder" xs=6 / %}
                {% bootstrap5 "Placeholder" xs=8 / %}
            </p>
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <p class="card-text placeholder-glow">
                <span class="placeholder col-7"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-4"></span>
                <span class="placeholder col-6"></span>
                <span class="placeholder col-8"></span>
            </p>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_width_variants(self):
        template = Template("""
            {% load bootstrap5 %}
            <div>
                {% bootstrap5 "Placeholder" xs=6 / %}
                {% bootstrap5 "Placeholder" xs=12 / %}
                {% bootstrap5 "Placeholder" xs=3 / %}
            </div>
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div>
                <span class="placeholder col-6"></span>
                <span class="placeholder col-12"></span>
                <span class="placeholder col-3"></span>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_size_large(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 size="lg" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 placeholder-lg"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_size_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 size="sm" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 placeholder-sm"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_size_extra_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 size="xs" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 placeholder-xs"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="primary" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-primary"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="secondary" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-secondary"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="success" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-success"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="danger" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-danger"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="warning" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-warning"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="info" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-info"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="light" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-light"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_bg_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 bg="dark" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 bg-dark"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_animation_glow(self):
        template = Template("""
            {% load bootstrap5 %}
            <p class="placeholder-glow">
                {% bootstrap5 "Placeholder" xs=12 / %}
            </p>
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <p class="placeholder-glow">
                <span class="placeholder col-12"></span>
            </p>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_animation_wave(self):
        template = Template("""
            {% load bootstrap5 %}
            <p class="placeholder-wave">
                {% bootstrap5 "Placeholder" xs=12 / %}
            </p>
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <p class="placeholder-wave">
                <span class="placeholder col-12"></span>
            </p>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_with_animation_prop(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 animation="glow" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 placeholder-glow"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_with_wave_animation(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 animation="wave" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 placeholder-wave"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_button_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "PlaceholderButton" variant="primary" xs=6 / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button class="btn btn-primary placeholder col-6" disabled aria-hidden="true"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_button_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "PlaceholderButton" variant="secondary" xs=4 / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button class="btn btn-secondary placeholder col-4" disabled aria-hidden="true"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_button_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "PlaceholderButton" variant="success" xs=6 / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button class="btn btn-success placeholder col-6" disabled aria-hidden="true"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_button_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "PlaceholderButton" variant="danger" xs=6 / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <button class="btn btn-danger placeholder col-6" disabled aria-hidden="true"></button>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_custom_element(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" as_="div" xs=12 / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="placeholder col-12"></div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_combined_size_and_color(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=12 size="lg" bg="primary" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-12 placeholder-lg bg-primary"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_placeholder_combined_all_props(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Placeholder" xs=8 size="sm" bg="success" animation="wave" / %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <span class="placeholder col-8 placeholder-sm bg-success placeholder-wave"></span>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
