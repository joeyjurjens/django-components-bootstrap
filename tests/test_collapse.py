from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class TestCollapse(SimpleTestCase):
    maxDiff = None

    @djc_test
    def test_basic(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" %}
              {% fill "toggle" %}
                {% component "CollapseToggle" attrs:class="btn btn-primary" %}Toggle collapse{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                <div class="card card-body">
                  Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
                </div>
              {% endfill %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <button type="button" class="btn btn-primary" data-bs-toggle="collapse" data-bs-target="#collapse-ctest01" aria-expanded="false" aria-controls="collapse-ctest01">Toggle collapse</button>
            <div class="collapse" id="collapse-ctest01">
              <div class="card card-body">
                Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_multiple_targets(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            <p>
              {% component "Collapse" %}
                {% fill "toggle" %}
                  {% component "CollapseToggle" as_="a" attrs={"class": "btn btn-primary"} %}Toggle first element{% endcomponent %}
                {% endfill %}
                {% fill "default" %}
                  <div class="card card-body">
                    Some placeholder content for the first collapse component.
                  </div>
                {% endfill %}
              {% endcomponent %}
              {% component "Collapse" %}
                {% fill "toggle" %}
                  {% component "CollapseToggle" attrs={"class": "btn btn-primary"} %}Toggle second element{% endcomponent %}
                {% endfill %}
                {% fill "default" %}
                  <div class="card card-body">
                    Some placeholder content for the second collapse component.
                  </div>
                {% endfill %}
              {% endcomponent %}
            </p>
        """)
            rendered = template.render(Context())

        self.assertIn("Toggle first element", rendered)
        self.assertIn("Toggle second element", rendered)

    @djc_test
    def test_horizontal(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" horizontal=True %}
              {% fill "toggle" %}
                {% component "CollapseToggle" attrs:class="btn btn-primary" %}Toggle horizontal collapse{% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                <div class="card card-body" style="width: 300px;">
                  This is some placeholder content for a horizontal collapse. It's hidden by default and shown when triggered.
                </div>
              {% endfill %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <button type="button" class="btn btn-primary" data-bs-toggle="collapse" data-bs-target="#collapse-ctest01" aria-expanded="false" aria-controls="collapse-ctest01">Toggle horizontal collapse</button>
            <div class="collapse collapse-horizontal" id="collapse-ctest01">
              <div class="card card-body" style="width: 300px;">
                This is some placeholder content for a horizontal collapse. It's hidden by default and shown when triggered.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_with_button_toggle(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" %}
              {% fill "toggle" %}
                {% component "CollapseToggle" attrs={"class": "btn btn-primary"} %}
                  Button with data-bs-target
                {% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                <div class="card card-body">
                  Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
                </div>
              {% endfill %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <button class="btn btn-primary" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest01" aria-expanded="false" aria-controls="collapse-ctest01">
              Button with data-bs-target
            </button>
            <div class="collapse" id="collapse-ctest01">
              <div class="card card-body">
                Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_with_link_toggle(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" %}
              {% fill "toggle" %}
                {% component "CollapseToggle" as_="a" attrs={"class": "btn btn-primary"} %}
                  Link with href
                {% endcomponent %}
              {% endfill %}
              {% fill "default" %}
                <div class="card card-body">
                  Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
                </div>
              {% endfill %}
            {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <a class="btn btn-primary" data-bs-toggle="collapse" href="#collapse-ctest01" role="button" aria-expanded="false" aria-controls="collapse-ctest01">
              Link with href
            </a>
            <div class="collapse" id="collapse-ctest01">
              <div class="card card-body">
                Some placeholder content for the collapse component. This panel is hidden by default but revealed when the user activates the relevant trigger.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
