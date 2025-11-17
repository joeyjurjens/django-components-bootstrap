from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class ListGroupTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" %}
                {% component "ListGroupItem" %}An item{% endcomponent %}
                {% component "ListGroupItem" %}A second item{% endcomponent %}
                {% component "ListGroupItem" %}A third item{% endcomponent %}
                {% component "ListGroupItem" %}A fourth item{% endcomponent %}
                {% component "ListGroupItem" %}And a fifth one{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group">
              <li class="list-group-item">An item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
              <li class="list-group-item">A fourth item</li>
              <li class="list-group-item">And a fifth one</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_active_items(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" %}
                {% component "ListGroupItem" active=True %}An active item{% endcomponent %}
                {% component "ListGroupItem" %}A second item{% endcomponent %}
                {% component "ListGroupItem" %}A third item{% endcomponent %}
                {% component "ListGroupItem" %}A fourth item{% endcomponent %}
                {% component "ListGroupItem" %}And a fifth one{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group">
              <li class="list-group-item active" aria-current="true">An active item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
              <li class="list-group-item">A fourth item</li>
              <li class="list-group-item">And a fifth one</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_disabled_items(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" %}
                {% component "ListGroupItem" %}An item{% endcomponent %}
                {% component "ListGroupItem" %}A second item{% endcomponent %}
                {% component "ListGroupItem" %}A third item{% endcomponent %}
                {% component "ListGroupItem" %}A fourth item{% endcomponent %}
                {% component "ListGroupItem" disabled=True %}A disabled fifth item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group">
              <li class="list-group-item">An item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
              <li class="list-group-item">A fourth item</li>
              <li class="list-group-item disabled" aria-disabled="true">A disabled fifth item</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_links(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" as_="div" %}
                {% component "ListGroupItem" href="#" active=True %}The current link item{% endcomponent %}
                {% component "ListGroupItem" href="#" %}A second link item{% endcomponent %}
                {% component "ListGroupItem" href="#" %}A third link item{% endcomponent %}
                {% component "ListGroupItem" href="#" %}A fourth link item{% endcomponent %}
                {% component "ListGroupItem" href="#" disabled=True %}A disabled link item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="list-group">
              <a href="#" class="list-group-item list-group-item-action active" aria-current="true">The current link item</a>
              <a href="#" class="list-group-item list-group-item-action">A second link item</a>
              <a href="#" class="list-group-item list-group-item-action">A third link item</a>
              <a href="#" class="list-group-item list-group-item-action">A fourth link item</a>
              <a href="#" class="list-group-item list-group-item-action disabled" aria-disabled="true">A disabled link item</a>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_buttons(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" as_="div" %}
                {% component "ListGroupItem" as_="button" active=True %}The current button{% endcomponent %}
                {% component "ListGroupItem" as_="button" %}A second button item{% endcomponent %}
                {% component "ListGroupItem" as_="button" %}A third button item{% endcomponent %}
                {% component "ListGroupItem" as_="button" %}A fourth button item{% endcomponent %}
                {% component "ListGroupItem" as_="button" disabled=True %}A disabled button item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="list-group">
              <button type="button" class="list-group-item list-group-item-action active" aria-current="true">The current button</button>
              <button type="button" class="list-group-item list-group-item-action">A second button item</button>
              <button type="button" class="list-group-item list-group-item-action">A third button item</button>
              <button type="button" class="list-group-item list-group-item-action">A fourth button item</button>
              <button type="button" class="list-group-item list-group-item-action" disabled>A disabled button item</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_flush(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" flush=True %}
                {% component "ListGroupItem" %}An item{% endcomponent %}
                {% component "ListGroupItem" %}A second item{% endcomponent %}
                {% component "ListGroupItem" %}A third item{% endcomponent %}
                {% component "ListGroupItem" %}A fourth item{% endcomponent %}
                {% component "ListGroupItem" %}And a fifth one{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group list-group-flush">
              <li class="list-group-item">An item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
              <li class="list-group-item">A fourth item</li>
              <li class="list-group-item">And a fifth one</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_numbered(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" numbered=True %}
                {% component "ListGroupItem" %}A list item{% endcomponent %}
                {% component "ListGroupItem" %}A list item{% endcomponent %}
                {% component "ListGroupItem" %}A list item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ol class="list-group list-group-numbered">
              <li class="list-group-item">A list item</li>
              <li class="list-group-item">A list item</li>
              <li class="list-group-item">A list item</li>
            </ol>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_numbered_with_custom_content(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" numbered=True %}
                {% component "ListGroupItem" attrs:class="d-flex justify-content-between align-items-start" %}
                    <div class="ms-2 me-auto">
                      <div class="fw-bold">Subheading</div>
                      Content for list item
                    </div>
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endcomponent %}
                {% component "ListGroupItem" attrs:class="d-flex justify-content-between align-items-start" %}
                    <div class="ms-2 me-auto">
                      <div class="fw-bold">Subheading</div>
                      Content for list item
                    </div>
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endcomponent %}
                {% component "ListGroupItem" attrs:class="d-flex justify-content-between align-items-start" %}
                    <div class="ms-2 me-auto">
                      <div class="fw-bold">Subheading</div>
                      Content for list item
                    </div>
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ol class="list-group list-group-numbered">
              <li class="list-group-item d-flex justify-content-between align-items-start">
                <div class="ms-2 me-auto">
                  <div class="fw-bold">Subheading</div>
                  Content for list item
                </div>
                <span class="badge text-bg-primary rounded-pill">14</span>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-start">
                <div class="ms-2 me-auto">
                  <div class="fw-bold">Subheading</div>
                  Content for list item
                </div>
                <span class="badge text-bg-primary rounded-pill">14</span>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-start">
                <div class="ms-2 me-auto">
                  <div class="fw-bold">Subheading</div>
                  Content for list item
                </div>
                <span class="badge text-bg-primary rounded-pill">14</span>
              </li>
            </ol>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_horizontal(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" horizontal=True %}
                {% component "ListGroupItem" %}An item{% endcomponent %}
                {% component "ListGroupItem" %}A second item{% endcomponent %}
                {% component "ListGroupItem" %}A third item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group list-group-horizontal">
              <li class="list-group-item">An item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_horizontal_responsive_sm(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" horizontal="sm" %}
                {% component "ListGroupItem" %}An item{% endcomponent %}
                {% component "ListGroupItem" %}A second item{% endcomponent %}
                {% component "ListGroupItem" %}A third item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group list-group-horizontal-sm">
              <li class="list-group-item">An item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_horizontal_responsive_md(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" horizontal="md" %}
                {% component "ListGroupItem" %}An item{% endcomponent %}
                {% component "ListGroupItem" %}A second item{% endcomponent %}
                {% component "ListGroupItem" %}A third item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group list-group-horizontal-md">
              <li class="list-group-item">An item</li>
              <li class="list-group-item">A second item</li>
              <li class="list-group-item">A third item</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_contextual_variants(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" %}
                {% component "ListGroupItem" %}A simple default list group item{% endcomponent %}
                {% component "ListGroupItem" variant="primary" %}A simple primary item{% endcomponent %}
                {% component "ListGroupItem" variant="secondary" %}A simple secondary item{% endcomponent %}
                {% component "ListGroupItem" variant="success" %}A simple success item{% endcomponent %}
                {% component "ListGroupItem" variant="danger" %}A simple danger item{% endcomponent %}
                {% component "ListGroupItem" variant="warning" %}A simple warning item{% endcomponent %}
                {% component "ListGroupItem" variant="info" %}A simple info item{% endcomponent %}
                {% component "ListGroupItem" variant="light" %}A simple light item{% endcomponent %}
                {% component "ListGroupItem" variant="dark" %}A simple dark item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group">
              <li class="list-group-item">A simple default list group item</li>
              <li class="list-group-item list-group-item-primary">A simple primary item</li>
              <li class="list-group-item list-group-item-secondary">A simple secondary item</li>
              <li class="list-group-item list-group-item-success">A simple success item</li>
              <li class="list-group-item list-group-item-danger">A simple danger item</li>
              <li class="list-group-item list-group-item-warning">A simple warning item</li>
              <li class="list-group-item list-group-item-info">A simple info item</li>
              <li class="list-group-item list-group-item-light">A simple light item</li>
              <li class="list-group-item list-group-item-dark">A simple dark item</li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_contextual_variants_for_links(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" as_="div" %}
                {% component "ListGroupItem" href="#" %}A simple default item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="primary" %}A simple primary item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="secondary" %}A simple secondary item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="success" %}A simple success item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="danger" %}A simple danger item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="warning" %}A simple warning item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="info" %}A simple info item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="light" %}A simple light item{% endcomponent %}
                {% component "ListGroupItem" href="#" variant="dark" %}A simple dark item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="list-group">
              <a href="#" class="list-group-item list-group-item-action">A simple default item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-primary">A simple primary item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-secondary">A simple secondary item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-success">A simple success item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-danger">A simple danger item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-warning">A simple warning item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-info">A simple info item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-light">A simple light item</a>
              <a href="#" class="list-group-item list-group-item-action list-group-item-dark">A simple dark item</a>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_with_badges(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" %}
                {% component "ListGroupItem" attrs:class="d-flex justify-content-between align-items-center" %}
                    A list item
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endcomponent %}
                {% component "ListGroupItem" attrs:class="d-flex justify-content-between align-items-center" %}
                    A second list item
                    <span class="badge text-bg-primary rounded-pill">2</span>
                {% endcomponent %}
                {% component "ListGroupItem" attrs:class="d-flex justify-content-between align-items-center" %}
                    A third list item
                    <span class="badge text-bg-primary rounded-pill">1</span>
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group">
              <li class="list-group-item d-flex justify-content-between align-items-center">
                A list item
                <span class="badge text-bg-primary rounded-pill">14</span>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-center">
                A second list item
                <span class="badge text-bg-primary rounded-pill">2</span>
              </li>
              <li class="list-group-item d-flex justify-content-between align-items-center">
                A third list item
                <span class="badge text-bg-primary rounded-pill">1</span>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_custom_content(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" as_="div" %}
                {% component "ListGroupItem" href="#" active=True %}
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">List group item heading</h5>
                      <small>3 days ago</small>
                    </div>
                    <p class="mb-1">Some placeholder content in a paragraph.</p>
                    <small>And some small print.</small>
                {% endcomponent %}
                {% component "ListGroupItem" href="#" %}
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">List group item heading</h5>
                      <small class="text-body-secondary">3 days ago</small>
                    </div>
                    <p class="mb-1">Some placeholder content in a paragraph.</p>
                    <small class="text-body-secondary">And some muted small print.</small>
                {% endcomponent %}
                {% component "ListGroupItem" href="#" %}
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">List group item heading</h5>
                      <small class="text-body-secondary">3 days ago</small>
                    </div>
                    <p class="mb-1">Some placeholder content in a paragraph.</p>
                    <small class="text-body-secondary">And some muted small print.</small>
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="list-group">
              <a href="#" class="list-group-item list-group-item-action active" aria-current="true">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">List group item heading</h5>
                  <small>3 days ago</small>
                </div>
                <p class="mb-1">Some placeholder content in a paragraph.</p>
                <small>And some small print.</small>
              </a>
              <a href="#" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">List group item heading</h5>
                  <small class="text-body-secondary">3 days ago</small>
                </div>
                <p class="mb-1">Some placeholder content in a paragraph.</p>
                <small class="text-body-secondary">And some muted small print.</small>
              </a>
              <a href="#" class="list-group-item list-group-item-action">
                <div class="d-flex w-100 justify-content-between">
                  <h5 class="mb-1">List group item heading</h5>
                  <small class="text-body-secondary">3 days ago</small>
                </div>
                <p class="mb-1">Some placeholder content in a paragraph.</p>
                <small class="text-body-secondary">And some muted small print.</small>
              </a>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_with_checkboxes(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" %}
                {% component "ListGroupItem" %}
                    <input class="form-check-input me-1" type="checkbox" value="" id="firstCheckbox">
                    <label class="form-check-label" for="firstCheckbox">First checkbox</label>
                {% endcomponent %}
                {% component "ListGroupItem" %}
                    <input class="form-check-input me-1" type="checkbox" value="" id="secondCheckbox">
                    <label class="form-check-label" for="secondCheckbox">Second checkbox</label>
                {% endcomponent %}
                {% component "ListGroupItem" %}
                    <input class="form-check-input me-1" type="checkbox" value="" id="thirdCheckbox">
                    <label class="form-check-label" for="thirdCheckbox">Third checkbox</label>
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group">
              <li class="list-group-item">
                <input class="form-check-input me-1" type="checkbox" value="" id="firstCheckbox">
                <label class="form-check-label" for="firstCheckbox">First checkbox</label>
              </li>
              <li class="list-group-item">
                <input class="form-check-input me-1" type="checkbox" value="" id="secondCheckbox">
                <label class="form-check-label" for="secondCheckbox">Second checkbox</label>
              </li>
              <li class="list-group-item">
                <input class="form-check-input me-1" type="checkbox" value="" id="thirdCheckbox">
                <label class="form-check-label" for="thirdCheckbox">Third checkbox</label>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_with_radio_buttons(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" %}
                {% component "ListGroupItem" %}
                    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="firstRadio" checked>
                    <label class="form-check-label" for="firstRadio">First radio</label>
                {% endcomponent %}
                {% component "ListGroupItem" %}
                    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="secondRadio">
                    <label class="form-check-label" for="secondRadio">Second radio</label>
                {% endcomponent %}
                {% component "ListGroupItem" %}
                    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="thirdRadio">
                    <label class="form-check-label" for="thirdRadio">Third radio</label>
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <ul class="list-group">
              <li class="list-group-item">
                <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="firstRadio" checked>
                <label class="form-check-label" for="firstRadio">First radio</label>
              </li>
              <li class="list-group-item">
                <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="secondRadio">
                <label class="form-check-label" for="secondRadio">Second radio</label>
              </li>
              <li class="list-group-item">
                <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="thirdRadio">
                <label class="form-check-label" for="thirdRadio">Third radio</label>
              </li>
            </ul>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
