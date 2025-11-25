from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class ProgressTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=25 / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar" style="width: 25.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_basic_0_percent(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=0 / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar" style="width: 0.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_basic_50_percent(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=50 / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar" style="width: 50.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_basic_75_percent(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=75 / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar" style="width: 75.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_basic_100_percent(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=100 / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar" style="width: 100.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # Heights
    def test_height_1px(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" height="1px" %}
                {% component "ProgressBar" now=25 / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress" style="height: 1px;">
              <div class="progress-bar" style="width: 25.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_height_20px(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" height="20px" %}
                {% component "ProgressBar" now=25 / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress" style="height: 20px;">
              <div class="progress-bar" style="width: 25.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # With Label
    def test_with_label(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=25 %}25%{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar" style="width: 25.0%">25%</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # Background Colors - All 8 Variants
    def test_variant_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=25 variant="success" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-success" style="width: 25.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_info(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=50 variant="info" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-info" style="width: 50.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_warning(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=75 variant="warning" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-warning" style="width: 75.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=100 variant="danger" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-danger" style="width: 100.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_primary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=30 variant="primary" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-primary" style="width: 30.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_secondary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=40 variant="secondary" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-secondary" style="width: 40.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_light(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=60 variant="light" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-light" style="width: 60.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_dark(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=80 variant="dark" / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-dark" style="width: 80.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # Variants with Labels
    def test_variant_success_with_label(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=25 variant="success" %}25%{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-success" style="width: 25.0%">25%</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_info_with_label(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=50 variant="info" %}50%{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-info" style="width: 50.0%">50%</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_warning_with_label(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=75 variant="warning" %}75%{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-warning" style="width: 75.0%">75%</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_danger_with_label(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=100 variant="danger" %}100%{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar bg-danger" style="width: 100.0%">100%</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # Multiple Bars
    def test_multiple_bars(self):
        template = Template("""
            {% load component_tags %}
            {% component "ProgressStacked" %}
                {% component "Progress" attrs:style="width: 15%" %}
                    {% component "ProgressBar" now=15 / %}
                {% endcomponent %}
                {% component "Progress" attrs:style="width: 30%" %}
                    {% component "ProgressBar" now=30 variant="success" / %}
                {% endcomponent %}
                {% component "Progress" attrs:style="width: 20%" %}
                    {% component "ProgressBar" now=20 variant="info" / %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        self.assertIn("progress-stacked", rendered)
        self.assertIn("bg-success", rendered)
        self.assertIn("bg-info", rendered)

    # Striped Bars
    def test_striped_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=10 striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped" style="width: 10.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=25 variant="success" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-success" style="width: 25.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_info(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=50 variant="info" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-info" style="width: 50.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_warning(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=75 variant="warning" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-warning" style="width: 75.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=100 variant="danger" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-danger" style="width: 100.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_primary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=40 variant="primary" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-primary" style="width: 40.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_secondary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=60 variant="secondary" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-secondary" style="width: 60.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_light(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=70 variant="light" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-light" style="width: 70.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_striped_dark(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=90 variant="dark" striped=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped bg-dark" style="width: 90.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # Animated Striped Bars
    def test_animated_striped(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=75 animated=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped progress-bar-animated" style="width: 75.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_animated_striped_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=50 variant="success" animated=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped progress-bar-animated bg-success" style="width: 50.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_animated_striped_info(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=60 variant="info" animated=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped progress-bar-animated bg-info" style="width: 60.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_animated_striped_warning(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=80 variant="warning" animated=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped progress-bar-animated bg-warning" style="width: 80.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_animated_striped_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "Progress" %}
                {% component "ProgressBar" now=90 variant="danger" animated=True / %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="progress">
              <div class="progress-bar progress-bar-striped progress-bar-animated bg-danger" style="width: 90.0%"></div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
