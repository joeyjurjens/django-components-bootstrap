import re

from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class NavDropdownTestCase(SimpleTestCase):
    maxDiff = None

    def assertHTMLEqual(self, actual, expected):
        super().assertHTMLEqual(normalize_html(actual), normalize_html(expected))

    def test_nav_dropdown_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" variant="tabs" as_="ul" %}
                {% component "NavItem" %}
                    {% component "NavLink" href="#" active=True %}Active{% endcomponent %}
                {% endcomponent %}
                {% component "NavDropdown" title="Dropdown" %}
                    {% component "DropdownItem" href="#" %}Action{% endcomponent %}
                    {% component "DropdownItem" href="#" %}Another action{% endcomponent %}
                    {% component "DropdownItem" href="#" %}Something else here{% endcomponent %}
                    {% component "DropdownDivider" / %}
                    {% component "DropdownItem" href="#" %}Separated link{% endcomponent %}
                {% endcomponent %}
                {% component "NavItem" %}
                    {% component "NavLink" href="#" %}Link{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        # Extract the auto-generated ID
        id_match = re.search(r'id="(nav-dropdown-[^"]+)"', rendered)
        self.assertIsNotNone(id_match)
        dropdown_id = id_match.group(1)

        expected = f"""
            <ul class="nav nav-tabs">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Active</a>
                </li>
                <li class="nav-item dropdown">
                    <button class="nav-link dropdown-toggle" type="button" id="{dropdown_id}" data-bs-toggle="dropdown" aria-expanded="false">Dropdown</button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Action</a></li>
                        <li><a class="dropdown-item" href="#">Another action</a></li>
                        <li><a class="dropdown-item" href="#">Something else here</a></li>
                        <li><hr class="dropdown-divider"></li>
                        <li><a class="dropdown-item" href="#">Separated link</a></li>
                    </ul>
                </li>
                <li class="nav-item">
                    <a class="nav-link" href="#">Link</a>
                </li>
            </ul>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_nav_dropdown_disabled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" as_="ul" %}
                {% component "NavDropdown" title="Disabled Dropdown" disabled=True %}
                    {% component "DropdownItem" href="#" %}Action{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        # Extract the auto-generated ID
        id_match = re.search(r'id="(nav-dropdown-[^"]+)"', rendered)
        self.assertIsNotNone(id_match)
        dropdown_id = id_match.group(1)

        expected = f"""
            <ul class="nav">
                <li class="nav-item dropdown">
                    <button class="nav-link dropdown-toggle disabled" type="button" id="{dropdown_id}" data-bs-toggle="dropdown" aria-expanded="false" disabled>Disabled Dropdown</button>
                    <ul class="dropdown-menu">
                        <li><a class="dropdown-item" href="#">Action</a></li>
                    </ul>
                </li>
            </ul>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_nav_dropdown_dark(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" as_="ul" %}
                {% component "NavDropdown" title="Dark Dropdown" dark=True %}
                    {% component "DropdownItem" href="#" %}Action{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        # Extract the auto-generated ID
        id_match = re.search(r'id="(nav-dropdown-[^"]+)"', rendered)
        self.assertIsNotNone(id_match)
        dropdown_id = id_match.group(1)

        expected = f"""
            <ul class="nav">
                <li class="nav-item dropdown">
                    <button class="nav-link dropdown-toggle" type="button" id="{dropdown_id}" data-bs-toggle="dropdown" aria-expanded="false">Dark Dropdown</button>
                    <ul class="dropdown-menu dropdown-menu-dark">
                        <li><a class="dropdown-item" href="#">Action</a></li>
                    </ul>
                </li>
            </ul>
        """

        self.assertHTMLEqual(rendered, expected)
