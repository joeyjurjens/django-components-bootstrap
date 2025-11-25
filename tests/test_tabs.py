from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class TestTabs(SimpleTestCase):
    maxDiff = None

    @djc_test
    def test_basic(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Tabs" %}
              {% component "Tab" title="Home" %}
                Home content
              {% endcomponent %}
              {% component "Tab" title="Profile" %}
                Profile content
              {% endcomponent %}
              {% component "Tab" title="Contact" %}
                Contact content
              {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div>
              <ul class="nav nav-tabs" id="tabs-ctest01" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-contact" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-contact" type="button" role="tab" aria-controls="tabs-ctest01-pane-contact" aria-selected="false">Contact</button>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
                  Home content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
                  Profile content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-contact" role="tabpanel" aria-labelledby="tabs-ctest01-tab-contact" tabindex="0">
                  Contact content
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_pills_variant(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Tabs" variant="pills" %}
              {% component "Tab" title="Home" %}
                Home content
              {% endcomponent %}
              {% component "Tab" title="Profile" %}
                Profile content
              {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div>
              <ul class="nav nav-pills" id="tabs-ctest01" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
                  Home content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
                  Profile content
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_underline_variant(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Tabs" variant="underline" %}
              {% component "Tab" title="Home" %}
                Home content
              {% endcomponent %}
              {% component "Tab" title="Profile" %}
                Profile content
              {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div>
              <ul class="nav nav-underline" id="tabs-ctest01" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
                  Home content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
                  Profile content
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_tabs_with_fill(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Tabs" fill=True %}
              {% component "Tab" title="Home" %}
                Home content
              {% endcomponent %}
              {% component "Tab" title="Longer title" %}
                Profile content
              {% endcomponent %}
              {% component "Tab" title="Link" %}
                Contact content
              {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div>
              <ul class="nav nav-tabs nav-fill" id="tabs-ctest01" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-longer-title" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-longer-title" type="button" role="tab" aria-controls="tabs-ctest01-pane-longer-title" aria-selected="false">Longer title</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-link" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-link" type="button" role="tab" aria-controls="tabs-ctest01-pane-link" aria-selected="false">Link</button>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
                  Home content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-longer-title" role="tabpanel" aria-labelledby="tabs-ctest01-tab-longer-title" tabindex="0">
                  Profile content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-link" role="tabpanel" aria-labelledby="tabs-ctest01-tab-link" tabindex="0">
                  Contact content
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_tabs_with_justified(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Tabs" justified=True %}
              {% component "Tab" title="Home" %}
                Home content
              {% endcomponent %}
              {% component "Tab" title="Profile" %}
                Profile content
              {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div>
              <ul class="nav nav-tabs nav-justified" id="tabs-ctest01" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
                  Home content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
                  Profile content
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_tabs_with_disabled_tab(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Tabs" %}
              {% component "Tab" title="Home" %}
                Home content
              {% endcomponent %}
              {% component "Tab" title="Profile" %}
                Profile content
              {% endcomponent %}
              {% component "Tab" title="Disabled" disabled=True %}
                Disabled content
              {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div>
              <ul class="nav nav-tabs" id="tabs-ctest01" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="true">Home</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="false">Profile</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link disabled" id="tabs-ctest01-tab-disabled" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-disabled" type="button" role="tab" aria-controls="tabs-ctest01-pane-disabled" aria-selected="false" disabled>Disabled</button>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade show active" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
                  Home content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
                  Profile content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-disabled" role="tabpanel" aria-labelledby="tabs-ctest01-tab-disabled" tabindex="0">
                  Disabled content
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_tabs_with_active_tab(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Tabs" %}
              {% component "Tab" title="Home" %}
                Home content
              {% endcomponent %}
              {% component "Tab" title="Profile" active=True %}
                Profile content
              {% endcomponent %}
              {% component "Tab" title="Contact" %}
                Contact content
              {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div>
              <ul class="nav nav-tabs" id="tabs-ctest01" role="tablist">
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-home" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-home" type="button" role="tab" aria-controls="tabs-ctest01-pane-home" aria-selected="false">Home</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link active" id="tabs-ctest01-tab-profile" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-profile" type="button" role="tab" aria-controls="tabs-ctest01-pane-profile" aria-selected="true">Profile</button>
                </li>
                <li class="nav-item" role="presentation">
                  <button class="nav-link" id="tabs-ctest01-tab-contact" data-bs-toggle="tab" data-bs-target="#tabs-ctest01-pane-contact" type="button" role="tab" aria-controls="tabs-ctest01-pane-contact" aria-selected="false">Contact</button>
                </li>
              </ul>
              <div class="tab-content">
                <div class="tab-pane fade" id="tabs-ctest01-pane-home" role="tabpanel" aria-labelledby="tabs-ctest01-tab-home" tabindex="0">
                  Home content
                </div>
                <div class="tab-pane fade show active" id="tabs-ctest01-pane-profile" role="tabpanel" aria-labelledby="tabs-ctest01-tab-profile" tabindex="0">
                  Profile content
                </div>
                <div class="tab-pane fade" id="tabs-ctest01-pane-contact" role="tabpanel" aria-labelledby="tabs-ctest01-tab-contact" tabindex="0">
                  Contact content
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
