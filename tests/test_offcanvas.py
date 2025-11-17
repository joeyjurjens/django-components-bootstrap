from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class TestOffcanvas(SimpleTestCase):
    maxDiff = None

    @djc_test
    def test_basic(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" scroll=False keyboard=False %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs={"class": "btn btn-primary", "type": "button"} %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Offcanvas{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  Content for the offcanvas goes here. You can place just about any Bootstrap component or custom elements here.
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button type="button" class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-keyboard="false">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                Content for the offcanvas goes here. You can place just about any Bootstrap component or custom elements here.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_placement_start(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" placement="start" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Offcanvas Start{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This offcanvas appears from the start (left).</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas Start</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This offcanvas appears from the start (left).</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_placement_end(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" placement="end" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Offcanvas End{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This offcanvas appears from the end (right).</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-end" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas End</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This offcanvas appears from the end (right).</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_placement_top(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" placement="top" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Offcanvas Top{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This offcanvas appears from the top.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-top" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas Top</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This offcanvas appears from the top.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_placement_bottom(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" placement="bottom" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Offcanvas Bottom{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This offcanvas appears from the bottom.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-bottom" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas Bottom</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This offcanvas appears from the bottom.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_body_scrolling_enabled(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" scroll=True backdrop="false" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Offcanvas with body scrolling{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>Try scrolling the rest of the page to see this option in action.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-backdrop="false" data-bs-scroll="true">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Offcanvas with body scrolling</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>Try scrolling the rest of the page to see this option in action.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_with_backdrop(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" scroll=True %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Backdrop with scrolling{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>Try scrolling the rest of the page to see this option in action.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-scroll="true">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Backdrop with scrolling</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>Try scrolling the rest of the page to see this option in action.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_static_backdrop(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" backdrop="static" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Static Backdrop{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>I will not close if you click outside of me.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-backdrop="static">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Static Backdrop</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>I will not close if you click outside of me.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_no_backdrop(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" backdrop="false" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}No Backdrop{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This offcanvas has no backdrop.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label" data-bs-backdrop="false">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">No Backdrop</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This offcanvas has no backdrop.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_responsive_lg(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" responsive="lg" placement="end" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Responsive offcanvas{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This is content within an offcanvas-lg.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas-lg offcanvas-end" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Responsive offcanvas</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This is content within an offcanvas-lg.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_responsive_md(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" responsive="md" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" %}Responsive MD offcanvas{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This is content within an offcanvas-md.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas-md offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">Responsive MD offcanvas</h5>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This is content within an offcanvas-md.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_without_close_button(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" close_button=False %}
                  {% bootstrap5 "OffcanvasTitle" %}No Close Button{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This offcanvas header has no close button.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h5 class="offcanvas-title" id="offcanvas-ctest01-label">No Close Button</h5>
              </div>
              <div class="offcanvas-body">
                <p>This offcanvas header has no close button.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_offcanvas_custom_title_heading(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags bootstrap5 %}
            {% bootstrap5 "Offcanvas" %}
              {% fill "toggle" %}
                {% bootstrap5 "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endbootstrap5 %}
              {% endfill %}
              {% fill "default" %}
                {% bootstrap5 "OffcanvasHeader" %}
                  {% bootstrap5 "OffcanvasTitle" as_="h3" %}Custom Heading{% endbootstrap5 %}
                {% endbootstrap5 %}
                {% bootstrap5 "OffcanvasBody" %}
                  <p>This offcanvas title uses h3.</p>
                {% endbootstrap5 %}
              {% endfill %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas-ctest01" aria-controls="offcanvas-ctest01">Toggle Offcanvas</button>
            <div class="offcanvas offcanvas-start" tabindex="-1" id="offcanvas-ctest01" aria-labelledby="offcanvas-ctest01-label">
              <div class="offcanvas-header">
                <h3 class="offcanvas-title" id="offcanvas-ctest01-label">Custom Heading</h3>
                <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
              </div>
              <div class="offcanvas-body">
                <p>This offcanvas title uses h3.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
