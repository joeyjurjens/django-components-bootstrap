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
            {% load component_tags %}
            {% component "Modal" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Modal title{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>Modal body text goes here.</p>
              {% endcomponent %}
              {% component "ModalFooter" %}
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" size="sm" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Small Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This is a small modal.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" size="lg" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Large Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This is a large modal.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" size="xl" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Extra Large Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This is an extra large modal.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" fullscreen=True %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Fullscreen Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This is a fullscreen modal.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" fullscreen="sm" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Fullscreen Below SM{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal is fullscreen below sm breakpoint.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" fullscreen="md" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Fullscreen Below MD{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal is fullscreen below md breakpoint.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" fullscreen="lg" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Fullscreen Below LG{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal is fullscreen below lg breakpoint.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" centered=True %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Vertically Centered Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal is vertically centered.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" scrollable=True %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Scrollable Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal has a scrollable body when content is long.</p>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" backdrop="static" keyboard=False %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Static Backdrop Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal won't close when clicking outside.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}New message{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
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
              {% endcomponent %}
              {% component "ModalFooter" %}
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Send message</button>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" fade=False %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}No Fade Modal{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal doesn't have fade animation.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" %}
              {% component "ModalHeader" close_button=False %}
                {% component "ModalTitle" %}No Close Button{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal header has no close button.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" as_="h1" %}Custom Heading Level{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal title uses h1 instead of h5.</p>
              {% endcomponent %}
            {% endcomponent %}
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
            {% load component_tags %}
            {% component "Modal" centered=True scrollable=True %}
              {% component "ModalHeader" %}
                {% component "ModalTitle" %}Centered & Scrollable{% endcomponent %}
              {% endcomponent %}
              {% component "ModalBody" %}
                <p>This modal is both centered and scrollable.</p>
              {% endcomponent %}
            {% endcomponent %}
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
