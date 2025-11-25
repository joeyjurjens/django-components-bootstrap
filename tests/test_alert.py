from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class AlertTests(SimpleTestCase):
    maxDiff = None

    # All 8 Color Variants
    def test_variant_primary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="primary" %}
                A simple primary alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-primary" role="alert">
              A simple primary alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_secondary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="secondary" %}
                A simple secondary alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-secondary" role="alert">
              A simple secondary alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="success" %}
                A simple success alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-success" role="alert">
              A simple success alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="danger" %}
                A simple danger alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-danger" role="alert">
              A simple danger alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_warning(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="warning" %}
                A simple warning alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-warning" role="alert">
              A simple warning alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_info(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="info" %}
                A simple info alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-info" role="alert">
              A simple info alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_light(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="light" %}
                A simple light alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-light" role="alert">
              A simple light alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_variant_dark(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="dark" %}
                A simple dark alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-dark" role="alert">
              A simple dark alert—check it out!
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # With Links
    def test_link_color_primary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="primary" %}
                A simple primary alert with {% component "AlertLink" href="#" %}an example link{% endcomponent %}. Give it a click if you like.
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-primary" role="alert">
              A simple primary alert with <a href="#" class="alert-link">an example link</a>. Give it a click if you like.
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_link_color_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="success" %}
                A simple success alert with {% component "AlertLink" href="#" %}an example link{% endcomponent %}.
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-success" role="alert">
              A simple success alert with <a href="#" class="alert-link">an example link</a>.
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_link_color_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="danger" %}
                A simple danger alert with {% component "AlertLink" href="#" %}an example link{% endcomponent %}.
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-danger" role="alert">
              A simple danger alert with <a href="#" class="alert-link">an example link</a>.
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    # With Additional Content
    def test_additional_content(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="success" %}
                {% component "AlertHeading" %}Well done!{% endcomponent %}
                <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
                <hr>
                <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-success" role="alert">
              <h4 class="alert-heading">Well done!</h4>
              <p>Aww yeah, you successfully read this important alert message. This example text is going to run a bit longer so that you can see how spacing within an alert works with this kind of content.</p>
              <hr>
              <p class="mb-0">Whenever you need to, be sure to use margin utilities to keep things nice and tidy.</p>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_with_icon(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="primary" attrs:class="d-flex align-items-center" %}
                <svg class="bi flex-shrink-0 me-2" width="24" height="24" role="img" aria-label="Info:"><use xlink:href="#info-fill"/></svg>
                <div>
                    An example alert with an icon
                </div>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        self.assertIn("alert-primary", rendered)
        self.assertIn("d-flex", rendered)
        self.assertIn("align-items-center", rendered)
        self.assertIn("An example alert with an icon", rendered)

    # Dismissible Variants - All Colors
    def test_dismissible_primary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="primary" dismissible=True %}
                A simple primary dismissible alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-primary alert-dismissible fade show" role="alert">
              A simple primary dismissible alert—check it out!
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_dismissible_secondary(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="secondary" dismissible=True %}
                A simple secondary dismissible alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-secondary alert-dismissible fade show" role="alert">
              A simple secondary dismissible alert—check it out!
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_dismissible_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="success" dismissible=True %}
                A simple success dismissible alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-success alert-dismissible fade show" role="alert">
              A simple success dismissible alert—check it out!
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_dismissible_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="danger" dismissible=True %}
                A simple danger dismissible alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-danger alert-dismissible fade show" role="alert">
              A simple danger dismissible alert—check it out!
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_dismissible_warning(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="warning" dismissible=True %}
                <strong>Holy guacamole!</strong> You should check in on some of those fields below.
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-warning alert-dismissible fade show" role="alert">
              <strong>Holy guacamole!</strong> You should check in on some of those fields below.
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_dismissible_info(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="info" dismissible=True %}
                A simple info dismissible alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-info alert-dismissible fade show" role="alert">
              A simple info dismissible alert—check it out!
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_dismissible_light(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="light" dismissible=True %}
                A simple light dismissible alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-light alert-dismissible fade show" role="alert">
              A simple light dismissible alert—check it out!
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_dismissible_dark(self):
        template = Template("""
            {% load component_tags %}
            {% component "Alert" variant="dark" dismissible=True %}
                A simple dark dismissible alert—check it out!
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="alert alert-dark alert-dismissible fade show" role="alert">
              A simple dark dismissible alert—check it out!
              <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
