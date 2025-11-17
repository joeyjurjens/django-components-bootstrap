from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class ListGroupTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "ListGroup" %}
                {% bootstrap5 "ListGroupItem" %}An item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A second item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A third item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A fourth item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}And a fifth one{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" %}
                {% bootstrap5 "ListGroupItem" active=True %}An active item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A second item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A third item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A fourth item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}And a fifth one{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" %}
                {% bootstrap5 "ListGroupItem" %}An item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A second item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A third item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A fourth item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" disabled=True %}A disabled fifth item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" as_="div" %}
                {% bootstrap5 "ListGroupItem" href="#" active=True %}The current link item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" %}A second link item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" %}A third link item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" %}A fourth link item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" disabled=True %}A disabled link item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" as_="div" %}
                {% bootstrap5 "ListGroupItem" as_="button" active=True %}The current button{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" as_="button" %}A second button item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" as_="button" %}A third button item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" as_="button" %}A fourth button item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" as_="button" disabled=True %}A disabled button item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" flush=True %}
                {% bootstrap5 "ListGroupItem" %}An item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A second item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A third item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A fourth item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}And a fifth one{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" numbered=True %}
                {% bootstrap5 "ListGroupItem" %}A list item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A list item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A list item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" numbered=True %}
                {% bootstrap5 "ListGroupItem" attrs:class="d-flex justify-content-between align-items-start" %}
                    <div class="ms-2 me-auto">
                      <div class="fw-bold">Subheading</div>
                      Content for list item
                    </div>
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" attrs:class="d-flex justify-content-between align-items-start" %}
                    <div class="ms-2 me-auto">
                      <div class="fw-bold">Subheading</div>
                      Content for list item
                    </div>
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" attrs:class="d-flex justify-content-between align-items-start" %}
                    <div class="ms-2 me-auto">
                      <div class="fw-bold">Subheading</div>
                      Content for list item
                    </div>
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" horizontal=True %}
                {% bootstrap5 "ListGroupItem" %}An item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A second item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A third item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" horizontal="sm" %}
                {% bootstrap5 "ListGroupItem" %}An item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A second item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A third item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" horizontal="md" %}
                {% bootstrap5 "ListGroupItem" %}An item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A second item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}A third item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" %}
                {% bootstrap5 "ListGroupItem" %}A simple default list group item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="primary" %}A simple primary item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="secondary" %}A simple secondary item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="success" %}A simple success item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="danger" %}A simple danger item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="warning" %}A simple warning item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="info" %}A simple info item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="light" %}A simple light item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" variant="dark" %}A simple dark item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" as_="div" %}
                {% bootstrap5 "ListGroupItem" href="#" %}A simple default item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="primary" %}A simple primary item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="secondary" %}A simple secondary item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="success" %}A simple success item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="danger" %}A simple danger item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="warning" %}A simple warning item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="info" %}A simple info item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="light" %}A simple light item{% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" variant="dark" %}A simple dark item{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" %}
                {% bootstrap5 "ListGroupItem" attrs:class="d-flex justify-content-between align-items-center" %}
                    A list item
                    <span class="badge text-bg-primary rounded-pill">14</span>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" attrs:class="d-flex justify-content-between align-items-center" %}
                    A second list item
                    <span class="badge text-bg-primary rounded-pill">2</span>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" attrs:class="d-flex justify-content-between align-items-center" %}
                    A third list item
                    <span class="badge text-bg-primary rounded-pill">1</span>
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" as_="div" %}
                {% bootstrap5 "ListGroupItem" href="#" active=True %}
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">List group item heading</h5>
                      <small>3 days ago</small>
                    </div>
                    <p class="mb-1">Some placeholder content in a paragraph.</p>
                    <small>And some small print.</small>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" %}
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">List group item heading</h5>
                      <small class="text-body-secondary">3 days ago</small>
                    </div>
                    <p class="mb-1">Some placeholder content in a paragraph.</p>
                    <small class="text-body-secondary">And some muted small print.</small>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" href="#" %}
                    <div class="d-flex w-100 justify-content-between">
                      <h5 class="mb-1">List group item heading</h5>
                      <small class="text-body-secondary">3 days ago</small>
                    </div>
                    <p class="mb-1">Some placeholder content in a paragraph.</p>
                    <small class="text-body-secondary">And some muted small print.</small>
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" %}
                {% bootstrap5 "ListGroupItem" %}
                    <input class="form-check-input me-1" type="checkbox" value="" id="firstCheckbox">
                    <label class="form-check-label" for="firstCheckbox">First checkbox</label>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}
                    <input class="form-check-input me-1" type="checkbox" value="" id="secondCheckbox">
                    <label class="form-check-label" for="secondCheckbox">Second checkbox</label>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}
                    <input class="form-check-input me-1" type="checkbox" value="" id="thirdCheckbox">
                    <label class="form-check-label" for="thirdCheckbox">Third checkbox</label>
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% bootstrap5 "ListGroup" %}
                {% bootstrap5 "ListGroupItem" %}
                    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="firstRadio" checked>
                    <label class="form-check-label" for="firstRadio">First radio</label>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}
                    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="secondRadio">
                    <label class="form-check-label" for="secondRadio">Second radio</label>
                {% endbootstrap5 %}
                {% bootstrap5 "ListGroupItem" %}
                    <input class="form-check-input me-1" type="radio" name="listGroupRadio" value="" id="thirdRadio">
                    <label class="form-check-label" for="thirdRadio">Third radio</label>
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
