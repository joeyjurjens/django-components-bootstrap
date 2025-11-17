from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class TestModal(SimpleTestCase):
    maxDiff = None

    @djc_test
    def test_basic(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Modal title{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>Modal body text goes here.</p>
              {% endbootstrap5 %}
              {% bootstrap5 "ModalFooter" %}
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Modal title</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>Modal body text goes here.</p>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Save changes</button>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_small_size(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" size="sm" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Small Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This is a small modal.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-sm">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Small Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This is a small modal.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_large_size(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" size="lg" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Large Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This is a large modal.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-lg">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Large Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This is a large modal.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_extra_large_size(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" size="xl" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Extra Large Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This is an extra large modal.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-xl">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Extra Large Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This is an extra large modal.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_fullscreen(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" fullscreen=True %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Fullscreen Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This is a fullscreen modal.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-fullscreen">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This is a fullscreen modal.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_fullscreen_sm_down(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" fullscreen="sm" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Fullscreen Below SM{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal is fullscreen below sm breakpoint.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-fullscreen-sm-down">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Below SM</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal is fullscreen below sm breakpoint.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_fullscreen_md_down(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" fullscreen="md" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Fullscreen Below MD{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal is fullscreen below md breakpoint.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-fullscreen-md-down">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Below MD</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal is fullscreen below md breakpoint.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_fullscreen_lg_down(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" fullscreen="lg" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Fullscreen Below LG{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal is fullscreen below lg breakpoint.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-fullscreen-lg-down">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Fullscreen Below LG</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal is fullscreen below lg breakpoint.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_centered(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" centered=True %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Vertically Centered Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal is vertically centered.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Vertically Centered Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal is vertically centered.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_scrollable(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" scrollable=True %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Scrollable Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal has a scrollable body when content is long.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Scrollable Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal has a scrollable body when content is long.</p>
                    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_static_backdrop(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" backdrop="static" keyboard=False %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Static Backdrop Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal won't close when clicking outside.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true" data-bs-backdrop="static" data-bs-keyboard="false">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Static Backdrop Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal won't close when clicking outside.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_with_form(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}New message{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <form>
                  <div class="mb-3">
                    <label for="recipient-name" class="col-form-label">Recipient:</label>
                    <input type="text" class="form-control" id="recipient-name">
                  </div>
                  <div class="mb-3">
                    <label for="message-text" class="col-form-label">Message:</label>
                    <textarea class="form-control" id="message-text"></textarea>
                  </div>
                </form>
              {% endbootstrap5 %}
              {% bootstrap5 "ModalFooter" %}
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Send message</button>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">New message</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <form>
                      <div class="mb-3">
                        <label for="recipient-name" class="col-form-label">Recipient:</label>
                        <input type="text" class="form-control" id="recipient-name">
                      </div>
                      <div class="mb-3">
                        <label for="message-text" class="col-form-label">Message:</label>
                        <textarea class="form-control" id="message-text"></textarea>
                      </div>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                    <button type="button" class="btn btn-primary">Send message</button>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_without_fade(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" fade=False %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}No Fade Modal{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal doesn't have fade animation.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">No Fade Modal</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal doesn't have fade animation.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_header_without_close_button(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" %}
              {% bootstrap5 "ModalHeader" close_button=False %}
                {% bootstrap5 "ModalTitle" %}No Close Button{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal header has no close button.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">No Close Button</h5>
                  </div>
                  <div class="modal-body">
                    <p>This modal header has no close button.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_with_custom_title_heading(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" as_="h1" %}Custom Heading Level{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal title uses h1 instead of h5.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title" id="modal-ctest01-label">Custom Heading Level</h1>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal title uses h1 instead of h5.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_modal_centered_and_scrollable(self):
        with mock_component_id():
            template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Modal" centered=True scrollable=True %}
              {% bootstrap5 "ModalHeader" %}
                {% bootstrap5 "ModalTitle" %}Centered & Scrollable{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "ModalBody" %}
                <p>This modal is both centered and scrollable.</p>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
            rendered = template.render(Context())

        expected = """
            <div class="modal fade" id="modal-ctest01" tabindex="-1" aria-labelledby="modal-ctest01-label" aria-hidden="true">
              <div class="modal-dialog modal-dialog-centered modal-dialog-scrollable">
                <div class="modal-content">
                  <div class="modal-header">
                    <h5 class="modal-title" id="modal-ctest01-label">Centered & Scrollable</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
                  </div>
                  <div class="modal-body">
                    <p>This modal is both centered and scrollable.</p>
                  </div>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
