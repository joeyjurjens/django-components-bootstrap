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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Brand{% endbootstrap5 %}
                {% bootstrap5 "NavbarToggler" / %}
                {% bootstrap5 "NavbarCollapse" %}
                    {% bootstrap5 "NavbarNav" %}
                        {% bootstrap5 "NavItem" %}
                            {% bootstrap5 "NavLink" href="#" active=True %}Home{% endbootstrap5 %}
                        {% endbootstrap5 %}
                        {% bootstrap5 "NavItem" %}
                            {% bootstrap5 "NavLink" href="#" %}Features{% endbootstrap5 %}
                        {% endbootstrap5 %}
                        {% bootstrap5 "NavItem" %}
                            {% bootstrap5 "NavLink" href="#" %}Pricing{% endbootstrap5 %}
                        {% endbootstrap5 %}
                        {% bootstrap5 "NavItem" %}
                            {% bootstrap5 "NavLink" href="#" disabled=True %}Disabled{% endbootstrap5 %}
                        {% endbootstrap5 %}
                    {% endbootstrap5 %}
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="sm" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Brand{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="md" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Brand{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="xl" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Brand{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="xxl" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Brand{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
                <form class="d-flex" role="search">
                    <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-outline-success" type="submit">Search</button>
                </form>
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("d-flex", rendered)
        self.assertIn("form-control", rendered)
        self.assertIn("Search", rendered)

    def test_navbar_light_background(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" attrs:class="bg-light" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" attrs:class="bg-primary" attrs:data-bs-theme="dark" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("bg-primary", rendered)
        self.assertIn('data-bs-theme="dark"', rendered)

    def test_navbar_container_sm(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="sm" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-sm", rendered)

    def test_navbar_container_md(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="md" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-md", rendered)

    def test_navbar_container_lg(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="lg" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-lg", rendered)

    def test_navbar_container_xl(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="xl" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-xl", rendered)

    def test_navbar_container_xxl(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" container="xxl" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        self.assertIn("container-xxl", rendered)

    def test_navbar_disabled_brand(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Disabled Brand{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}
                    <img src="/docs/5.3/assets/brand/bootstrap-logo.svg" alt="Bootstrap" width="30" height="24" class="d-inline-block align-text-top">
                    Bootstrap
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" attrs:class="bg-body-tertiary" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar w/ text{% endbootstrap5 %}
                {% bootstrap5 "NavbarText" %}
                    Navbar text with an inline element
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" attrs:class="navbar-dark bg-dark" variant="dark" %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Navbar" expand="lg" attrs:class="bg-body-tertiary" container=False %}
                {% bootstrap5 "NavbarBrand" href="#" %}Navbar{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <nav class="navbar navbar-expand-lg bg-body-tertiary">
                <a class="navbar-brand" href="#">Navbar</a>
            </nav>
        """

        self.assertHTMLEqual(rendered, expected)
