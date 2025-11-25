import re

from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class NavbarTestCase(SimpleTestCase):
    maxDiff = None

    def assertHTMLEqual(self, actual, expected):
        super().assertHTMLEqual(normalize_html(actual), normalize_html(expected))

    def test_basic_navbar(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Brand{% endcomponent %}
                {% component "NavbarToggler" / %}
                {% component "NavbarCollapse" %}
                    {% component "NavbarNav" %}
                        {% component "NavItem" %}
                            {% component "NavLink" href="#" active=True %}Home{% endcomponent %}
                        {% endcomponent %}
                        {% component "NavItem" %}
                            {% component "NavLink" href="#" %}Features{% endcomponent %}
                        {% endcomponent %}
                        {% component "NavItem" %}
                            {% component "NavLink" href="#" %}Pricing{% endcomponent %}
                        {% endcomponent %}
                        {% component "NavItem" %}
                            {% component "NavLink" href="#" disabled=True %}Disabled{% endcomponent %}
                        {% endcomponent %}
                    {% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        collapse_id_match = re.search(r'id="(navbar-collapse-[^"]+)"', rendered)
        self.assertIsNotNone(collapse_id_match)
        collapse_id = collapse_id_match.group(1)

        expected = f"""
            <nav class="navbar navbar-expand-lg bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Brand</a>
                    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#{collapse_id}" aria-controls="{collapse_id}" aria-expanded="false" aria-label="Toggle navigation">
                        <span class="navbar-toggler-icon"></span>
                    </button>
                    <div class="collapse navbar-collapse" id="{collapse_id}">
                        <ul class="navbar-nav">
                            <li class="nav-item">
                                <a class="nav-link active" aria-current="page" href="#">Home</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Features</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link" href="#">Pricing</a>
                            </li>
                            <li class="nav-item">
                                <a class="nav-link disabled" aria-disabled="true">Disabled</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_expand_sm(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="sm" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Brand{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-expand-sm bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Brand</a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_expand_md(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="md" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Brand{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-expand-md bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Brand</a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_expand_xl(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="xl" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Brand{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-expand-xl bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Brand</a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_expand_xxl(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="xxl" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Brand{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-expand-xxl bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Brand</a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_with_form(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("d-flex", rendered)
        self.assertIn("form-control", rendered)
        self.assertIn("Search", rendered)

    def test_navbar_light_background(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" attrs:class="bg-light" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar bg-light">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar</a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_primary_background(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" attrs:class="bg-primary" attrs:data-bs-theme="dark" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("bg-primary", rendered)
        self.assertIn('data-bs-theme="dark"', rendered)

    def test_navbar_container_sm(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="sm" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-sm", rendered)

    def test_navbar_container_md(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="md" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-md", rendered)

    def test_navbar_container_lg(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="lg" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-lg", rendered)

    def test_navbar_container_xl(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="xl" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-xl", rendered)

    def test_navbar_container_xxl(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="xxl" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-xxl", rendered)

    def test_navbar_disabled_brand(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Disabled Brand{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Disabled Brand</a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_with_brand_image(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}
                    <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24" class="d-inline-block align-text-top">
                    Bootstrap
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-expand-lg bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">
                        <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24" class="d-inline-block align-text-top">
                        Bootstrap
                    </a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_with_text(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" attrs:class="bg-body-tertiary" %}
                {% component "NavbarBrand" href="#" %}Navbar w/ text{% endcomponent %}
                {% component "NavbarText" %}
                    Navbar text with an inline element
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar bg-body-tertiary">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar w/ text</a>
                    <span class="navbar-text">
                        Navbar text with an inline element
                    </span>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_dark(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" attrs:class="navbar-dark bg-dark" variant="dark" %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-dark bg-dark" data-bs-theme="dark">
                <div class="container-fluid">
                    <a class="navbar-brand" href="#">Navbar</a>
                </div>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_navbar_without_container(self):
        template = Template("""
            {% load component_tags %}
            {% component "Navbar" expand="lg" attrs:class="bg-body-tertiary" container=False %}
                {% component "NavbarBrand" href="#" %}Navbar{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-expand-lg bg-body-tertiary">
                <a class="navbar-brand" href="#">Navbar</a>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)
