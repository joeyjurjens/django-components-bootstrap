from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class AccordionTests(SimpleTestCase):
    maxDiff = None

    @djc_test
    def test_basic(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Accordion" %}
                {% component "AccordionItem" default_open=True %}
                    {% component "AccordionHeader" %}Accordion Item #1{% endcomponent %}
                    {% component "AccordionBody" %}
                        <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                    {% endcomponent %}
                {% endcomponent %}
                {% component "AccordionItem" %}
                    {% component "AccordionHeader" %}Accordion Item #2{% endcomponent %}
                    {% component "AccordionBody" %}
                        <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                    {% endcomponent %}
                {% endcomponent %}
                {% component "AccordionItem" %}
                    {% component "AccordionHeader" %}Accordion Item #3{% endcomponent %}
                    {% component "AccordionBody" %}
                        <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                    {% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
            """)
            rendered = normalize_html(template.render(Context({})))

        expected = """
        <div class="accordion" id="accordion-ctest01">
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest02">
              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest02" aria-expanded="true" aria-controls="collapse-ctest02">
                Accordion Item #1
              </button>
            </h2>
            <div id="collapse-ctest02" class="accordion-collapse collapse show" aria-labelledby="heading-ctest02" data-bs-parent="#accordion-ctest01">
              <div class="accordion-body">
                <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest03">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest03" aria-expanded="false" aria-controls="collapse-ctest03">
                Accordion Item #2
              </button>
            </h2>
            <div id="collapse-ctest03" class="accordion-collapse collapse" aria-labelledby="heading-ctest03" data-bs-parent="#accordion-ctest01">
              <div class="accordion-body">
                <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest04">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest04" aria-expanded="false" aria-controls="collapse-ctest04">
                Accordion Item #3
              </button>
            </h2>
            <div id="collapse-ctest04" class="accordion-collapse collapse" aria-labelledby="heading-ctest04" data-bs-parent="#accordion-ctest01">
              <div class="accordion-body">
                <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
              </div>
            </div>
          </div>
        </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    @djc_test
    def test_with_icon_in_header(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Accordion" %}
                {% component "AccordionItem" default_open=True %}
                    {% component "AccordionHeader" %}
                        <i class="bi bi-info-circle"></i> Accordion Item with Icon
                    {% endcomponent %}
                    {% component "AccordionBody" %}
                        This accordion item has an icon in the header.
                    {% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = normalize_html(template.render(Context({})))

        self.assertIn('<i class="bi bi-info-circle"></i>', rendered)
        self.assertIn("Accordion Item with Icon", rendered)

    @djc_test
    def test_with_badge_in_header(self):
        with mock_component_id():
            template = Template("""
            {% load component_tags %}
            {% component "Accordion" %}
                {% component "AccordionItem" default_open=True %}
                    {% component "AccordionHeader" %}
                        Accordion Item <span class="badge bg-primary">New</span>
                    {% endcomponent %}
                    {% component "AccordionBody" %}
                        This accordion item has a badge in the header.
                    {% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
            rendered = normalize_html(template.render(Context({})))

        self.assertIn('<span class="badge bg-primary">New</span>', rendered)
        self.assertIn("Accordion Item", rendered)

    @djc_test
    def test_flush(self):
        with mock_component_id():
            template = Template("""
        {% load component_tags %}
        {% component "Accordion" flush=True %}
            {% component "AccordionItem" %}
                {% component "AccordionHeader" %}Accordion Item #1{% endcomponent %}
                {% component "AccordionBody" %}
                    Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the first item's accordion body.
                {% endcomponent %}
            {% endcomponent %}
            {% component "AccordionItem" %}
                {% component "AccordionHeader" %}Accordion Item #2{% endcomponent %}
                {% component "AccordionBody" %}
                    Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the second item's accordion body. Let's imagine this being filled with some actual content.
                {% endcomponent %}
            {% endcomponent %}
            {% component "AccordionItem" %}
                {% component "AccordionHeader" %}Accordion Item #3{% endcomponent %}
                {% component "AccordionBody" %}
                    Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.
                {% endcomponent %}
            {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = normalize_html(template.render(Context({})))

        expected = """
        <div class="accordion accordion-flush" id="accordion-ctest01">
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest02">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest02" aria-expanded="false" aria-controls="collapse-ctest02">
                Accordion Item #1
              </button>
            </h2>
            <div id="collapse-ctest02" class="accordion-collapse collapse" aria-labelledby="heading-ctest02" data-bs-parent="#accordion-ctest01">
              <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the first item's accordion body.</div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest03">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest03" aria-expanded="false" aria-controls="collapse-ctest03">
                Accordion Item #2
              </button>
            </h2>
            <div id="collapse-ctest03" class="accordion-collapse collapse" aria-labelledby="heading-ctest03" data-bs-parent="#accordion-ctest01">
              <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the second item's accordion body. Let's imagine this being filled with some actual content.</div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest04">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest04" aria-expanded="false" aria-controls="collapse-ctest04">
                Accordion Item #3
              </button>
            </h2>
            <div id="collapse-ctest04" class="accordion-collapse collapse" aria-labelledby="heading-ctest04" data-bs-parent="#accordion-ctest01">
              <div class="accordion-body">Placeholder content for this accordion, which is intended to demonstrate the <code>.accordion-flush</code> class. This is the third item's accordion body. Nothing more exciting happening here in terms of content, but just filling up the space to make it look, at least at first glance, a bit more representative of how this would look in a real-world application.</div>
            </div>
          </div>
        </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)

    @djc_test
    def test_always_open(self):
        with mock_component_id():
            template = Template("""
        {% load component_tags %}
        {% component "Accordion" always_open=True %}
            {% component "AccordionItem" default_open=True %}
                {% component "AccordionHeader" %}Accordion Item #1{% endcomponent %}
                {% component "AccordionBody" %}
                    <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                {% endcomponent %}
            {% endcomponent %}
            {% component "AccordionItem" %}
                {% component "AccordionHeader" %}Accordion Item #2{% endcomponent %}
                {% component "AccordionBody" %}
                    <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                {% endcomponent %}
            {% endcomponent %}
            {% component "AccordionItem" %}
                {% component "AccordionHeader" %}Accordion Item #3{% endcomponent %}
                {% component "AccordionBody" %}
                    <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
                {% endcomponent %}
            {% endcomponent %}
        {% endcomponent %}
        """)
            rendered = normalize_html(template.render(Context({})))

        expected = """
        <div class="accordion" id="accordion-ctest01">
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest02">
              <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest02" aria-expanded="true" aria-controls="collapse-ctest02">
                Accordion Item #1
              </button>
            </h2>
            <div id="collapse-ctest02" class="accordion-collapse collapse show" aria-labelledby="heading-ctest02">
              <div class="accordion-body">
                <strong>This is the first item's accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest03">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest03" aria-expanded="false" aria-controls="collapse-ctest03">
                Accordion Item #2
              </button>
            </h2>
            <div id="collapse-ctest03" class="accordion-collapse collapse" aria-labelledby="heading-ctest03">
              <div class="accordion-body">
                <strong>This is the second item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
              </div>
            </div>
          </div>
          <div class="accordion-item">
            <h2 class="accordion-header" id="heading-ctest04">
              <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse-ctest04" aria-expanded="false" aria-controls="collapse-ctest04">
                Accordion Item #3
              </button>
            </h2>
            <div id="collapse-ctest04" class="accordion-collapse collapse" aria-labelledby="heading-ctest04">
              <div class="accordion-body">
                <strong>This is the third item's accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It's also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
              </div>
            </div>
          </div>
        </div>
        """

        self.assertHTMLEqual(normalize_html(expected), rendered)
