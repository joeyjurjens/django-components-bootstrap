from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TestDropdown(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Dropdown button{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
                {% bootstrap5 "DropdownItem" href="#" %}Another action{% endbootstrap5 %}
                {% bootstrap5 "DropdownItem" href="#" %}Something else here{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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

    # Color Variants
    def test_variant_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="primary" %}Primary{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-primary", rendered)

    def test_variant_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="success" %}Success{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-success", rendered)

    def test_variant_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="danger" %}Danger{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-danger", rendered)

    def test_variant_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="warning" %}Warning{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-warning", rendered)

    def test_variant_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="info" %}Info{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-info", rendered)

    def test_variant_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="light" %}Light{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-light", rendered)

    def test_variant_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="dark" %}Dark{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-dark", rendered)

    # Sizing
    def test_size_large(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" size="lg" %}Large button{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle btn-lg" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Large button
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_size_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" size="sm" %}Small button{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle btn-sm" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Small button
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    # Directions
    def test_dropup(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" direction="up" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Dropup{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropup">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropup
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_dropend(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" direction="end" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Dropend{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropend">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropend
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_dropstart(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" direction="start" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Dropstart{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropstart">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropstart
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_centered(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" centered=True %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Centered dropdown{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown dropdown-center">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Centered dropdown
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_centered_dropup(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" direction="up" centered=True %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Centered dropup{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropup dropup-center">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Centered dropup
              </button>
              <ul class="dropdown-menu">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    # Menu Alignment
    def test_menu_align_end(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Right-aligned menu{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" align="end" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Right-aligned menu
              </button>
              <ul class="dropdown-menu dropdown-menu-end">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_menu_responsive_align_lg_end(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Left-aligned, lg-right{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" align_lg="end" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Left-aligned, lg-right
              </button>
              <ul class="dropdown-menu dropdown-menu-lg-end">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_menu_responsive_align_end_lg_start(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Right-aligned, lg-left{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" align="end" align_lg="start" %}
                {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Right-aligned, lg-left
              </button>
              <ul class="dropdown-menu dropdown-menu-end dropdown-menu-lg-start">
                <li><a class="dropdown-item" href="#">Action</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    # Auto Close Behaviors
    def test_auto_close_true(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" auto_close="true" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Default dropdown{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Menu item{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="true"', rendered)

    def test_auto_close_false(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" auto_close="false" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Manual close{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Menu item{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="false"', rendered)

    def test_auto_close_inside(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" auto_close="inside" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Clickable inside{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Menu item{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="inside"', rendered)

    def test_auto_close_outside(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" auto_close="outside" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Clickable outside{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" %}
                {% bootstrap5 "DropdownItem" href="#" %}Menu item{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="outside"', rendered)

    # Dark Dropdown
    def test_dark_dropdown(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Dropdown" %}
              {% bootstrap5 "DropdownToggle" variant="secondary" %}Dropdown button{% endbootstrap5 %}
              {% bootstrap5 "DropdownMenu" dark=True %}
                {% bootstrap5 "DropdownItem" href="#" active=True %}Action{% endbootstrap5 %}
                {% bootstrap5 "DropdownItem" href="#" %}Another action{% endbootstrap5 %}
                {% bootstrap5 "DropdownItem" href="#" %}Something else here{% endbootstrap5 %}
                {% bootstrap5 "DropdownDivider" / %}
                {% bootstrap5 "DropdownItem" href="#" %}Separated link{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="dropdown">
              <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                Dropdown button
              </button>
              <ul class="dropdown-menu dropdown-menu-dark">
                <li><a class="dropdown-item active" href="#" aria-current="true">Action</a></li>
                <li><a class="dropdown-item" href="#">Another action</a></li>
                <li><a class="dropdown-item" href="#">Something else here</a></li>
                <li><hr class="dropdown-divider"></li>
                <li><a class="dropdown-item" href="#">Separated link</a></li>
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    # Menu Headers and Dividers
    def test_with_divider(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "DropdownMenu" %}
              {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Another action{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Something else here{% endbootstrap5 %}
              {% bootstrap5 "DropdownDivider" / %}
              {% bootstrap5 "DropdownItem" href="#" %}Separated link{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
              <li><a class="dropdown-item" href="#">Something else here</a></li>
              <li><hr class="dropdown-divider"></li>
              <li><a class="dropdown-item" href="#">Separated link</a></li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_with_header(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "DropdownMenu" %}
              {% bootstrap5 "DropdownHeader" %}Dropdown header{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Another action{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="dropdown-menu">
              <li><h6 class="dropdown-header">Dropdown header</h6></li>
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_with_text(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "DropdownMenu" %}
              {% bootstrap5 "DropdownItemText" %}Dropdown item text{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Action{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Another action{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="dropdown-menu">
              <li><span class="dropdown-item-text">Dropdown item text</span></li>
              <li><a class="dropdown-item" href="#">Action</a></li>
              <li><a class="dropdown-item" href="#">Another action</a></li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    # Active and Disabled Items
    def test_active_item(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "DropdownMenu" %}
              {% bootstrap5 "DropdownItem" href="#" %}Regular link{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" active=True %}Active link{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Another link{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Regular link</a></li>
              <li><a class="dropdown-item active" href="#" aria-current="true">Active link</a></li>
              <li><a class="dropdown-item" href="#">Another link</a></li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_disabled_item(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "DropdownMenu" %}
              {% bootstrap5 "DropdownItem" href="#" %}Regular link{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" disabled=True %}Disabled link{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" href="#" %}Another link{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="dropdown-menu">
              <li><a class="dropdown-item" href="#">Regular link</a></li>
              <li><a class="dropdown-item disabled" href="#" aria-disabled="true" tabindex="-1">Disabled link</a></li>
              <li><a class="dropdown-item" href="#">Another link</a></li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_button_items(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "DropdownMenu" %}
              {% bootstrap5 "DropdownItem" as_="button" %}Action{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" as_="button" %}Another action{% endbootstrap5 %}
              {% bootstrap5 "DropdownItem" as_="button" %}Something else here{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="dropdown-menu">
              <li><button class="dropdown-item" type="button">Action</button></li>
              <li><button class="dropdown-item" type="button">Another action</button></li>
              <li><button class="dropdown-item" type="button">Something else here</button></li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
