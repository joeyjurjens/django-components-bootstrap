from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class PaginationTests(SimpleTestCase):
    maxDiff = None

    def test_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" %}
                {% bootstrap5 "PaginationItem" href="#" %}Previous{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}Next{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" %}
                {% bootstrap5 "PaginationItem" href="#" aria_label="Previous" %}
                    <span aria-hidden="true">&laquo;</span>
                {% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" aria_label="Next" %}
                    <span aria-hidden="true">&raquo;</span>
                {% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" %}
                <li class="page-item"><a href="#" class="page-link">Previous</a></li>
                {% bootstrap5 "PaginationItem" href="#" %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" active=True %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
                <li class="page-item"><a class="page-link" href="#">Next</a></li>
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" %}
                {% bootstrap5 "PaginationItem" disabled=True %}Previous{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" active=True %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}Next{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" size="lg" %}
                {% bootstrap5 "PaginationItem" active=True %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" size="sm" %}
                {% bootstrap5 "PaginationItem" active=True %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" ul_attrs:class="justify-content-center" %}
                {% bootstrap5 "PaginationItem" disabled=True %}Previous{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}Next{% endbootstrap5 %}
            {% endbootstrap5 %}
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
            {% load bootstrap5 %}
            {% bootstrap5 "Pagination" ul_attrs:class="justify-content-end" %}
                {% bootstrap5 "PaginationItem" disabled=True %}Previous{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}1{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}2{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}3{% endbootstrap5 %}
                {% bootstrap5 "PaginationItem" href="#" %}Next{% endbootstrap5 %}
            {% endbootstrap5 %}
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
