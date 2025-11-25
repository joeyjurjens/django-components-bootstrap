from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TestDropdownButton(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Dropdown button" variant="secondary" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Something else here{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown button
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_variant_primary(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Primary" variant="primary" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Primary
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_variant_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Success" variant="success" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-success dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Success
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_variant_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Danger" variant="danger" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-danger dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Danger
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_variant_warning(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Warning" variant="warning" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-warning dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Warning
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_variant_info(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Info" variant="info" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-info dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Info
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_variant_light(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Light" variant="light" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-light dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Light
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_variant_dark(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Dark" variant="dark" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-dark dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dark
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_size_large(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Large button" variant="secondary" size="lg" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle btn-lg" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Large button
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_size_small(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Small button" variant="secondary" size="sm" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle btn-sm" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Small button
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_dark_menu(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Dropdown" variant="secondary" dark=True %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </button>
              <ul class="dropdown-menu dropdown-menu-dark">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_menu_alignment_end(self):
        template = Template("""
            {% load component_tags %}
            {% component "DropdownButton" title="Dropdown" variant="secondary" align="end" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown
              </button>
              <ul class="dropdown-menu dropdown-menu-end">
                <li><a class="dropdown-item" href="#">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))


class TestSplitButton(SimpleTestCase):
    maxDiff = None

    def test_basic_split_button(self):
        template = Template("""
            {% load component_tags %}
            {% component "SplitButton" title="Primary" variant="primary" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Something else here{% endcomponent %}
              {% component "DropdownDivider" / %}
              {% component "DropdownItem" href="#" %}Separated link{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <div class="btn-group" role="group">
                <button class="btn btn-primary" type="button">
                  Primary
                </button>
                <button class="btn btn-primary dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Toggle dropdown</span>
                </button>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><a class="dropdown-item" href="#">Something else here</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Separated link</a></li>
                </ul>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_split_button_danger(self):
        template = Template("""
            {% load component_tags %}
            {% component "SplitButton" title="Danger" variant="danger" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
              {% component "DropdownDivider" / %}
              {% component "DropdownItem" href="#" %}Separated link{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <div class="btn-group" role="group">
                <button class="btn btn-danger" type="button">
                  Danger
                </button>
                <button class="btn btn-danger dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Toggle dropdown</span>
                </button>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                  <li><hr class="dropdown-divider"></li>
                  <li><a class="dropdown-item" href="#">Separated link</a></li>
                </ul>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_split_button_success(self):
        template = Template("""
            {% load component_tags %}
            {% component "SplitButton" title="Success" variant="success" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <div class="btn-group" role="group">
                <button class="btn btn-success" type="button">
                  Success
                </button>
                <button class="btn btn-success dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Toggle dropdown</span>
                </button>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                </ul>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_split_button_large(self):
        template = Template("""
            {% load component_tags %}
            {% component "SplitButton" title="Large button" variant="primary" size="lg" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <div class="btn-group" role="group">
                <button class="btn btn-primary btn-lg" type="button">
                  Large button
                </button>
                <button class="btn btn-primary dropdown-toggle dropdown-toggle-split btn-lg" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Toggle dropdown</span>
                </button>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                </ul>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_split_button_small(self):
        template = Template("""
            {% load component_tags %}
            {% component "SplitButton" title="Small button" variant="secondary" size="sm" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <div class="btn-group" role="group">
                <button class="btn btn-secondary btn-sm" type="button">
                  Small button
                </button>
                <button class="btn btn-secondary dropdown-toggle dropdown-toggle-split btn-sm" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Toggle dropdown</span>
                </button>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                </ul>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_split_button_custom_toggle_label(self):
        template = Template("""
            {% load component_tags %}
            {% component "SplitButton" title="Action" variant="primary" toggle_label="Custom toggle" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <div class="btn-group" role="group">
                <button class="btn btn-primary" type="button">
                  Action
                </button>
                <button class="btn btn-primary dropdown-toggle dropdown-toggle-split" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Custom toggle</span>
                </button>
                <ul class="dropdown-menu">
                  <li><a class="dropdown-item" href="#">Action</a></li>
                  <li><a class="dropdown-item" href="#">Another action</a></li>
                </ul>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
