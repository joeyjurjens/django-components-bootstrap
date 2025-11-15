import pytest
from django.template import Context, Template
from django_components.testing import djc_test


@djc_test
class TestComponents:
    def test_accordion(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Accordion" flush=True attrs:id="myAccordion" %}
                {% component "AccordionItem" default_open=True %}
                    {% component "AccordionHeader" %}Item 1{% endcomponent %}
                    {% component "AccordionBody" %}Content 1{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "accordion" in rendered
        assert "accordion-flush" in rendered
        assert 'id="myAccordion"' in rendered
        assert "Item 1" in rendered
        assert "Content 1" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Accordion" attrs:data-test="accordion-attrs" attrs:id="custom-accordion" %}
                {% component "AccordionItem" %}
                    {% component "AccordionHeader" %}Test{% endcomponent %}
                    {% component "AccordionBody" %}Body{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "accordion" in rendered
        assert 'data-test="accordion-attrs"' in rendered
        assert 'id="custom-accordion"' in rendered
        assert "Test" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Accordion" attrs:class="custom-accordion-class extra-class" attrs:data-merged="test" %}
                {% component "AccordionItem" %}
                    {% component "AccordionHeader" %}Test{% endcomponent %}
                    {% component "AccordionBody" %}Body{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "accordion" in rendered
        assert "custom-accordion-class" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Accordion" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "AccordionItem" %}
                    {% component "AccordionHeader" %}Test{% endcomponent %}
                    {% component "AccordionBody" %}Body{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "accordion" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_alert(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Alert" variant="warning" dismissible=True close_label="Dismiss" %}
                {% component "AlertHeading" %}Warning!{% endcomponent %}
                Check out this {% component "AlertLink" href="#info" %}important link{% endcomponent %}.
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "alert" in rendered
        assert "alert-warning" in rendered
        assert "alert-dismissible" in rendered
        assert 'aria-label="Dismiss"' in rendered
        assert "Warning!" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Alert" variant="info" attrs:data-test="alert-attrs" attrs:id="custom-alert" %}
                Info message
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "alert" in rendered
        assert "alert-info" in rendered
        assert 'data-test="alert-attrs"' in rendered
        assert 'id="custom-alert"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Alert" variant="success" attrs:class="custom-alert-class extra-class" attrs:data-merged="test" %}
                Success message
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "alert" in rendered
        assert "alert-success" in rendered
        assert "custom-alert-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Alert" variant="danger" attrs:class="custom-inline" attrs:data-inline="value" %}
                Danger alert
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "alert" in rendered
        assert "alert-danger" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_badge(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Badge" bg="danger" pill=True %}Default{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "badge" in rendered
        assert "text-bg-danger" in rendered
        assert "rounded-pill" in rendered
        assert "Default" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Badge" bg="primary" text="danger" %}Custom Colors{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "badge" in rendered
        assert "bg-primary" in rendered
        assert "text-danger" in rendered
        assert "Custom Colors" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Badge" bg="primary" attrs:data-test="badge-attrs" attrs:id="custom-badge" %}Badge{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "badge" in rendered
        assert "text-bg-primary" in rendered
        assert 'data-test="badge-attrs"' in rendered
        assert 'id="custom-badge"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Badge" bg="primary" attrs:class="custom-class extra-class" attrs:data-merged="test" %}Badge{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "badge" in rendered
        assert "custom-class" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Badge" bg="primary" attrs:class="custom-inline" attrs:data-inline="value" %}Badge{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "badge" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_breadcrumb(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Breadcrumb" %}
                {% component "BreadcrumbItem" href="#" %}Home{% endcomponent %}
                {% component "BreadcrumbItem" href="#" %}Library{% endcomponent %}
                {% component "BreadcrumbItem" active=True %}Data{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "breadcrumb" in rendered
        assert "breadcrumb-item" in rendered
        assert "active" in rendered
        assert "Home" in rendered
        assert "Data" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Breadcrumb" attrs:data-test="breadcrumb-attrs" attrs:id="custom-breadcrumb" %}
                {% component "BreadcrumbItem" %}Home{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "breadcrumb" in rendered
        assert 'data-test="breadcrumb-attrs"' in rendered
        assert 'id="custom-breadcrumb"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Breadcrumb" attrs:class="custom-breadcrumb-class extra-class" attrs:data-merged="test" %}
                {% component "BreadcrumbItem" %}Home{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "breadcrumb" in rendered
        assert "custom-breadcrumb-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Breadcrumb" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "BreadcrumbItem" %}Home{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "breadcrumb" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_button(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" size="lg" active=True %}Primary Large{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "btn-primary" in rendered
        assert "btn-lg" in rendered
        assert "active" in rendered
        assert "Primary Large" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="outline-primary" %}Outline{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "btn-outline-primary" in rendered
        assert "Outline" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="link" %}Link Button{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "btn-link" in rendered
        assert "Link Button" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="link" disabled=True %}Disabled Link{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "btn-link" in rendered
        assert "Disabled Link" in rendered
        assert 'tabindex="-1"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" as_="span" %}Span Button{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "Span Button" in rendered
        assert "<span" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" type="submit" disabled=True %}Submit{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert 'type="submit"' in rendered
        assert "disabled" in rendered
        assert "Submit" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" attrs:data-test="button-attrs" attrs:id="custom-button" %}Button{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert 'data-test="button-attrs"' in rendered
        assert 'id="custom-button"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="success" attrs:class="custom-button-class extra-class" attrs:data-merged="test" %}Success{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "btn-success" in rendered
        assert "custom-button-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" attrs:class="custom-inline" attrs:data-inline="value" %}Button{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" href="/test" %}Link Button{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "<a" in rendered
        assert 'href="/test"' in rendered
        assert "btn-primary" in rendered
        assert 'role="button"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" variant="primary" outline=True %}Outline{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-outline-primary" in rendered
        assert "Outline" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Button" disabled=True %}Disabled{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "disabled" in rendered
        assert "<button" in rendered

    def test_button_group(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ButtonGroup" size="sm" aria_label="Actions" %}
                {% component "Button" %}Left{% endcomponent %}
                {% component "Button" %}Right{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-group" in rendered
        assert "btn-group-sm" in rendered
        assert 'aria-label="Actions"' in rendered
        assert "Left" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ButtonToolbar" aria_label="Toolbar" %}
                {% component "ButtonGroup" %}
                    {% component "Button" %}1{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-toolbar" in rendered
        assert 'aria-label="Toolbar"' in rendered
        assert "btn-group" in rendered
        assert "1" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ButtonGroup" attrs:data-test="group-attrs" attrs:id="custom-group" %}
                {% component "Button" %}Button{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-group" in rendered
        assert 'data-test="group-attrs"' in rendered
        assert 'id="custom-group"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ButtonGroup" attrs:class="custom-group-class extra-class" attrs:data-merged="test" %}
                {% component "Button" %}Button{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-group" in rendered
        assert "custom-group-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ButtonGroup" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "Button" %}Button{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-group" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_card(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Card" border="primary" text_align="center" %}
                Card content
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card" in rendered
        assert "border-primary" in rendered
        assert "text-center" in rendered
        assert "Card content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Card" bg="success" %}
                {% component "CardHeader" %}Header{% endcomponent %}
                {% component "CardImg" position="top" src="test.jpg" %}{% endcomponent %}
                {% component "CardBody" %}
                    {% component "CardTitle" as_="h3" %}Title{% endcomponent %}
                    {% component "CardSubtitle" %}Subtitle{% endcomponent %}
                    {% component "CardText" %}Text content{% endcomponent %}
                    {% component "CardLink" href="#" %}Link{% endcomponent %}
                {% endcomponent %}
                {% component "CardImg" position="bottom" src="test2.jpg" %}{% endcomponent %}
                {% component "CardFooter" %}Footer{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card" in rendered
        assert "text-bg-success" in rendered
        assert "card-header" in rendered
        assert 'src="test.jpg"' in rendered
        assert "Title" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "CardGroup" %}
                {% component "Card" %}
                    {% component "CardImgOverlay" %}Overlay{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card-group" in rendered
        assert "card" in rendered
        assert "card-img-overlay" in rendered
        assert "Overlay" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Card" bg="info" text="dark" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card" in rendered
        assert "bg-info" in rendered
        assert "text-dark" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Card" attrs:data-test="card-attrs" attrs:id="custom-card" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card" in rendered
        assert 'data-test="card-attrs"' in rendered
        assert 'id="custom-card"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Card" bg="warning" attrs:class="custom-card-class extra-class" attrs:data-merged="test" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card" in rendered
        assert "text-bg-warning" in rendered
        assert "custom-card-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Card" attrs:class="custom-inline" attrs:data-inline="value" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Card" %}
                {% component "CardImg" src="test.jpg" alt="Test" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "card-img" in rendered
        assert "card-img-top" not in rendered
        assert "card-img-bottom" not in rendered
        assert 'src="test.jpg"' in rendered

    def test_carousel(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Carousel" ride=True interval=3000 fade=True theme="dark" controls=True indicators=True attrs:id="myCarousel" %}
                {% component "CarouselItem" active=True %}
                    <img src="img1.jpg" class="d-block w-100" alt="First">
                    {% component "CarouselCaption" %}
                        <h5>First slide</h5>
                    {% endcomponent %}
                {% endcomponent %}
                {% component "CarouselItem" %}
                    <img src="img2.jpg" class="d-block w-100" alt="Second">
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "carousel" in rendered
        assert "carousel-fade" in rendered
        assert 'data-bs-ride="carousel"' in rendered
        assert 'data-bs-interval="3000"' in rendered
        assert 'id="myCarousel"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Carousel" attrs:data-test="carousel-attrs" attrs:id="custom-carousel" %}
                {% component "CarouselItem" %}Image{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "carousel" in rendered
        assert 'data-test="carousel-attrs"' in rendered
        assert 'id="custom-carousel"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Carousel" attrs:class="custom-carousel-class extra-class" attrs:data-merged="test" %}
                {% component "CarouselItem" %}Image{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "carousel" in rendered
        assert "custom-carousel-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Carousel" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "CarouselItem" %}Image{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "carousel" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Carousel" %}
                {% component "CarouselItem" active=True %}
                    <img src="img1.jpg" alt="First">
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "carousel" in rendered
        assert "carousel-indicators" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% provide "carousel" carousel_id="test-carousel" %}
                {% component "CarouselIndicator" slide_to=0 active=True %}{% endcomponent %}
            {% endprovide %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-slide-to="0"' in rendered
        assert 'aria-current="true"' in rendered
        assert "active" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% provide "carousel" carousel_id="test-carousel" %}
                {% component "CarouselIndicator" slide_to=2 aria_label="Third slide" %}{% endcomponent %}
            {% endprovide %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-slide-to="2"' in rendered
        assert 'aria-label="Third slide"' in rendered

    def test_close_button(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "CloseButton" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-close" in rendered
        assert 'type="button"' in rendered
        assert 'aria-label="Close"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "CloseButton" variant="white" disabled=True aria_label="Dismiss" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-close" in rendered
        assert "btn-close-white" in rendered
        assert "disabled" in rendered
        assert 'aria-label="Dismiss"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "CloseButton" attrs:data-test="close" attrs:id="my-close" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-close" in rendered
        assert 'data-test="close"' in rendered
        assert 'id="my-close"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "CloseButton" attrs:class="custom-close extra-class" attrs:data-merged="test" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-close" in rendered
        assert "custom-close" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

    def test_collapse(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" %}
                {% fill "default" %}
                    {% component "CollapseToggle" %}Toggle{% endcomponent %}
                    Content
                {% endfill %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "collapse" in rendered
        assert 'data-bs-toggle="collapse"' in rendered
        assert "Content" in rendered
        assert "Toggle" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" horizontal=True show=True %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "collapse" in rendered
        assert "collapse-horizontal" in rendered
        assert "show" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" %}
                {% fill "default" %}
                    {% component "CollapseToggle" as_="a" expanded=True %}Link{% endcomponent %}
                {% endfill %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="collapse"' in rendered
        assert 'aria-expanded="true"' in rendered
        assert "<a" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" attrs:data-test="collapse-attrs" attrs:id="custom-collapse" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "collapse" in rendered
        assert 'data-test="collapse-attrs"' in rendered
        assert 'id="custom-collapse"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" attrs:class="custom-collapse-class extra-class" attrs:data-merged="test" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "collapse" in rendered
        assert "custom-collapse-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Collapse" attrs:class="custom-inline" attrs:data-inline="value" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "collapse" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_dropdown(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" direction="up" centered=True auto_close="outside" %}
                {% component "DropdownToggle" %}Actions{% endcomponent %}
                {% component "DropdownMenu" dark=True align="end" align_lg="start" %}
                    {% component "DropdownHeader" %}Header{% endcomponent %}
                    {% component "DropdownItem" active=True %}Active{% endcomponent %}
                    {% component "DropdownItem" disabled=True %}Disabled{% endcomponent %}
                    {% component "DropdownDivider" / %}
                    {% component "DropdownItemText" %}Text{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropup" in rendered
        assert "dropup-center" in rendered
        assert 'data-bs-auto-close="outside"' in rendered
        assert "dropdown-menu-dark" in rendered
        assert "Active" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" direction="end" %}
                {% component "DropdownToggle" %}End{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropend" in rendered
        assert "End" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" direction="start" %}
                {% component "DropdownToggle" %}Start{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropstart" in rendered
        assert "Start" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
                {% component "Button" variant="secondary" size="sm" %}Action{% endcomponent %}
                {% component "DropdownToggle" split=True variant="secondary" size="sm" %}{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-secondary" in rendered
        assert "btn-sm" in rendered
        assert "dropdown-toggle-split" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" centered=True %}
                {% component "DropdownToggle" %}Centered{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown-center" in rendered
        assert "Centered" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" direction="up" %}
                {% component "DropdownToggle" %}Up{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropup" in rendered
        assert "Up" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" attrs:data-test="dropdown-attrs" attrs:id="custom-dropdown" %}
                {% component "DropdownToggle" %}Toggle{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown" in rendered
        assert 'data-test="dropdown-attrs"' in rendered
        assert 'id="custom-dropdown"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" attrs:class="custom-dropdown-class extra-class" attrs:data-merged="test" %}
                {% component "DropdownToggle" %}Toggle{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown" in rendered
        assert "custom-dropdown-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "DropdownToggle" %}Toggle{% endcomponent %}
                {% component "DropdownMenu" %}Items{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
                {% component "DropdownToggle" %}Actions{% endcomponent %}
                {% component "DropdownMenu" align_responsive={"md": "end", "lg": "start"} %}
                    {% component "DropdownItem" %}Item{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown-menu-md-end" in rendered
        assert "dropdown-menu-lg-start" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
                {% component "DropdownToggle" %}Actions{% endcomponent %}
                {% component "DropdownMenu" align_sm="end" %}
                    {% component "DropdownItem" %}Item{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown-menu-sm-end" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
                {% component "DropdownToggle" %}Actions{% endcomponent %}
                {% component "DropdownMenu" align_md="start" %}
                    {% component "DropdownItem" %}Item{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown-menu-md-start" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
                {% component "DropdownToggle" %}Actions{% endcomponent %}
                {% component "DropdownMenu" align_xl="end" %}
                    {% component "DropdownItem" %}Item{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown-menu-xl-end" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
                {% component "DropdownToggle" %}Actions{% endcomponent %}
                {% component "DropdownMenu" align_xxl="start" %}
                    {% component "DropdownItem" %}Item{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown-menu-xxl-start" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Dropdown" %}
                {% component "DropdownToggle" %}Actions{% endcomponent %}
                {% component "DropdownMenu" %}
                    {% component "DropdownItem" as_="button" disabled=True %}Disabled Button{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "<button" in rendered
        assert "disabled" in rendered
        assert "Disabled Button" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "DropdownButton" title="Actions" %}
                {% component "DropdownItem" %}Action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "dropdown" in rendered
        assert "Actions" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "SplitButton" title="Split" %}
                {% component "DropdownItem" %}Action{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-group" in rendered
        assert "Split" in rendered

    def test_figure(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Figure" %}
                {% component "FigureImage" src="photo.jpg" alt="Photo" %}{% endcomponent %}
                {% component "FigureCaption" %}A caption{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "figure" in rendered
        assert "figure-img" in rendered
        assert "img-fluid" in rendered
        assert 'src="photo.jpg"' in rendered
        assert "figure-caption" in rendered
        assert "A caption" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Figure" attrs:data-test="figure" %}
                {% component "FigureImage" src="test.jpg" fluid=False %}{% endcomponent %}
                {% component "FigureCaption" %}Caption text{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "figure" in rendered
        assert "figure-img" in rendered
        assert 'src="test.jpg"' in rendered
        assert 'data-test="figure"' in rendered
        assert "Caption text" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Figure" attrs:class="custom-figure extra-class" attrs:data-merged="test" %}
                {% component "FigureImage" src="img.jpg" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "figure" in rendered
        assert "custom-figure" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FigureCaption" attrs:data-test="caption" %}Caption{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "figure-caption" in rendered
        assert 'data-test="caption"' in rendered
        assert "Caption" in rendered

    def test_form(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Form" validated=True %}
                {% component "FormLabel" for_="email" %}Email{% endcomponent %}
                {% component "FormControl" type="email" is_valid=True attrs:id="email" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "was-validated" in rendered
        assert "form-label" in rendered
        assert "form-control" in rendered
        assert 'type="email"' in rendered
        assert "is-valid" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormControl" is_invalid=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control" in rendered
        assert "is-invalid" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormControl" type="file" size="lg" readonly=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control" in rendered
        assert "form-control-lg" in rendered
        assert 'type="file"' in rendered
        assert "readonly" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormControl" disabled=True readonly=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control" in rendered
        assert "disabled" in rendered
        assert "readonly" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormControl" plaintext=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control-plaintext" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormControl" type="color" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control" in rendered
        assert "form-control-color" in rendered
        assert 'type="color"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormTextarea" size="lg" disabled=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control" in rendered
        assert "form-control-lg" in rendered
        assert "disabled" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormTextarea" readonly=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control" in rendered
        assert "readonly" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormSelect" is_invalid=True %}
                <option>Option</option>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-select" in rendered
        assert "is-invalid" in rendered
        assert "Option" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormSelect" size="sm" disabled=True is_valid=True html_size=3 %}
                <option>1</option>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-select" in rendered
        assert "form-select-sm" in rendered
        assert "is-valid" in rendered
        assert "disabled" in rendered
        assert 'size="3"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormCheck" type="switch" reverse=True is_valid=True %}
                {% component "FormCheckInput" %}{% endcomponent %}
                {% component "FormCheckLabel" %}Switch{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-check" in rendered
        assert "form-switch" in rendered
        assert "form-check-reverse" in rendered
        assert "is-valid" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormCheck" inline=True is_invalid=True disabled=True %}
                {% component "FormCheckInput" %}{% endcomponent %}
                {% component "FormCheckLabel" %}Checkbox{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-check" in rendered
        assert "form-check-inline" in rendered
        assert "is-invalid" in rendered
        assert "disabled" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormCheck" %}Checkbox{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-check" in rendered
        assert "Checkbox" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormText" %}Helper text{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-text" in rendered
        assert "Helper text" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Form" attrs:data-test="form-attrs" attrs:id="custom-form" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-test="form-attrs"' in rendered
        assert 'id="custom-form"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Form" validated=True attrs:class="custom-form-class extra-class" attrs:data-merged="test" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "was-validated" in rendered
        assert "custom-form-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Form" attrs:class="custom-inline" attrs:data-inline="value" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormGroup" control_id="test-input" %}
                {% component "FormLabel" %}Label{% endcomponent %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-label" in rendered
        assert 'for="test-input"' in rendered
        assert 'id="test-input"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormGroup" control_id="grouped-input" %}
                {% component "FormLabel" %}Grouped Label{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-label" in rendered
        assert 'for="grouped-input"' in rendered
        assert "Grouped Label" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormLabel" for_="myinput" %}Label{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-label" in rendered
        assert 'for="myinput"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormControl" id="standalone" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-control" in rendered
        assert 'id="standalone"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormCheckInput" id="checked-input" checked=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-check-input" in rendered
        assert "checked" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormCheckInput" id="standalone-check" type="checkbox" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-check-input" in rendered
        assert 'type="checkbox"' in rendered
        assert 'id="standalone-check"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormCheckLabel" for_="standalone-check" %}Label{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-check-label" in rendered
        assert 'for="standalone-check"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormCheck" label="Check me" id="check1" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-check" in rendered
        assert "Check me" in rendered

    def test_form_range(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "FormRange" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-range" in rendered
        assert 'type="range"' in rendered
        assert 'min="0"' in rendered
        assert 'max="100"' in rendered
        assert 'step="1"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormRange" min=0 max=10 step=0.5 value=5 %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-range" in rendered
        assert 'min="0"' in rendered
        assert 'max="10"' in rendered
        assert 'step="0.5"' in rendered
        assert 'value="5"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormRange" id="customRange" name="volume" disabled=True attrs:data-test="range" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-range" in rendered
        assert 'id="customRange"' in rendered
        assert 'name="volume"' in rendered
        assert "disabled" in rendered
        assert 'data-test="range"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FormRange" attrs:class="custom-range extra-class" attrs:data-merged="test" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-range" in rendered
        assert "custom-range" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

    def test_image(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Image" src="photo.jpg" alt="My Photo" fluid=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'src="photo.jpg"' in rendered
        assert 'alt="My Photo"' in rendered
        assert "img-fluid" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Image" src="test.jpg" fluid=True rounded=True thumbnail=True %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'src="test.jpg"' in rendered
        assert "img-fluid" in rendered
        assert "rounded" in rendered
        assert "img-thumbnail" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Image" src="avatar.jpg" rounded_circle=True attrs:data-test="image" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'src="avatar.jpg"' in rendered
        assert "rounded-circle" in rendered
        assert 'data-test="image"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Image" src="pic.jpg" rounded=True attrs:class="custom-image extra-class" attrs:data-merged="test" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'src="pic.jpg"' in rendered
        assert "rounded" in rendered
        assert "custom-image" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

    def test_input_group(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "InputGroup" size="lg" nowrap=True %}
                {% component "InputGroupText" %}@{% endcomponent %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "input-group" in rendered
        assert "input-group-lg" in rendered
        assert "flex-nowrap" in rendered
        assert "input-group-text" in rendered
        assert "@" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "FloatingLabel" label="Email" %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "form-floating" in rendered
        assert "Email" in rendered
        assert "form-control" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "InputGroup" attrs:data-test="input-group-attrs" attrs:id="custom-input-group" %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "input-group" in rendered
        assert 'data-test="input-group-attrs"' in rendered
        assert 'id="custom-input-group"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "InputGroup" size="sm" attrs:class="custom-input-group-class extra-class" attrs:data-merged="test" %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "input-group" in rendered
        assert "input-group-sm" in rendered
        assert "custom-input-group-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "InputGroup" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "input-group" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "InputGroup" %}
                {% component "InputGroupRadio" %}{% endcomponent %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "input-group" in rendered
        assert "input-group-text" in rendered
        assert 'type="radio"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "InputGroup" %}
                {% component "InputGroupCheckbox" %}{% endcomponent %}
                {% component "FormControl" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "input-group" in rendered
        assert "input-group-text" in rendered
        assert 'type="checkbox"' in rendered

    def test_layout(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Container" fluid="md" as_="section" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "container-md" in rendered
        assert "Content" in rendered
        assert "<section" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Row" gutter=5 gutter_x=2 gutter_y=3 cols=2 cols_sm=3 cols_md=4 cols_lg=5 cols_xl=6 cols_xxl=7 %}
                Content
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "row" in rendered
        assert "g-5" in rendered
        assert "gx-2" in rendered
        assert "gy-3" in rendered
        assert "row-cols-2" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Col" as_="article" col=12 sm=6 md=4 lg=3 xl=2 xxl=1 %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "col-12" in rendered
        assert "col-sm-6" in rendered
        assert "col-md-4" in rendered
        assert "<article" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Col" col="auto" sm="auto" md="auto" lg="auto" xl="auto" xxl="auto" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "col-auto" in rendered
        assert "col-sm-auto" in rendered
        assert "col-md-auto" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Col" auto=True %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "col-auto" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Container" fluid=True %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "container-fluid" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Container" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "container" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Container" attrs:data-test="container-attrs" attrs:id="custom-container" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "container" in rendered
        assert 'data-test="container-attrs"' in rendered
        assert 'id="custom-container"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Container" fluid="lg" attrs:class="custom-container-class extra-class" attrs:data-merged="test" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "container-lg" in rendered
        assert "custom-container-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Container" attrs:class="custom-inline" attrs:data-inline="value" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "container" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Col" %}Default{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'class="col"' in rendered
        assert "Default" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Col" xs=6 %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "col-6" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Col" xs="auto" %}Auto Col{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "col-auto" in rendered
        assert "Auto Col" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Col" col="auto" %}Auto{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "col-auto" in rendered
        assert "Auto" in rendered

    def test_list_group(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" flush=True numbered=True horizontal="md" %}
                {% component "ListGroupItem" as_="a" href="#" action=True variant="danger" active=True %}Item 1{% endcomponent %}
                {% component "ListGroupItem" as_="button" disabled=True %}Item 2{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "list-group" in rendered
        assert "list-group-flush" in rendered
        assert "list-group-numbered" in rendered
        assert "list-group-horizontal-md" in rendered
        assert "list-group-item-danger" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" horizontal=True %}
                {% component "ListGroupItem" %}Item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "list-group" in rendered
        assert "list-group-horizontal" in rendered
        assert "Item" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" attrs:data-test="list-group-attrs" attrs:id="custom-list-group" %}
                {% component "ListGroupItem" %}Item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "list-group" in rendered
        assert 'data-test="list-group-attrs"' in rendered
        assert 'id="custom-list-group"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" flush=True attrs:class="custom-list-group-class extra-class" attrs:data-merged="test" %}
                {% component "ListGroupItem" %}Item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "list-group" in rendered
        assert "list-group-flush" in rendered
        assert "custom-list-group-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ListGroup" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "ListGroupItem" %}Item{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "list-group" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_modal(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Modal" %}
                {% fill "default" %}
                    {% component "ModalToggle" %}Open Modal{% endcomponent %}
                {% endfill %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="modal"' in rendered
        assert "Open Modal" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Modal" size="lg" fullscreen="md-down" centered=True scrollable=True dialog_class="my-dialog" content_class="my-content" attrs:id="myModal" %}
                {% component "ModalHeader" %}
                    {% component "ModalTitle" %}Title{% endcomponent %}
                {% endcomponent %}
                {% component "ModalBody" %}Body content{% endcomponent %}
                {% component "ModalFooter" %}Footer content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "modal" in rendered
        assert "modal-lg" in rendered
        assert "modal-fullscreen-md-down" in rendered
        assert "modal-dialog-centered" in rendered
        assert "my-dialog" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Modal" fullscreen=True %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "modal" in rendered
        assert "modal-fullscreen" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Modal" %}
                {% fill "default" %}
                    {% component "ModalToggle" as_="a" %}Link{% endcomponent %}
                {% endfill %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="modal"' in rendered
        assert "<a" in rendered
        assert "<a" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Modal" attrs:data-test="modal-attrs" attrs:id="custom-modal" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "modal" in rendered
        assert 'data-test="modal-attrs"' in rendered
        assert 'id="custom-modal"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Modal" attrs:class="custom-modal-class extra-class" attrs:data-merged="test" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "modal" in rendered
        assert "custom-modal-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Modal" attrs:class="custom-inline" attrs:data-inline="value" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "modal" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_nav(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" variant="pills" fill=True justified=True vertical=True role="navigation" %}
                {% component "NavItem" %}
                    {% component "NavLink" active=True href="#" %}Active{% endcomponent %}
                {% endcomponent %}
                {% component "NavItem" %}
                    {% component "NavLink" disabled=True href="#" %}Disabled{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav" in rendered
        assert "nav-pills" in rendered
        assert "nav-fill" in rendered
        assert "nav-justified" in rendered
        assert "flex-column" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" variant="tabs" %}
                {% component "NavItem" %}
                    {% component "NavLink" %}Link{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav" in rendered
        assert "nav-tabs" in rendered
        assert "Link" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" variant="underline" %}
                {% component "NavItem" %}
                    {% component "NavLink" %}Link{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav" in rendered
        assert "nav-underline" in rendered
        assert "Link" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" attrs:data-test="nav-attrs" attrs:id="custom-nav" %}
                {% component "NavItem" %}
                    {% component "NavLink" %}Link{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav" in rendered
        assert 'data-test="nav-attrs"' in rendered
        assert 'id="custom-nav"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" variant="pills" attrs:class="custom-nav-class extra-class" attrs:data-merged="test" %}
                {% component "NavItem" %}
                    {% component "NavLink" %}Link{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav" in rendered
        assert "nav-pills" in rendered
        assert "custom-nav-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "NavItem" %}
                    {% component "NavLink" %}Link{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Nav" %}
                {% component "NavDropdown" title="Dropdown" %}
                    {% component "DropdownItem" %}Action{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav-item" in rendered
        assert "dropdown-toggle" in rendered
        assert "Dropdown" in rendered

    def test_navbar(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Navbar" expand="md" bg="light" variant="dark" placement="fixed-top" container=True %}
                {% component "NavbarBrand" href="#" %}Brand{% endcomponent %}
                {% component "NavbarToggler" %}{% endcomponent %}
                {% component "NavbarCollapse" attrs:id="navbarNav" %}
                    {% component "NavbarNav" scroll=True %}
                        {% component "NavItem" %}
                            {% component "NavLink" %}Link{% endcomponent %}
                        {% endcomponent %}
                    {% endcomponent %}
                    {% component "NavbarText" %}Text{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "navbar" in rendered
        assert "navbar-expand-md" in rendered
        assert "bg-light" in rendered
        assert "fixed-top" in rendered
        assert 'data-bs-theme="dark"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Navbar" container="sm" %}
                {% component "NavbarBrand" as_="span" %}Brand{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "navbar" in rendered
        assert "container-sm" in rendered
        assert "<span" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Navbar" container="fluid" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "navbar" in rendered
        assert "container-fluid" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Navbar" attrs:data-test="navbar-attrs" attrs:id="custom-navbar" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "navbar" in rendered
        assert 'data-test="navbar-attrs"' in rendered
        assert 'id="custom-navbar"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Navbar" bg="dark" attrs:class="custom-navbar-class extra-class" attrs:data-merged="test" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "navbar" in rendered
        assert "bg-dark" in rendered
        assert "custom-navbar-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Navbar" attrs:class="custom-inline" attrs:data-inline="value" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "navbar" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_offcanvas(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Offcanvas" placement="end" responsive="lg" scroll=True keyboard=False attrs:id="myOffcanvas" %}
                {% component "OffcanvasHeader" %}
                    {% component "OffcanvasTitle" %}Title{% endcomponent %}
                {% endcomponent %}
                {% component "OffcanvasBody" %}Body content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "offcanvas" in rendered
        assert "offcanvas-end" in rendered
        assert "offcanvas-lg" in rendered
        assert 'data-bs-scroll="true"' in rendered
        assert 'data-bs-keyboard="false"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Offcanvas" placement="start" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "offcanvas" in rendered
        assert "offcanvas-start" in rendered
        assert "Content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Offcanvas" %}
                {% fill "default" %}
                    {% component "OffcanvasToggle" %}Toggle{% endcomponent %}
                {% endfill %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="offcanvas"' in rendered
        assert "Toggle" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Offcanvas" %}
                {% fill "default" %}
                    {% component "OffcanvasToggle" as_="a" %}Link{% endcomponent %}
                {% endfill %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="offcanvas"' in rendered
        assert "<a" in rendered
        assert "<a" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Offcanvas" attrs:data-test="offcanvas-attrs" attrs:id="custom-offcanvas" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "offcanvas" in rendered
        assert 'data-test="offcanvas-attrs"' in rendered
        assert 'id="custom-offcanvas"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Offcanvas" attrs:class="custom-offcanvas-class extra-class" attrs:data-merged="test" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "offcanvas" in rendered
        assert "custom-offcanvas-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Offcanvas" attrs:class="custom-inline" attrs:data-inline="value" %}Content{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "offcanvas" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_pagination(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Pagination" size="lg" %}
                {% component "PageItem" disabled=True %}
                    {% component "PageLink" %}Previous{% endcomponent %}
                {% endcomponent %}
                {% component "PageItem" active=True %}
                    {% component "PageLink" %}1{% endcomponent %}
                {% endcomponent %}
                {% component "PageItem" %}
                    {% component "PageLink" %}2{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "pagination" in rendered
        assert "pagination-lg" in rendered
        assert "disabled" in rendered
        assert "active" in rendered
        assert "Previous" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Pagination" attrs:data-test="pagination-attrs" attrs:id="custom-pagination" %}
                {% component "PageItem" %}
                    {% component "PageLink" %}1{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "pagination" in rendered
        assert 'data-test="pagination-attrs"' in rendered
        assert 'id="custom-pagination"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Pagination" size="sm" attrs:class="custom-pagination-class extra-class" attrs:data-merged="test" %}
                {% component "PageItem" %}
                    {% component "PageLink" %}1{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "pagination" in rendered
        assert "pagination-sm" in rendered
        assert "custom-pagination-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Pagination" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "PageItem" %}
                    {% component "PageLink" %}1{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "pagination" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Pagination" %}
                {% component "PaginationFirst" disabled=True %}{% endcomponent %}
                {% component "PaginationPrev" disabled=True %}{% endcomponent %}
                {% component "PageItem" active=True %}
                    {% component "PageLink" %}1{% endcomponent %}
                {% endcomponent %}
                {% component "PaginationNext" disabled=True %}{% endcomponent %}
                {% component "PaginationLast" disabled=True %}{% endcomponent %}
                {% component "PaginationEllipsis" disabled=True %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "«" in rendered
        assert "‹" in rendered
        assert "›" in rendered
        assert "»" in rendered
        assert "…" in rendered
        assert "visually-hidden" in rendered
        assert "First" in rendered
        assert "Previous" in rendered
        assert "Next" in rendered
        assert "Last" in rendered
        assert "More" in rendered
        assert "disabled" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Pagination" %}
                {% component "PaginationFirst" href="/page/1" attrs:class="custom-first" disabled=False %}{% endcomponent %}
                {% component "PaginationPrev" href="/page/2" attrs:data-prev="true" disabled=False %}{% endcomponent %}
                {% component "PaginationNext" href="/page/4" attrs:data-next="true" disabled=False %}{% endcomponent %}
                {% component "PaginationLast" href="/page/10" attrs:class="custom-last" disabled=False %}{% endcomponent %}
                {% component "PaginationEllipsis" disabled=False attrs:class="custom-ellipsis" %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'href="/page/1"' in rendered
        assert 'href="/page/2"' in rendered
        assert 'href="/page/4"' in rendered
        assert 'href="/page/10"' in rendered
        assert "custom-first" in rendered
        assert "custom-last" in rendered
        assert "custom-ellipsis" in rendered
        assert 'data-prev="true"' in rendered
        assert 'data-next="true"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Pagination" %}
                {% component "PaginationFirst" %}Custom First{% endcomponent %}
                {% component "PaginationPrev" %}Custom Prev{% endcomponent %}
                {% component "PaginationNext" %}Custom Next{% endcomponent %}
                {% component "PaginationLast" %}Custom Last{% endcomponent %}
                {% component "PaginationEllipsis" %}...{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "Custom First" in rendered
        assert "Custom Prev" in rendered
        assert "Custom Next" in rendered
        assert "Custom Last" in rendered

    def test_placeholder(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Placeholder" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "placeholder" in rendered
        assert "<span" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Placeholder" size="lg" bg="primary" animation="glow" xs=6 %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "placeholder" in rendered
        assert "placeholder-lg" in rendered
        assert "bg-primary" in rendered
        assert "placeholder-glow" in rendered
        assert "col-6" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Placeholder" as_="div" animation="wave" attrs:data-test="placeholder" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "placeholder" in rendered
        assert "placeholder-wave" in rendered
        assert "<div" in rendered
        assert 'data-test="placeholder"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "PlaceholderButton" variant="danger" xs=4 %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn" in rendered
        assert "btn-danger" in rendered
        assert "placeholder" in rendered
        assert "col-4" in rendered
        assert "disabled" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Placeholder" attrs:class="custom-placeholder extra-class" attrs:data-merged="test" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "placeholder" in rendered
        assert "custom-placeholder" in rendered
        assert "extra-class" in rendered

    def test_popover(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Popover" content="Popover content" %}Click me{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="popover"' in rendered
        assert 'data-bs-placement="top"' in rendered
        assert 'data-bs-content="Popover content"' in rendered
        assert 'data-bs-trigger="click"' in rendered
        assert "Click me" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Popover" content="Body text" title="Popover title" placement="bottom" trigger="hover" %}
                Hover me
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="popover"' in rendered
        assert 'data-bs-content="Body text"' in rendered
        assert 'data-bs-title="Popover title"' in rendered
        assert 'data-bs-placement="bottom"' in rendered
        assert 'data-bs-trigger="hover"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Popover" content="Info" placement="left" as_="a" attrs:data-test="popover" %}Link{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="popover"' in rendered
        assert 'data-bs-placement="left"' in rendered
        assert 'data-test="popover"' in rendered
        assert "<a" in rendered
        assert "Link" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Popover" content="Text" attrs:class="custom-popover extra-class" attrs:data-merged="test" %}
                Button
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="popover"' in rendered
        assert "custom-popover" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

    def test_progress(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Progress" height="20px" %}
                {% component "ProgressBar" now=75 variant="success" striped=True animated=True %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "progress" in rendered
        assert "progress-bar" in rendered
        assert "bg-success" in rendered
        assert "progress-bar-striped" in rendered
        assert "progress-bar-animated" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ProgressStacked" %}
                {% component "ProgressBar" now=30 %}{% endcomponent %}
                {% component "ProgressBar" now=20 %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "progress-stacked" in rendered
        assert "progress-bar" in rendered
        assert "30" in rendered
        assert "20" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Progress" attrs:data-test="progress-attrs" attrs:id="custom-progress" %}
                {% component "ProgressBar" now=50 %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "progress" in rendered
        assert 'data-test="progress-attrs"' in rendered
        assert 'id="custom-progress"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Progress" attrs:class="custom-progress-class extra-class" attrs:data-merged="test" %}
                {% component "ProgressBar" now=50 %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "progress" in rendered
        assert "custom-progress-class" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Progress" attrs:class="custom-inline" attrs:data-inline="value" %}
                {% component "ProgressBar" now=50 %}{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "progress" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_spinner(self):
        template = Template("""
            {% component "Spinner" animation="grow" size="sm" variant="primary" %}Loading...{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "spinner-grow" in rendered
        assert "spinner-grow-sm" in rendered
        assert "text-primary" in rendered
        assert "Loading..." in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Spinner" attrs:data-test="spinner-attrs" attrs:id="custom-spinner" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "spinner-border" in rendered
        assert 'data-test="spinner-attrs"' in rendered
        assert 'id="custom-spinner"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Spinner" animation="grow" variant="danger" attrs:class="custom-spinner-class extra-class" attrs:data-merged="test" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "spinner-grow" in rendered
        assert "text-danger" in rendered
        assert "custom-spinner-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Spinner" attrs:class="custom-inline" attrs:data-inline="value" %}{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "spinner-border" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_stack(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" %}
                <div>First</div>
                <div>Second</div>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "vstack" in rendered
        assert "First" in rendered
        assert "Second" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="horizontal" gap=3 %}
                <div>Item 1</div>
                <div>Item 2</div>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "hstack" in rendered
        assert "gap-3" in rendered
        assert "Item 1" in rendered
        assert "Item 2" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" direction="horizontal" responsive="md" gap=2 attrs:data-test="stack" %}
                <div>Item</div>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "hstack-md" in rendered
        assert "gap-2" in rendered
        assert 'data-test="stack"' in rendered
        assert "Item" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Stack" gap=4 attrs:class="custom-stack extra-class" attrs:data-merged="test" %}
                <div>Content</div>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "vstack" in rendered
        assert "gap-4" in rendered
        assert "custom-stack" in rendered
        assert "extra-class" in rendered

    def test_table(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Table" striped=True striped_columns=True bordered=True hover=True borderless=True small=True variant="dark" responsive="lg" caption_top=True %}
                <caption>Caption</caption>
                <thead><tr><th>Header</th></tr></thead>
                <tbody><tr><td>Data</td></tr></tbody>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "table" in rendered
        assert "table-striped" in rendered
        assert "table-striped-columns" in rendered
        assert "table-bordered" in rendered
        assert "table-hover" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Table" responsive=True %}
                <tbody><tr><td>Data</td></tr></tbody>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "table" in rendered
        assert "table-responsive" in rendered
        assert "Data" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Table" attrs:data-test="table-attrs" attrs:id="custom-table" %}
                <tbody><tr><td>Data</td></tr></tbody>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "table" in rendered
        assert 'data-test="table-attrs"' in rendered
        assert 'id="custom-table"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Table" striped=True hover=True attrs:class="custom-table-class extra-class" attrs:data-merged="test" %}
                <tbody><tr><td>Data</td></tr></tbody>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "table" in rendered
        assert "table-striped" in rendered
        assert "table-hover" in rendered
        assert "custom-table-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Table" attrs:class="custom-inline" attrs:data-inline="value" %}
                <tbody><tr><td>Data</td></tr></tbody>
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "table" in rendered
        assert "custom-inline" in rendered
        assert 'data-inline="value"' in rendered

    def test_tabs(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tabs" default_active_tab="home" %}
                {% component "Tab" tab_id="home" title="Home" %}
                    Home content
                {% endcomponent %}
                {% component "Tab" tab_id="profile" title="Profile" %}
                    Profile content
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav-tabs" in rendered
        assert 'role="tablist"' in rendered
        assert "Home" in rendered
        assert "Profile" in rendered
        assert "Home content" in rendered
        assert "Profile content" in rendered
        assert "tab-pane" in rendered
        assert "active" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Tabs" variant="pills" fill=True default_active_tab="first" %}
                {% component "Tab" tab_id="first" title="First Tab" %}
                    First content
                {% endcomponent %}
                {% component "Tab" tab_id="second" title="Second Tab" disabled=True %}
                    Second content
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav-pills" in rendered
        assert "nav-fill" in rendered
        assert "First Tab" in rendered
        assert "Second Tab" in rendered
        assert "disabled" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "TabContent" %}
                {% component "TabPane" id="pane1" active=True %}
                    Pane 1 content
                {% endcomponent %}
                {% component "TabPane" id="pane2" fade=False %}
                    Pane 2 content
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "tab-content" in rendered
        assert "tab-pane" in rendered
        assert 'id="pane1"' in rendered
        assert 'id="pane2"' in rendered
        assert "show active" in rendered
        assert "Pane 1 content" in rendered
        assert "Pane 2 content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "TabContainer" id="my-tabs" %}
                {% component "Nav" variant="tabs" %}
                    {% component "NavItem" %}
                        {% component "NavLink" active=True %}Tab 1{% endcomponent %}
                    {% endcomponent %}
                {% endcomponent %}
                {% component "TabContent" %}
                    {% component "TabPane" active=True %}Content 1{% endcomponent %}
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "nav-tabs" in rendered
        assert "Tab 1" in rendered
        assert "Content 1" in rendered

        with pytest.raises(RuntimeError) as exc_info:
            template = Template("""
                {% load bootstrap5 %}
                {% component "Tab" tab_id="orphan" title="Orphan" %}Content{% endcomponent %}
            """)
            template.render(Context({}))
        assert "must be used as a child of 'Tabs' component" in str(exc_info.value)

        with pytest.raises(RuntimeError) as exc_info:
            template = Template("""
                {% load bootstrap5 %}
                {% provide "_tabs" id="test" tab_data=[] default_active_tab="" enabled=False %}
                    {% component "Tab" tab_id="nested" title="Nested" %}Content{% endcomponent %}
                {% endprovide %}
            """)
            template.render(Context({}))
        assert "must be a direct child of 'Tabs' component" in str(exc_info.value)

        template = Template("""
            {% load bootstrap5 %}
            {% component "Tabs" %}
                {% component "Tab" tab_id="tab1" title="Tab 1" %}
                    Content
                {% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "Tab 1" in rendered
        assert "Content" in rendered

    def test_toast(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Toast" %}
                {% component "ToastHeader" %}Header{% endcomponent %}
                {% component "ToastBody" %}Body content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast" in rendered
        assert "toast-header" in rendered
        assert "toast-body" in rendered
        assert "Header" in rendered
        assert "Body content" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Toast" show=True bg="primary" autohide=False %}
                {% component "ToastHeader" close_button=False %}Title{% endcomponent %}
                {% component "ToastBody" %}Message{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast" in rendered
        assert "show" in rendered
        assert "bg-primary" in rendered
        assert "text-white" in rendered
        assert 'data-bs-autohide="false"' in rendered
        assert "Title" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToastContainer" position="top" %}
                {% component "Toast" %}Content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast-container" in rendered
        assert "position-fixed" in rendered
        assert "top-0" in rendered
        assert "toast" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Toast" delay=3000 attrs:data-test="toast" attrs:id="myToast" %}
                {% component "ToastBody" %}Test{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast" in rendered
        assert 'data-bs-delay="3000"' in rendered
        assert 'data-test="toast"' in rendered
        assert 'id="myToast"' in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Toast" attrs:class="custom-toast extra-class" attrs:data-merged="test" %}
                {% component "ToastBody" %}Content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast" in rendered
        assert "custom-toast" in rendered
        assert "extra-class" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToastContainer" position="bottom" %}
                {% component "Toast" %}Content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast-container" in rendered
        assert "position-fixed" in rendered
        assert "bottom-0" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToastContainer" position="start" %}
                {% component "Toast" %}Content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast-container" in rendered
        assert "position-fixed" in rendered
        assert "start-0" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToastContainer" position="end" %}
                {% component "Toast" %}Content{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "toast-container" in rendered
        assert "position-fixed" in rendered
        assert "end-0" in rendered

    def test_toggle_button(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "ToggleButton" id="toggle1" %}Toggle{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-check" in rendered
        assert 'type="checkbox"' in rendered
        assert 'id="toggle1"' in rendered
        assert "btn" in rendered
        assert "btn-outline-primary" in rendered
        assert "Toggle" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToggleButton" id="radio1" type="radio" name="options" value="1" checked=True variant="success" outline=False %}
                Option 1
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-check" in rendered
        assert 'type="radio"' in rendered
        assert 'name="options"' in rendered
        assert 'value="1"' in rendered
        assert "checked" in rendered
        assert "btn-success" in rendered
        assert "Option 1" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToggleButtonGroup" name="choices" type="checkbox" vertical=True size="lg" %}
                {% component "ToggleButton" id="choice1" %}Choice 1{% endcomponent %}
                {% component "ToggleButton" id="choice2" %}Choice 2{% endcomponent %}
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-group-vertical" in rendered
        assert "btn-group-lg" in rendered
        assert "Choice 1" in rendered
        assert "Choice 2" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToggleButton" id="btn1" disabled=True size="sm" attrs:data-test="toggle" %}
                Disabled
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-check" in rendered
        assert "disabled" in rendered
        assert "btn-sm" in rendered
        assert 'data-test="toggle"' in rendered
        assert "Disabled" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "ToggleButton" id="btn2" attrs:class="custom-toggle extra-class" attrs:data-merged="test" %}
                Button
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert "btn-check" in rendered
        assert "custom-toggle" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered

    def test_tooltip(self):
        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Tooltip text" %}Hover me{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="tooltip"' in rendered
        assert 'data-bs-placement="top"' in rendered
        assert 'title="Tooltip text"' in rendered
        assert "Hover me" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Help text" placement="bottom" as_="button" %}
                Click for help
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="tooltip"' in rendered
        assert 'data-bs-placement="bottom"' in rendered
        assert 'title="Help text"' in rendered
        assert "<button" in rendered
        assert "Click for help" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Info" placement="right" attrs:data-test="tooltip" %}Info{% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="tooltip"' in rendered
        assert 'data-bs-placement="right"' in rendered
        assert 'data-test="tooltip"' in rendered
        assert "Info" in rendered

        template = Template("""
            {% load bootstrap5 %}
            {% component "Tooltip" text="Tip" attrs:class="custom-tooltip extra-class" attrs:data-merged="test" %}
                Content
            {% endcomponent %}
        """)
        rendered = template.render(Context({}))
        assert 'data-bs-toggle="tooltip"' in rendered
        assert "custom-tooltip" in rendered
        assert "extra-class" in rendered
        assert 'data-merged="test"' in rendered
