from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class TestToast(SimpleTestCase):
    maxDiff = None

    @djc_test
    def test_basic_with_header(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "Toast" %}
                  {% component "ToastHeader" %}
                    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                    <strong class="me-auto">Bootstrap</strong>
                    <small>11 mins ago</small>
                  {% endcomponent %}
                  {% component "ToastBody" %}
                    Hello, world! This is a toast message.
                  {% endcomponent %}
                {% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
              <div class="toast-header">
                <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                <strong class="me-auto">Bootstrap</strong>
                <small>11 mins ago</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>
              <div class="toast-body">
                Hello, world! This is a toast message.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_autohide_false(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "Toast" autohide=False %}
                  {% component "ToastHeader" %}
                    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                    <strong class="me-auto">Bootstrap</strong>
                    <small>11 mins ago</small>
                  {% endcomponent %}
                  {% component "ToastBody" %}
                    Hello, world! This is a toast message.
                  {% endcomponent %}
                {% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <div role="alert" aria-live="assertive" aria-atomic="true" class="toast" data-bs-autohide="false" id="toast-ctest01">
              <div class="toast-header">
                <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                <strong class="me-auto">Bootstrap</strong>
                <small>11 mins ago</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>
              <div class="toast-body">
                Hello, world! This is a toast message.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_translucent(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "Toast" %}
                  {% component "ToastHeader" %}
                    <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                    <strong class="me-auto">Bootstrap</strong>
                    <small class="text-body-secondary">11 mins ago</small>
                  {% endcomponent %}
                  {% component "ToastBody" %}
                    Hello, world! This is a toast message.
                  {% endcomponent %}
                {% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
              <div class="toast-header">
                <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                <strong class="me-auto">Bootstrap</strong>
                <small class="text-body-secondary">11 mins ago</small>
                <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>
              <div class="toast-body">
                Hello, world! This is a toast message.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_stacking(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                <div class="toast-container position-static">
                  {% component "Toast" %}
                    {% component "ToastHeader" %}
                      <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                      <strong class="me-auto">Bootstrap</strong>
                      <small class="text-body-secondary">just now</small>
                    {% endcomponent %}
                    {% component "ToastBody" %}
                      See? Just like this.
                    {% endcomponent %}
                  {% endcomponent %}

                  {% component "Toast" %}
                    {% component "ToastHeader" %}
                      <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                      <strong class="me-auto">Bootstrap</strong>
                      <small class="text-body-secondary">2 seconds ago</small>
                    {% endcomponent %}
                    {% component "ToastBody" %}
                      Heads up, toasts will stack automatically
                    {% endcomponent %}
                  {% endcomponent %}
                </div>
            """)
            rendered = template.render(Context())

        expected = """
            <div class="toast-container position-static">
              <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
                <div class="toast-header">
                  <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                  <strong class="me-auto">Bootstrap</strong>
                  <small class="text-body-secondary">just now</small>
                  <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">
                  See? Just like this.
                </div>
              </div>

              <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest05">
                <div class="toast-header">
                  <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                  <strong class="me-auto">Bootstrap</strong>
                  <small class="text-body-secondary">2 seconds ago</small>
                  <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">
                  Heads up, toasts will stack automatically
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_custom_content_simplified(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "Toast" attrs:class="align-items-center" %}
                  <div class="d-flex">
                    {% component "ToastBody" %}
                      Hello, world! This is a toast message.
                    {% endcomponent %}
                    {% component "CloseButton" attrs:class="me-2 m-auto" attrs:data-bs-dismiss="toast" / %}
                  </div>
                {% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <div class="toast align-items-center" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
              <div class="d-flex">
                <div class="toast-body">
                  Hello, world! This is a toast message.
                </div>
                <button type="button" class="btn-close me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_custom_content_with_actions(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "Toast" %}
                  {% component "ToastBody" %}
                    Hello, world! This is a toast message.
                    <div class="mt-2 pt-2 border-top">
                      {% component "Button" variant="primary" size="sm" %}Take action{% endcomponent %}
                      {% component "Button" variant="secondary" size="sm" attrs:data-bs-dismiss="toast" %}Close{% endcomponent %}
                    </div>
                  {% endcomponent %}
                {% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
              <div class="toast-body">
                Hello, world! This is a toast message.
                <div class="mt-2 pt-2 border-top">
                  <button type="button" class="btn btn-primary btn-sm">Take action</button>
                  <button type="button" class="btn btn-secondary btn-sm" data-bs-dismiss="toast">Close</button>
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_color_scheme_primary(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "Toast" attrs:class="align-items-center text-bg-primary border-0" %}
                  <div class="d-flex">
                    {% component "ToastBody" %}
                      Hello, world! This is a toast message.
                    {% endcomponent %}
                    {% component "CloseButton" variant="white" attrs:class="me-2 m-auto" attrs:data-bs-dismiss="toast" / %}
                  </div>
                {% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <div class="toast align-items-center text-bg-primary border-0" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest01">
              <div class="d-flex">
                <div class="toast-body">
                  Hello, world! This is a toast message.
                </div>
                <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_toast_container_bottom_end(self):
        with mock_component_id():
            template = Template("""
                {% load component_tags %}
                {% component "ToastContainer" position="end" attrs:class="bottom-0 p-3" %}
                  {% component "Toast" %}
                    {% component "ToastHeader" %}
                      <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                      <strong class="me-auto">Bootstrap</strong>
                      <small>11 mins ago</small>
                    {% endcomponent %}
                    {% component "ToastBody" %}
                      Hello, world! This is a toast message.
                    {% endcomponent %}
                  {% endcomponent %}
                {% endcomponent %}
            """)
            rendered = template.render(Context())

        expected = """
            <div class="toast-container position-fixed top-0 end-0 bottom-0 p-3">
              <div class="toast" role="alert" aria-live="assertive" aria-atomic="true" id="toast-ctest02">
                <div class="toast-header">
                  <img src="https://placehold.net/600x400.png" class="rounded me-2" alt="Toast icon">
                  <strong class="me-auto">Bootstrap</strong>
                  <small>11 mins ago</small>
                  <button type="button" class="btn-close" data-bs-dismiss="toast" aria-label="Close"></button>
                </div>
                <div class="toast-body">
                  Hello, world! This is a toast message.
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
