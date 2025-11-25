from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TestButtonGroup(SimpleTestCase):
    def test_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonGroup" %}
              {% component "Button" variant="primary" %}Left{% endcomponent %}
              {% component "Button" variant="primary" %}Middle{% endcomponent %}
              {% component "Button" variant="primary" %}Right{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="btn-group" role="group">
              <button type="button" class="btn btn-primary">Left</button>
              <button type="button" class="btn btn-primary">Middle</button>
              <button type="button" class="btn btn-primary">Right</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_mixed_styles(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonGroup" %}
              {% component "Button" variant="danger" %}Danger{% endcomponent %}
              {% component "Button" variant="warning" %}Warning{% endcomponent %}
              {% component "Button" variant="success" %}Success{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="btn-group" role="group">
              <button type="button" class="btn btn-danger">Danger</button>
              <button type="button" class="btn btn-warning">Warning</button>
              <button type="button" class="btn btn-success">Success</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_checkbox_buttons(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonGroup" %}
              <input type="checkbox" class="btn-check" id="btncheck1" autocomplete="off">
              <label class="btn btn-outline-primary" for="btncheck1">Checkbox 1</label>

              <input type="checkbox" class="btn-check" id="btncheck2" autocomplete="off">
              <label class="btn btn-outline-primary" for="btncheck2">Checkbox 2</label>

              <input type="checkbox" class="btn-check" id="btncheck3" autocomplete="off">
              <label class="btn btn-outline-primary" for="btncheck3">Checkbox 3</label>
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        self.assertIn("btn-check", rendered)
        self.assertIn("Checkbox 1", rendered)
        self.assertIn("Checkbox 2", rendered)
        self.assertIn("Checkbox 3", rendered)

    def test_radio_buttons(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonGroup" %}
              <input type="radio" class="btn-check" name="btnradio" id="btnradio1" autocomplete="off" checked>
              <label class="btn btn-outline-primary" for="btnradio1">Radio 1</label>

              <input type="radio" class="btn-check" name="btnradio" id="btnradio2" autocomplete="off">
              <label class="btn btn-outline-primary" for="btnradio2">Radio 2</label>

              <input type="radio" class="btn-check" name="btnradio" id="btnradio3" autocomplete="off">
              <label class="btn btn-outline-primary" for="btnradio3">Radio 3</label>
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        self.assertIn("btn-check", rendered)
        self.assertIn("Radio 1", rendered)
        self.assertIn("Radio 2", rendered)
        self.assertIn("Radio 3", rendered)

    def test_large(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonGroup" size="lg" %}
              {% component "Button" variant="primary" outline=True %}Left{% endcomponent %}
              {% component "Button" variant="primary" outline=True %}Middle{% endcomponent %}
              {% component "Button" variant="primary" outline=True %}Right{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="btn-group btn-group-lg" role="group">
              <button type="button" class="btn btn-outline-primary">Left</button>
              <button type="button" class="btn btn-outline-primary">Middle</button>
              <button type="button" class="btn btn-outline-primary">Right</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_small(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonGroup" size="sm" %}
              {% component "Button" variant="primary" outline=True %}Left{% endcomponent %}
              {% component "Button" variant="primary" outline=True %}Middle{% endcomponent %}
              {% component "Button" variant="primary" outline=True %}Right{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="btn-group btn-group-sm" role="group">
              <button type="button" class="btn btn-outline-primary">Left</button>
              <button type="button" class="btn btn-outline-primary">Middle</button>
              <button type="button" class="btn btn-outline-primary">Right</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_vertical(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonGroup" vertical=True %}
              {% component "Button" variant="primary" %}Button{% endcomponent %}
              {% component "Button" variant="primary" %}Button{% endcomponent %}
              {% component "Button" variant="primary" %}Button{% endcomponent %}
              {% component "Button" variant="primary" %}Button{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="btn-group-vertical" role="group">
              <button type="button" class="btn btn-primary">Button</button>
              <button type="button" class="btn btn-primary">Button</button>
              <button type="button" class="btn btn-primary">Button</button>
              <button type="button" class="btn btn-primary">Button</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))


class TestButtonToolbar(SimpleTestCase):
    def test_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "ButtonToolbar" %}
              {% component "ButtonGroup" attrs:class="me-2" %}
                {% component "Button" variant="primary" %}1{% endcomponent %}
                {% component "Button" variant="primary" %}2{% endcomponent %}
                {% component "Button" variant="primary" %}3{% endcomponent %}
                {% component "Button" variant="primary" %}4{% endcomponent %}
              {% endcomponent %}
              {% component "ButtonGroup" attrs:class="me-2" %}
                {% component "Button" variant="secondary" %}5{% endcomponent %}
                {% component "Button" variant="secondary" %}6{% endcomponent %}
                {% component "Button" variant="secondary" %}7{% endcomponent %}
              {% endcomponent %}
              {% component "ButtonGroup" %}
                {% component "Button" variant="info" %}8{% endcomponent %}
              {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="btn-toolbar" role="toolbar">
              <div class="btn-group me-2" role="group">
                <button type="button" class="btn btn-primary">1</button>
                <button type="button" class="btn btn-primary">2</button>
                <button type="button" class="btn btn-primary">3</button>
                <button type="button" class="btn btn-primary">4</button>
              </div>
              <div class="btn-group me-2" role="group">
                <button type="button" class="btn btn-secondary">5</button>
                <button type="button" class="btn btn-secondary">6</button>
                <button type="button" class="btn btn-secondary">7</button>
              </div>
              <div class="btn-group" role="group">
                <button type="button" class="btn btn-info">8</button>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
