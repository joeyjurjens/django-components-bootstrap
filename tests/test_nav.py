from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TestNav(SimpleTestCase):
    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" %}
              {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="tabs" as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="pills" as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="underline" as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" vertical=True as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" vertical=True %}
              {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="pills" fill=True as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Much longer nav link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="pills" fill=True %}
              {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Much longer nav link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="pills" justified=True as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Much longer nav link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="pills" justified=True %}
              {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Much longer nav link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
              {% bootstrap5 "NavLink" disabled=True %}Disabled{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" variant="pills" as_="ul" %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" as_="button" active=True %}Active{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" as_="button" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" as_="button" %}Link{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "NavItem" %}
                {% bootstrap5 "NavLink" as_="button" disabled=True %}Disabled{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" attrs:class="custom-nav" %}
              {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Nav" role="tablist" %}
              {% bootstrap5 "NavLink" active=True href="#" %}Active{% endbootstrap5 %}
              {% bootstrap5 "NavLink" href="#" %}Link{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <nav class="nav" role="tablist">
              <a class="nav-link active" aria-current="page" href="#">Active</a>
              <a class="nav-link" href="#">Link</a>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
