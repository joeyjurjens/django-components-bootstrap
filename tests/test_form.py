from django.template import Context, Template
from django.test import SimpleTestCase
from django_components.testing import djc_test

from .utils import mock_component_id, normalize_html


class FormTestCase(SimpleTestCase):
    maxDiff = None

    def assertHTMLEqual(self, actual, expected):
        super().assertHTMLEqual(normalize_html(actual), normalize_html(expected))

    def test_basic_form(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "Form" %}
                {% bootstrap5 "FormGroup" control_id="exampleInputEmail1" %}
                    {% bootstrap5 "FormLabel" %}Email address{% endbootstrap5 %}
                    {% bootstrap5 "FormControl" type="email" / %}
                {% endbootstrap5 %}
                {% bootstrap5 "Button" type="submit" variant="primary" %}Submit{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <form>
                <div>
                    <label class="form-label" for="exampleInputEmail1">Email address</label>
                    <input class="form-control" type="email" id="exampleInputEmail1" />
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_with_text(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormGroup" control_id="exampleInputEmail1" %}
                {% bootstrap5 "FormLabel" %}Email address{% endbootstrap5 %}
                {% bootstrap5 "FormControl" type="email" / %}
                {% bootstrap5 "FormText" %}We'll never share your email with anyone else.{% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div>
                <label class="form-label" for="exampleInputEmail1">Email address</label>
                <input class="form-control" type="email" id="exampleInputEmail1" />
                <div class="form-text">We'll never share your email with anyone else.</div>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    @djc_test
    def test_form_checkbox(self):
        with mock_component_id():
            template = Template("""
                {% load bootstrap5 %}
                {% bootstrap5 "FormCheck" attrs:id="exampleCheck1" label="Check me out" / %}
            """)
            rendered = template.render(Context({}))

        expected = """
            <div class="form-check" id="exampleCheck1">
                <input type="checkbox" class="form-check-input" id="formcheck-ctest01">
                <label class="form-check-label" for="formcheck-ctest01">Check me out</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    @djc_test
    def test_form_radio(self):
        with mock_component_id():
            template = Template("""
                {% load bootstrap5 %}
                {% bootstrap5 "FormCheck" type="radio" name="exampleRadio" attrs:id="exampleRadio1" label="Option one" / %}
            """)
            rendered = template.render(Context({}))

        expected = """
            <div class="form-check" id="exampleRadio1">
                <input class="form-check-input" type="radio" name="exampleRadio" id="formcheck-ctest01">
                <label class="form-check-label" for="formcheck-ctest01">Option one</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_control_sizes(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormControl" size="lg" placeholder=".form-control-lg" / %}
            {% bootstrap5 "FormControl" placeholder="Default input" / %}
            {% bootstrap5 "FormControl" size="sm" placeholder=".form-control-sm" / %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <input class="form-control form-control-lg" type="text" placeholder=".form-control-lg" />
            <input class="form-control" type="text" placeholder="Default input" />
            <input class="form-control form-control-sm" type="text" placeholder=".form-control-sm" />
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_control_disabled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormControl" placeholder="Disabled input" disabled=True / %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <input class="form-control" type="text" placeholder="Disabled input" disabled />
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_control_readonly(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormControl" placeholder="Readonly input" readonly=True value="readonly" / %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <input class="form-control" type="text" placeholder="Readonly input" value="readonly" readonly />
        """

        self.assertHTMLEqual(rendered, expected)

    @djc_test
    def test_form_check_inline(self):
        with mock_component_id():
            template = Template("""
                {% load bootstrap5 %}
                {% bootstrap5 "FormCheck" inline=True attrs:id="inlineCheckbox1" value="option1" label="1" / %}
                {% bootstrap5 "FormCheck" inline=True attrs:id="inlineCheckbox2" value="option2" label="2" / %}
            """)
            rendered = template.render(Context({}))

        expected = """
            <div class="form-check form-check-inline" id="inlineCheckbox1">
                <input class="form-check-input" type="checkbox" id="formcheck-ctest01" value="option1">
                <label class="form-check-label" for="formcheck-ctest01">1</label>
            </div>
            <div class="form-check form-check-inline" id="inlineCheckbox2">
                <input class="form-check-input" type="checkbox" id="formcheck-ctest04" value="option2">
                <label class="form-check-label" for="formcheck-ctest04">2</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    @djc_test
    def test_form_check_disabled(self):
        with mock_component_id():
            template = Template("""
                {% load bootstrap5 %}
                {% bootstrap5 "FormCheck" attrs:id="disabledCheck" label="Disabled checkbox" disabled=True / %}
            """)
            rendered = template.render(Context({}))

        expected = """
            <div class="form-check" id="disabledCheck">
                <input class="form-check-input" type="checkbox" id="formcheck-ctest01" disabled>
                <label class="form-check-label" for="formcheck-ctest01">Disabled checkbox</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    @djc_test
    def test_form_switch(self):
        with mock_component_id():
            template = Template("""
                {% load bootstrap5 %}
                {% bootstrap5 "FormCheck" type="switch" attrs:id="flexSwitchCheckDefault" label="Default switch checkbox input" / %}
            """)
            rendered = template.render(Context({}))

        expected = """
            <div class="form-check form-switch" id="flexSwitchCheckDefault">
                <input class="form-check-input" type="checkbox" role="switch" id="formcheck-ctest01">
                <label class="form-check-label" for="formcheck-ctest01">Default switch checkbox input</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_range_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormRange" / %}
        """)
        rendered = template.render(Context())

        expected = """
            <input type="range" class="form-range" min="0" max="100" step="1">
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_range_disabled(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormRange" disabled=True / %}
        """)
        rendered = template.render(Context())

        expected = """
            <input type="range" class="form-range" disabled min="0" max="100" step="1">
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_range_min_max(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormRange" min=0 max=5 / %}
        """)
        rendered = template.render(Context())

        expected = """
            <input type="range" class="form-range" min="0" max="5" step="1">
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_range_step(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormRange" min=0 max=5 step=0.5 / %}
        """)
        rendered = template.render(Context())

        expected = """
            <input type="range" class="form-range" min="0" max="5" step="0.5">
        """

        self.assertHTMLEqual(rendered, expected)

    def test_input_group_with_text(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "InputGroup" %}
                {% bootstrap5 "InputGroupText" %}@{% endbootstrap5 %}
                {% bootstrap5 "FormControl" placeholder="Username" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="input-group">
                <span class="input-group-text">@</span>
                <input type="text" class="form-control" placeholder="Username">
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_input_group_with_button(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "InputGroup" %}
                {% bootstrap5 "Button" variant="outline-secondary" type="button" %}Button{% endbootstrap5 %}
                {% bootstrap5 "FormControl" placeholder="" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="input-group">
                <button class="btn btn-outline-secondary" type="button">Button</button>
                <input type="text" class="form-control" placeholder="">
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_input_group_with_checkbox(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "InputGroup" %}
                {% bootstrap5 "InputGroupCheckbox" attrs:value="" / %}
                {% bootstrap5 "FormControl" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="input-group">
                <div class="input-group-text">
                    <input class="form-check-input mt-0" type="checkbox" value="">
                </div>
                <input type="text" class="form-control">
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_input_group_with_radio(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "InputGroup" %}
                {% bootstrap5 "InputGroupRadio" attrs:value="" / %}
                {% bootstrap5 "FormControl" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="input-group">
                <div class="input-group-text">
                    <input class="form-check-input mt-0" type="radio" value="">
                </div>
                <input type="text" class="form-control">
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_input_group_sizing(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "InputGroup" size="sm" %}
                {% bootstrap5 "InputGroupText" %}Small{% endbootstrap5 %}
                {% bootstrap5 "FormControl" / %}
            {% endbootstrap5 %}
            {% bootstrap5 "InputGroup" %}
                {% bootstrap5 "InputGroupText" %}Default{% endbootstrap5 %}
                {% bootstrap5 "FormControl" / %}
            {% endbootstrap5 %}
            {% bootstrap5 "InputGroup" size="lg" %}
                {% bootstrap5 "InputGroupText" %}Large{% endbootstrap5 %}
                {% bootstrap5 "FormControl" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="input-group input-group-sm">
                <span class="input-group-text">Small</span>
                <input type="text" class="form-control">
            </div>
            <div class="input-group">
                <span class="input-group-text">Default</span>
                <input type="text" class="form-control">
            </div>
            <div class="input-group input-group-lg">
                <span class="input-group-text">Large</span>
                <input type="text" class="form-control">
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_input_group_multiple_inputs(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "InputGroup" %}
                {% bootstrap5 "InputGroupText" %}First and last name{% endbootstrap5 %}
                {% bootstrap5 "FormControl" / %}
                {% bootstrap5 "FormControl" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="input-group">
                <span class="input-group-text">First and last name</span>
                <input type="text" class="form-control">
                <input type="text" class="form-control">
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_input_group_multiple_addons(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "InputGroup" %}
                {% bootstrap5 "InputGroupText" %}${% endbootstrap5 %}
                {% bootstrap5 "InputGroupText" %}0.00{% endbootstrap5 %}
                {% bootstrap5 "FormControl" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="input-group">
                <span class="input-group-text">$</span>
                <span class="input-group-text">0.00</span>
                <input type="text" class="form-control">
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_floating_label_basic(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FloatingLabel" label="Email address" control_id="floatingInput" %}
                {% bootstrap5 "FormControl" type="email" placeholder="name@example.com" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                <label for="floatingInput">Email address</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_floating_label_with_textarea(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FloatingLabel" label="Comments" control_id="floatingTextarea" %}
                {% bootstrap5 "FormTextarea" placeholder="Leave a comment here" attrs:style="height: 100px" attrs:rows="5" / %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="form-floating">
                <textarea class="form-control" id="floatingTextarea" placeholder="Leave a comment here" rows="5" style="height: 100px;"></textarea>
                <label for="floatingTextarea">Comments</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_floating_label_with_select(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FloatingLabel" label="Works with selects" control_id="floatingSelect" %}
                {% bootstrap5 "FormSelect" %}
                    <option selected>Open this select menu</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                {% endbootstrap5 %}
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="form-floating">
                <select class="form-select" id="floatingSelect">
                    <option selected>Open this select menu</option>
                    <option value="1">One</option>
                    <option value="2">Two</option>
                    <option value="3">Three</option>
                </select>
                <label for="floatingSelect">Works with selects</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)

    def test_form_floating_low_level(self):
        template = Template("""
            {% load bootstrap5 %}
            {% bootstrap5 "FormFloating" %}
                {% bootstrap5 "FormControl" type="email" attrs:id="floatingInputCustom" placeholder="name@example.com" / %}
                <label for="floatingInputCustom">Email address</label>
            {% endbootstrap5 %}
        """)
        rendered = template.render(Context({}))

        expected = """
            <div class="form-floating">
                <input type="email" class="form-control" id="floatingInputCustom" placeholder="name@example.com">
                <label for="floatingInputCustom">Email address</label>
            </div>
        """

        self.assertHTMLEqual(rendered, expected)
