from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class TestCarousel(SimpleTestCase):
    @djc_test
    def test_basic_with_controls(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" indicators=False %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_with_indicators(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide">
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="2" aria-label="Slide 3"></button>
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_with_captions(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            {% component "CarouselCaption" %}
              <h5>First slide label</h5>
              <p>Some representative placeholder content for the first slide.</p>
            {% endcomponent %}
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            {% component "CarouselCaption" %}
              <h5>Second slide label</h5>
              <p>Some representative placeholder content for the second slide.</p>
            {% endcomponent %}
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            {% component "CarouselCaption" %}
              <h5>Third slide label</h5>
              <p>Some representative placeholder content for the third slide.</p>
            {% endcomponent %}
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide">
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="2" aria-label="Slide 3"></button>
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                  <div class="carousel-caption">
                    <h5>First slide label</h5>
                    <p>Some representative placeholder content for the first slide.</p>
                  </div>
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                  <div class="carousel-caption">
                    <h5>Second slide label</h5>
                    <p>Some representative placeholder content for the second slide.</p>
                  </div>
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                  <div class="carousel-caption">
                    <h5>Third slide label</h5>
                    <p>Some representative placeholder content for the third slide.</p>
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_crossfade(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" fade=True indicators=False %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide carousel-fade">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_autoplaying_carousel(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" ride="carousel" indicators=False %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_user_initiated_autoplay(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" ride="true" indicators=False %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide" data-bs-ride="true">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_individual_item_intervals(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" ride="carousel" indicators=False %}
          {% component "CarouselItem" active=True interval=10000 %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" interval=2000 %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active" data-bs-interval="10000">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item" data-bs-interval="2000">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_slides_only_no_controls(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" ride="carousel" controls=False indicators=False %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_disabled_touch_swiping(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" touch=False indicators=False %}
          {% component "CarouselItem" active=True %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide" data-bs-touch="false">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))

    @djc_test
    def test_dark_variant(self):
        with mock_component_id():
            template = Template("""
        {% load bootstrap5 %}
        {% component "Carousel" theme="dark" %}
          {% component "CarouselItem" active=True interval=10000 %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            {% component "CarouselCaption" %}
              <h5>First slide label</h5>
              <p>Some representative placeholder content for the first slide.</p>
            {% endcomponent %}
          {% endcomponent %}
          {% component "CarouselItem" interval=2000 %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            {% component "CarouselCaption" %}
              <h5>Second slide label</h5>
              <p>Some representative placeholder content for the second slide.</p>
            {% endcomponent %}
          {% endcomponent %}
          {% component "CarouselItem" %}
            <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
            {% component "CarouselCaption" %}
              <h5>Third slide label</h5>
              <p>Some representative placeholder content for the third slide.</p>
            {% endcomponent %}
          {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = template.render(Context())

        expected = """
            <div id="carousel-ctest01" class="carousel slide" data-bs-theme="dark">
              <div class="carousel-indicators">
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="1" aria-label="Slide 2"></button>
                <button type="button" data-bs-target="#carousel-ctest01" data-bs-slide-to="2" aria-label="Slide 3"></button>
              </div>
              <div class="carousel-inner">
                <div class="carousel-item active" data-bs-interval="10000">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                  <div class="carousel-caption">
                    <h5>First slide label</h5>
                    <p>Some representative placeholder content for the first slide.</p>
                  </div>
                </div>
                <div class="carousel-item" data-bs-interval="2000">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                  <div class="carousel-caption">
                    <h5>Second slide label</h5>
                    <p>Some representative placeholder content for the second slide.</p>
                  </div>
                </div>
                <div class="carousel-item">
                  <img src="https://placehold.net/600x400.png" class="d-block w-100" alt="Slide">
                  <div class="carousel-caption">
                    <h5>Third slide label</h5>
                    <p>Some representative placeholder content for the third slide.</p>
                  </div>
                </div>
              </div>
              <button class="carousel-control-prev" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="prev">
                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Previous</span>
              </button>
              <button class="carousel-control-next" type="button" data-bs-target="#carousel-ctest01" data-bs-slide="next">
                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                <span class="visually-hidden">Next</span>
              </button>
            </div>
        """

        self.assertHTMLEqual(normalize_html(rendered), normalize_html(expected))
