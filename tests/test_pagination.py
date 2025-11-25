from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class PaginationTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" %}
                {% component "PaginationItem" href="#" %}Previous{% endcomponent %}
                {% component "PaginationItem" href="#" %}1{% endcomponent %}
                {% component "PaginationItem" href="#" %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
                {% component "PaginationItem" href="#" %}Next{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination">
                <li class="page-item"><a class="page-link" href="#">Previous</a></li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_with_icons(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" %}
                {% component "PaginationItem" href="#" aria_label="Previous" %}
                    <span aria-hidden="true">&laquo;</span>
                {% endcomponent %}
                {% component "PaginationItem" href="#" %}1{% endcomponent %}
                {% component "PaginationItem" href="#" %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
                {% component "PaginationItem" href="#" aria_label="Next" %}
                    <span aria-hidden="true">&raquo;</span>
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination">
                <li class="page-item">
                  <a class="page-link" href="#" aria-label="Previous">
                    <span aria-hidden="true">&laquo;</span>
                  </a>
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item">
                  <a class="page-link" href="#" aria-label="Next">
                    <span aria-hidden="true">&raquo;</span>
                  </a>
                </li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_active_state(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" %}
                <li class="page-item"><a href="#" class="page-link">Previous</a></li>
                {% component "PaginationItem" href="#" %}1{% endcomponent %}
                {% component "PaginationItem" href="#" active=True %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination">
                <li class="page-item"><a href="#" class="page-link">Previous</a></li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item active">
                  <a class="page-link" href="#" aria-current="page">2</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_disabled_state(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" %}
                {% component "PaginationItem" disabled=True %}Previous{% endcomponent %}
                {% component "PaginationItem" href="#" %}1{% endcomponent %}
                {% component "PaginationItem" href="#" active=True %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
                {% component "PaginationItem" href="#" %}Next{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination">
                <li class="page-item disabled">
                  <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item active">
                  <a class="page-link" href="#" aria-current="page">2</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_large_sizing(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" size="lg" %}
                {% component "PaginationItem" active=True %}1{% endcomponent %}
                {% component "PaginationItem" href="#" %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination pagination-lg">
                <li class="page-item active">
                  <a class="page-link" href="#" aria-current="page">1</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_small_sizing(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" size="sm" %}
                {% component "PaginationItem" active=True %}1{% endcomponent %}
                {% component "PaginationItem" href="#" %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination pagination-sm">
                <li class="page-item active">
                  <a class="page-link" href="#" aria-current="page">1</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_centered_alignment(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" ul_attrs:class="justify-content-center" %}
                {% component "PaginationItem" disabled=True %}Previous{% endcomponent %}
                {% component "PaginationItem" href="#" %}1{% endcomponent %}
                {% component "PaginationItem" href="#" %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
                {% component "PaginationItem" href="#" %}Next{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination justify-content-center">
                <li class="page-item disabled">
                  <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    def test_right_alignment(self):
        template = Template("""
            {% load component_tags %}
            {% component "Pagination" ul_attrs:class="justify-content-end" %}
                {% component "PaginationItem" disabled=True %}Previous{% endcomponent %}
                {% component "PaginationItem" href="#" %}1{% endcomponent %}
                {% component "PaginationItem" href="#" %}2{% endcomponent %}
                {% component "PaginationItem" href="#" %}3{% endcomponent %}
                {% component "PaginationItem" href="#" %}Next{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = normalize_html(template.render(Context({})))

        expected = """
            <nav aria-label="Page navigation">
              <ul class="pagination justify-content-end">
                <li class="page-item disabled">
                  <a class="page-link" href="#" tabindex="-1" aria-disabled="true">Previous</a>
                </li>
                <li class="page-item"><a class="page-link" href="#">1</a></li>
                <li class="page-item"><a class="page-link" href="#">2</a></li>
                <li class="page-item"><a class="page-link" href="#">3</a></li>
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
              </ul>
            </nav>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
