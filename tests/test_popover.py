from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class PopoverTestCase(SimpleTestCase):
    maxDiff = None

    def assertHTMLEqual(self, actual, expected):
        super().assertHTMLEqual(normalize_html(actual), normalize_html(expected))

    def test_popover_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Popover title" content="And here's some amazing content. It's very engaging. Right?" placement="top" %}
                {% bootstrap5 "Button" variant="danger" size="lg" %}Click to toggle popover{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Popover title" data-bs-content="And here's some amazing content. It's very engaging. Right?" data-bs-placement="top" data-bs-trigger="click">
                <button class="btn btn-lg btn-danger" type="button">Click to toggle popover</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_popover_placement_top(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Top popover" content="Popover content on top" placement="top" %}
                {% bootstrap5 "Button" variant="secondary" attrs:data-bs-container="body" %}Popover on top{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Top popover" data-bs-content="Popover content on top" data-bs-placement="top" data-bs-trigger="click">
                <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on top</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_popover_placement_right(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Right popover" content="Popover content on right" placement="right" %}
                {% bootstrap5 "Button" variant="secondary" attrs:data-bs-container="body" %}Popover on right{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Right popover" data-bs-content="Popover content on right" data-bs-placement="right" data-bs-trigger="click">
                <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on right</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_popover_placement_bottom(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Bottom popover" content="Popover content on bottom" placement="bottom" %}
                {% bootstrap5 "Button" variant="secondary" attrs:data-bs-container="body" %}Popover on bottom{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Bottom popover" data-bs-content="Popover content on bottom" data-bs-placement="bottom" data-bs-trigger="click">
                <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on bottom</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_popover_placement_left(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Left popover" content="Popover content on left" placement="left" %}
                {% bootstrap5 "Button" variant="secondary" attrs:data-bs-container="body" %}Popover on left{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Left popover" data-bs-content="Popover content on left" data-bs-placement="left" data-bs-trigger="click">
                <button class="btn btn-secondary" type="button" data-bs-container="body">Popover on left</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_popover_custom_styled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Custom popover" content="This popover is themed via CSS variables." placement="right" attrs:data-bs-custom-class="custom-popover" %}
                {% bootstrap5 "Button" variant="secondary" %}Custom popover{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Custom popover" data-bs-content="This popover is themed via CSS variables." data-bs-placement="right" data-bs-trigger="click" data-bs-custom-class="custom-popover">
                <button class="btn btn-secondary" type="button">Custom popover</button>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_popover_dismissible(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Dismissible popover" content="And here's some amazing content. It's very engaging. Right?" placement="top" trigger="focus" %}
                <a tabindex="0" class="btn btn-lg btn-danger" role="button">Dismissible popover</a>
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Dismissible popover" data-bs-content="And here's some amazing content. It's very engaging. Right?" data-bs-placement="top" data-bs-trigger="focus">
                <a tabindex="0" class="btn btn-lg btn-danger" role="button">Dismissible popover</a>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_popover_disabled_button_wrapper(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Popover" title="Disabled popover" content="Popover on disabled button" placement="top" trigger="hover" %}
                <span class="d-inline-block" tabindex="0">
                    {% bootstrap5 "Button" variant="primary" type="button" disabled=True %}Disabled button{% endbootstrap5 %}
                </span>
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <span data-bs-toggle="popover" data-bs-title="Disabled popover" data-bs-content="Popover on disabled button" data-bs-placement="top" data-bs-trigger="hover">
                <span class="d-inline-block" tabindex="0">
                    <button class="btn btn-primary" type="button" disabled>Disabled button</button>
                </span>
            </span>
        """

        self.assertHTMLEqual(rendered, expected)
