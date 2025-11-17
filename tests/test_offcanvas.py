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
            {% component "Offcanvas" scroll=False keyboard=False %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs={"class": "btn btn-primary", "type": "button"} %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Offcanvas{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  Content for the offcanvas goes here. You can place just about any Bootstrap component or custom elements here.
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" placement="start" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Offcanvas Start{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This offcanvas appears from the start (left).</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" placement="end" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Offcanvas End{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This offcanvas appears from the end (right).</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" placement="top" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Offcanvas Top{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This offcanvas appears from the top.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" placement="bottom" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Offcanvas Bottom{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This offcanvas appears from the bottom.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" scroll=True backdrop="false" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Offcanvas with body scrolling{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>Try scrolling the rest of the page to see this option in action.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" scroll=True %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Backdrop with scrolling{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>Try scrolling the rest of the page to see this option in action.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" backdrop="static" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Static Backdrop{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>I will not close if you click outside of me.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" backdrop="false" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}No Backdrop{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This offcanvas has no backdrop.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" responsive="lg" placement="end" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Responsive offcanvas{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This is content within an offcanvas-lg.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" responsive="md" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" %}Responsive MD offcanvas{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This is content within an offcanvas-md.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" close_button=False %}
                  {% component "OffcanvasTitle" %}No Close Button{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This offcanvas header has no close button.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
            {% component "Offcanvas" %}
              {% fill "toggle" %}
                {% component "OffcanvasToggle" attrs:class="btn btn-primary" %}Toggle Offcanvas{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                {% component "OffcanvasHeader" %}
                  {% component "OffcanvasTitle" as_="h3" %}Custom Heading{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}
                  <p>This offcanvas title uses h3.</p>
                {% endcomponent %}
              {% endfill %}
            {% endcomponent %}
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
