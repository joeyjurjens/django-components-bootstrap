from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TestDropdown(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="secondary" %}Dropdown button{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
                {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
                {% component "DropdownItem" href="#" %}Something else here{% endcomponent %}
              {% endcomponent %}
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

    # Color Variants
    def test_variant_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="primary" %}Primary{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-primary", rendered)

    def test_variant_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="success" %}Success{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-success", rendered)

    def test_variant_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="danger" %}Danger{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-danger", rendered)

    def test_variant_warning(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="warning" %}Warning{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-warning", rendered)

    def test_variant_info(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="info" %}Info{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-info", rendered)

    def test_variant_light(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="light" %}Light{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-light", rendered)

    def test_variant_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="dark" %}Dark{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn("btn-dark", rendered)

    # Sizing
    def test_size_large(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="secondary" size="lg" %}Large button{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
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
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_size_small(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="secondary" size="sm" %}Small button{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
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
              </ul>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    # Directions
    def test_dropup(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" direction="up" %}
              {% component "DropdownToggle" variant="secondary" %}Dropup{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" direction="end" %}
              {% component "DropdownToggle" variant="secondary" %}Dropend{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" direction="start" %}
              {% component "DropdownToggle" variant="secondary" %}Dropstart{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" centered=True %}
              {% component "DropdownToggle" variant="secondary" %}Centered dropdown{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" direction="up" centered=True %}
              {% component "DropdownToggle" variant="secondary" %}Centered dropup{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="secondary" %}Right-aligned menu{% endcomponent %}
              {% component "DropdownMenu" align="end" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="secondary" %}Left-aligned, lg-right{% endcomponent %}
              {% component "DropdownMenu" align_lg="end" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="secondary" %}Right-aligned, lg-left{% endcomponent %}
              {% component "DropdownMenu" align="end" align_lg="start" %}
                {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "Dropdown" auto_close="true" %}
              {% component "DropdownToggle" variant="secondary" %}Default dropdown{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Menu item{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="true"', rendered)

    def test_auto_close_false(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" auto_close="false" %}
              {% component "DropdownToggle" variant="secondary" %}Manual close{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Menu item{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="false"', rendered)

    def test_auto_close_inside(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" auto_close="inside" %}
              {% component "DropdownToggle" variant="secondary" %}Clickable inside{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Menu item{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="inside"', rendered)

    def test_auto_close_outside(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" auto_close="outside" %}
              {% component "DropdownToggle" variant="secondary" %}Clickable outside{% endcomponent %}
              {% component "DropdownMenu" %}
                {% component "DropdownItem" href="#" %}Menu item{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())
        self.assertIn('data-bs-auto-close="outside"', rendered)

    # Dark Dropdown
    def test_dark_dropdown(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
              {% component "DropdownToggle" variant="secondary" %}Dropdown button{% endcomponent %}
              {% component "DropdownMenu" dark=True %}
                {% component "DropdownItem" href="#" active=True %}Action{% endcomponent %}
                {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
                {% component "DropdownItem" href="#" %}Something else here{% endcomponent %}
                {% component "DropdownDivider" / %}
                {% component "DropdownItem" href="#" %}Separated link{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
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
            {% component "DropdownMenu" %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Something else here{% endcomponent %}
              {% component "DropdownDivider" / %}
              {% component "DropdownItem" href="#" %}Separated link{% endcomponent %}
            {% endcomponent %}
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
            {% component "DropdownMenu" %}
              {% component "DropdownHeader" %}Dropdown header{% endcomponent %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
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
            {% component "DropdownMenu" %}
              {% component "DropdownItemText" %}Dropdown item text{% endcomponent %}
              {% component "DropdownItem" href="#" %}Action{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
            {% endcomponent %}
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
            {% component "DropdownMenu" %}
              {% component "DropdownItem" href="#" %}Regular link{% endcomponent %}
              {% component "DropdownItem" href="#" active=True %}Active link{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another link{% endcomponent %}
            {% endcomponent %}
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
            {% component "DropdownMenu" %}
              {% component "DropdownItem" href="#" %}Regular link{% endcomponent %}
              {% component "DropdownItem" href="#" disabled=True %}Disabled link{% endcomponent %}
              {% component "DropdownItem" href="#" %}Another link{% endcomponent %}
            {% endcomponent %}
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
            {% component "DropdownMenu" %}
              {% component "DropdownItem" as_="button" %}Action{% endcomponent %}
              {% component "DropdownItem" as_="button" %}Another action{% endcomponent %}
              {% component "DropdownItem" as_="button" %}Something else here{% endcomponent %}
            {% endcomponent %}
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
