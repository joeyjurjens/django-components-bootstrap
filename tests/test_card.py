from django.template import Context, Template
from django.test import SimpleTestCase

from .utils import normalize_html


class TestCard(SimpleTestCase):
    maxDiff = None

    def test_basic_with_image(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" %}
              {% bootstrap5 "CardImg" src="https://placehold.net/600x400.png" alt="Card image" position="top" / %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}Some quick example text to build on the card title and make up the bulk of the card's content.{% endbootstrap5 %}
                <a href="#" class="btn btn-primary">Go somewhere</a>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card">
              <img src="https://placehold.net/600x400.png" class="card-img-top" alt="Card image">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_with_header_and_footer(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" text_align="center" %}
              {% bootstrap5 "CardHeader" %}
                Featured
              {% endbootstrap5 %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Special title treatment{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}With supporting text below as a natural lead-in to additional content.{% endbootstrap5 %}
                <a href="#" class="btn btn-primary">Go somewhere</a>
              {% endbootstrap5 %}
              {% bootstrap5 "CardFooter" %}
                2 days ago
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card text-center">
              <div class="card-header">
                Featured
              </div>
              <div class="card-body">
                <h5 class="card-title">Special title treatment</h5>
                <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
              </div>
              <div class="card-footer">
                2 days ago
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_with_image_cap(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" %}
              {% bootstrap5 "CardImg" src="https://placehold.net/600x400.png" alt="Card image" position="top" / %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}<small class="text-body-secondary">Last updated 3 mins ago</small>{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card">
              <img src="https://placehold.net/600x400.png" class="card-img-top" alt="Card image">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_body_only(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" %}
              {% bootstrap5 "CardBody" %}
                This is some text within a card body.
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card">
              <div class="card-body">
                This is some text within a card body.
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_with_title_subtitle_links(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Card title{% endbootstrap5 %}
                {% bootstrap5 "CardSubtitle" %}Card subtitle{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}Some quick example text to build on the card title and make up the bulk of the card's content.{% endbootstrap5 %}
                <a href="#" class="card-link">Card link</a>
                <a href="#" class="card-link">Another link</a>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <h6 class="card-subtitle">Card subtitle</h6>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                <a href="#" class="card-link">Card link</a>
                <a href="#" class="card-link">Another link</a>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_with_image_bottom(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}<small class="text-body-secondary">Last updated 3 mins ago</small>{% endbootstrap5 %}
              {% endbootstrap5 %}
              {% bootstrap5 "CardImg" src="https://placehold.net/600x400.png" alt="Card image" position="bottom" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card">
              <div class="card-body">
                <h5 class="card-title">Card title</h5>
                <p class="card-text">This is a wider card with supporting text below as a natural lead-in to additional content. This content is a little bit longer.</p>
                <p class="card-text"><small class="text-body-secondary">Last updated 3 mins ago</small></p>
              </div>
              <img src="https://placehold.net/600x400.png" class="card-img-bottom" alt="Card image">
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_bg_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" bg="primary" attrs={"class": "mb-3", "style": "max-width: 18rem;"} %}
              {% bootstrap5 "CardHeader" %}Header{% endbootstrap5 %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Primary card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}Some quick example text to build on the card title and make up the bulk of the card's content.{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card text-bg-primary mb-3" style="max-width: 18rem;">
              <div class="card-header">Header</div>
              <div class="card-body">
                <h5 class="card-title">Primary card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_bg_secondary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" bg="secondary" attrs={"class": "mb-3", "style": "max-width: 18rem;"} %}
              {% bootstrap5 "CardHeader" %}Header{% endbootstrap5 %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Secondary card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}Some quick example text to build on the card title and make up the bulk of the card's content.{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card text-bg-secondary mb-3" style="max-width: 18rem;">
              <div class="card-header">Header</div>
              <div class="card-body">
                <h5 class="card-title">Secondary card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_bg_success(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" bg="success" attrs={"class": "mb-3", "style": "max-width: 18rem;"} %}
              {% bootstrap5 "CardHeader" %}Header{% endbootstrap5 %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Success card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}Some quick example text to build on the card title and make up the bulk of the card's content.{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card text-bg-success mb-3" style="max-width: 18rem;">
              <div class="card-header">Header</div>
              <div class="card-body">
                <h5 class="card-title">Success card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_bg_danger(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" bg="danger" attrs={"class": "mb-3", "style": "max-width: 18rem;"} %}
              {% bootstrap5 "CardHeader" %}Header{% endbootstrap5 %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Danger card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}Some quick example text to build on the card title and make up the bulk of the card's content.{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card text-bg-danger mb-3" style="max-width: 18rem;">
              <div class="card-header">Header</div>
              <div class="card-body">
                <h5 class="card-title">Danger card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_border_primary(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" border="primary" attrs={"class": "mb-3", "style": "max-width: 18rem;"} %}
              {% bootstrap5 "CardHeader" %}Header{% endbootstrap5 %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Primary card title{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}Some quick example text to build on the card title and make up the bulk of the card's content.{% endbootstrap5 %}
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card border-primary mb-3" style="max-width: 18rem;">
              <div class="card-header">Header</div>
              <div class="card-body">
                <h5 class="card-title">Primary card title</h5>
                <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_text_align_center(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" text_align="center" attrs={"class": "mb-3", "style": "width: 18rem;"} %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Special title treatment{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}With supporting text below as a natural lead-in to additional content.{% endbootstrap5 %}
                <a href="#" class="btn btn-primary">Go somewhere</a>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card text-center mb-3" style="width: 18rem;">
              <div class="card-body">
                <h5 class="card-title">Special title treatment</h5>
                <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    def test_text_align_end(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Card" text_align="end" %}
              {% bootstrap5 "CardBody" %}
                {% bootstrap5 "CardTitle" %}Special title treatment{% endbootstrap5 %}
                {% bootstrap5 "CardText" %}With supporting text below as a natural lead-in to additional content.{% endbootstrap5 %}
                <a href="#" class="btn btn-primary">Go somewhere</a>
              {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context())

        expected = """
            <div class="card text-end">
              <div class="card-body">
                <h5 class="card-title">Special title treatment</h5>
                <p class="card-text">With supporting text below as a natural lead-in to additional content.</p>
                <a href="#" class="btn btn-primary">Go somewhere</a>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
