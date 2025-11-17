from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class StackTests(SimpleTestCase):
    maxDiff = None

    def test_vstack(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="vertical" gap=3 %}
                <div class="p-2">First item</div>
                <div class="p-2">Second item</div>
                <div class="p-2">Third item</div>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="vstack gap-3">
              <div class="p-2">First item</div>
              <div class="p-2">Second item</div>
              <div class="p-2">Third item</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_hstack(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="horizontal" gap=3 %}
                <div class="p-2">First item</div>
                <div class="p-2">Second item</div>
                <div class="p-2">Third item</div>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="hstack gap-3">
              <div class="p-2">First item</div>
              <div class="p-2">Second item</div>
              <div class="p-2">Third item</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_hstack_with_spacer(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="horizontal" gap=3 %}
                <div class="p-2">First item</div>
                <div class="p-2 ms-auto">Second item</div>
                <div class="p-2">Third item</div>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="hstack gap-3">
              <div class="p-2">First item</div>
              <div class="p-2 ms-auto">Second item</div>
              <div class="p-2">Third item</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_hstack_with_vertical_rule(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="horizontal" gap=3 %}
                <div class="p-2">First item</div>
                <div class="p-2 ms-auto">Second item</div>
                <div class="vr"></div>
                <div class="p-2">Third item</div>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="hstack gap-3">
              <div class="p-2">First item</div>
              <div class="p-2 ms-auto">Second item</div>
              <div class="vr"></div>
              <div class="p-2">Third item</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_vstack_buttons(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="vertical" gap=2 %}
                <button type="button" class="btn btn-secondary">Save changes</button>
                <button type="button" class="btn btn-outline-secondary">Cancel</button>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="vstack gap-2">
              <button type="button" class="btn btn-secondary">Save changes</button>
              <button type="button" class="btn btn-outline-secondary">Cancel</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_hstack_inline_form(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="horizontal" gap=3 %}
                <input class="form-control me-auto" type="text" placeholder="Add your item here..." aria-label="Add your item here...">
                <button type="button" class="btn btn-secondary">Submit</button>
                <div class="vr"></div>
                <button type="button" class="btn btn-outline-danger">Reset</button>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="hstack gap-3">
              <input class="form-control me-auto" type="text" placeholder="Add your item here..." aria-label="Add your item here...">
              <button type="button" class="btn btn-secondary">Submit</button>
              <div class="vr"></div>
              <button type="button" class="btn btn-outline-danger">Reset</button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_vstack_no_gap(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="vertical" %}
                <div class="p-2">First item</div>
                <div class="p-2">Second item</div>
                <div class="p-2">Third item</div>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="vstack">
              <div class="p-2">First item</div>
              <div class="p-2">Second item</div>
              <div class="p-2">Third item</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_hstack_no_gap(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="horizontal" %}
                <div class="p-2">First item</div>
                <div class="p-2">Second item</div>
                <div class="p-2">Third item</div>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <div class="hstack">
              <div class="p-2">First item</div>
              <div class="p-2">Second item</div>
              <div class="p-2">Third item</div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
