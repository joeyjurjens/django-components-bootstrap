from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class TestToggleButton(SimpleTestCase):
    @djc_test
    def test_checkbox_single(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "ToggleButton" attrs:id="btn-check" variant="primary" outline=False %}Single toggle{% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <input type="checkbox" class="btn-check" id="btn-check" autocomplete="off">
            <label class="btn btn-primary" for="btn-check">Single toggle</label>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_checkbox_checked(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "ToggleButton" attrs:id="btn-check-2" checked=True variant="primary" outline=False %}Checked{% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <input type="checkbox" class="btn-check" id="btn-check-2" checked autocomplete="off">
            <label class="btn btn-primary" for="btn-check-2">Checked</label>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_checkbox_disabled(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "ToggleButton" attrs:id="btn-check-3" disabled=True variant="primary" outline=False %}Disabled{% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <input type="checkbox" class="btn-check" id="btn-check-3" autocomplete="off" disabled>
            <label class="btn btn-primary" for="btn-check-3">Disabled</label>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_radio_checked(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "ToggleButton" type="radio" name="options" attrs:id="option1" checked=True variant="secondary" outline=False %}Checked{% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <input type="radio" class="btn-check" name="options" id="option1" autocomplete="off" checked>
            <label class="btn btn-secondary" for="option1">Checked</label>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_radio_unchecked(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "ToggleButton" type="radio" name="options" attrs:id="option2" variant="secondary" outline=False %}Radio{% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <input type="radio" class="btn-check" name="options" id="option2" autocomplete="off">
            <label class="btn btn-secondary" for="option2">Radio</label>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_radio_disabled(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "ToggleButton" type="radio" name="options" attrs:id="option3" disabled=True variant="secondary" outline=False %}Disabled{% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <input type="radio" class="btn-check" name="options" id="option3" autocomplete="off" disabled>
            <label class="btn btn-secondary" for="option3">Disabled</label>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
