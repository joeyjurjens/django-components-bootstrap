from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TestNav(SimpleTestCase):
    def test_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_basic_nav_element(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" %}
              {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <nav class="nav">
              <a class="nav-link active" aria-current="page" href="#">Active</a>
              <a class="nav-link" href="#">Link</a>
              <a class="nav-link" href="#">Link</a>
              <a class="nav-link disabled" aria-disabled="true">Disabled</a>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_tabs(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="tabs" as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav nav-tabs">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_pills(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="pills" as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav nav-pills">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_underline(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="underline" as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav nav-underline">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_vertical(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" vertical=True as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav flex-column">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_vertical_nav_element(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" vertical=True %}
              {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <nav class="nav flex-column">
              <a class="nav-link active" aria-current="page" href="#">Active</a>
              <a class="nav-link" href="#">Link</a>
              <a class="nav-link" href="#">Link</a>
              <a class="nav-link disabled" aria-disabled="true">Disabled</a>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_fill(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="pills" fill=True as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Much longer nav link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav nav-pills nav-fill">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Much longer nav link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_fill_nav_element(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="pills" fill=True %}
              {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% component "NavLink" href="#" %}Much longer nav link{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <nav class="nav nav-pills nav-fill">
              <a class="nav-link active" aria-current="page" href="#">Active</a>
              <a class="nav-link" href="#">Much longer nav link</a>
              <a class="nav-link" href="#">Link</a>
              <a class="nav-link disabled" aria-disabled="true">Disabled</a>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_justified(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="pills" justified=True as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Much longer nav link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav nav-pills nav-justified">
              <li class="nav-item">
                <a class="nav-link active" aria-current="page" href="#">Active</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Much longer nav link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="#">Link</a>
              </li>
              <li class="nav-item">
                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_justified_nav_element(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="pills" justified=True %}
              {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% component "NavLink" href="#" %}Much longer nav link{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
              {% component "NavLink" disabled=True %}Disabled{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <nav class="nav nav-pills nav-justified">
              <a class="nav-link active" aria-current="page" href="#">Active</a>
              <a class="nav-link" href="#">Much longer nav link</a>
              <a class="nav-link" href="#">Link</a>
              <a class="nav-link disabled" aria-disabled="true">Disabled</a>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_button_links(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" variant="pills" as_="ul" %}
              {% component "NavItem" %}
                {% component "NavLink" as_="button" active=True %}Active{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" as_="button" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" as_="button" %}Link{% endcomponent %}
              {% endcomponent %}
              {% component "NavItem" %}
                {% component "NavLink" as_="button" disabled=True %}Disabled{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <ul class="nav nav-pills">
              <li class="nav-item">
                <button type="button" class="nav-link active">Active</button>
              </li>
              <li class="nav-item">
                <button type="button" class="nav-link">Link</button>
              </li>
              <li class="nav-item">
                <button type="button" class="nav-link">Link</button>
              </li>
              <li class="nav-item">
                <button type="button" class="nav-link disabled" disabled>Disabled</button>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_custom_attrs(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" attrs:class="custom-nav" %}
              {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <nav class="nav custom-nav">
              <a class="nav-link active" aria-current="page" href="#">Active</a>
              <a class="nav-link" href="#">Link</a>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_custom_role(self):
        template = Template("""
            {% load component_tags %}
            {% component "Nav" role="tablist" %}
              {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
              {% component "NavLink" href="#" %}Link{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <nav class="nav" role="tablist">
              <a class="nav-link active" aria-current="page" href="#">Active</a>
              <a class="nav-link" href="#">Link</a>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
