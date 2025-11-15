from typing import Literal

from django.template import Context
from django_components import Component, SlotInput, register, types

from django_components_bootstrap.components.bootstrap5.types import FormCheckType, Size
from django_components_bootstrap.templatetags.bootstrap5 import comp_registry


@register("Form", registry=comp_registry)
class Form(Component):
    class Kwargs:
        validated: bool = False
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = []
        if kwargs.validated:
            classes.append("was-validated")

        return {
            "form_class": " ".join(classes),
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <form {% html_attrs attrs class=form_class %}>
            {% slot "default" / %}
        </form>
    """


@register("FormGroup", registry=comp_registry)
class FormGroup(Component):
    class Kwargs:
        control_id: str | None = None
        as_: str = "div"
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "tag": kwargs.as_,
            "control_id": kwargs.control_id,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        {% provide "formgroup" control_id=control_id %}
            <{{ tag }} {% html_attrs attrs %}>
                {% slot "default" / %}
            </{{ tag }}>
        {% endprovide %}
    """


@register("FormLabel", registry=comp_registry)
class FormLabel(Component):
    class Kwargs:
        for_: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        try:
            formgroup = self.inject("formgroup")
            for_value = kwargs.for_ or formgroup.control_id
        except Exception:
            for_value = kwargs.for_

        return {
            "for_": for_value,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <label {% html_attrs attrs defaults:class="form-label" defaults:for=for_ %}>
            {% slot "default" / %}
        </label>
    """


@register("FormControl", registry=comp_registry)
class FormControl(Component):
    class Kwargs:
        type: Literal[
            "text",
            "email",
            "password",
            "number",
            "tel",
            "url",
            "search",
            "date",
            "time",
            "datetime-local",
            "month",
            "week",
            "color",
            "file",
        ] = "text"
        size: Size | None = None
        plaintext: bool = False
        disabled: bool = False
        readonly: bool = False
        is_valid: bool = False
        is_invalid: bool = False
        html_size: int | None = None
        value: str | None = None
        placeholder: str | None = None
        id: str | None = None
        name: str | None = None
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        try:
            formgroup = self.inject("formgroup")
            control_id = kwargs.id or formgroup.control_id
        except Exception:
            control_id = kwargs.id

        if kwargs.plaintext:
            form_class = "form-control-plaintext"
        else:
            classes = ["form-control"]
            if kwargs.type == "color":
                classes.append("form-control-color")
            if kwargs.size:
                classes.append(f"form-control-{kwargs.size}")
            if kwargs.is_valid:
                classes.append("is-valid")
            if kwargs.is_invalid:
                classes.append("is-invalid")
            form_class = " ".join(classes)

        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True
        if kwargs.readonly:
            html_attrs["readonly"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "form_class": form_class,
            "type": kwargs.type,
            "html_size": kwargs.html_size,
            "value": kwargs.value,
            "placeholder": kwargs.placeholder,
            "id": control_id,
            "name": kwargs.name,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <input {% html_attrs attrs class=form_class defaults:type=type defaults:id=id defaults:name=name defaults:value=value defaults:placeholder=placeholder defaults:size=html_size %} />
    """


@register("FormTextarea", registry=comp_registry)
class FormTextarea(Component):
    class Kwargs:
        rows: int = 3
        size: Size | None = None
        disabled: bool = False
        readonly: bool = False
        value: str | None = None
        placeholder: str | None = None
        id: str | None = None
        name: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["form-control"]
        if kwargs.size:
            classes.append(f"form-control-{kwargs.size}")

        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True
        if kwargs.readonly:
            html_attrs["readonly"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "classes": " ".join(classes),
            "rows": kwargs.rows,
            "value": kwargs.value,
            "placeholder": kwargs.placeholder,
            "id": kwargs.id,
            "name": kwargs.name,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <textarea {% html_attrs attrs class=classes defaults:rows=rows defaults:id=id defaults:name=name defaults:placeholder=placeholder %}>{% if value %}{{ value }}{% endif %}{% slot "default" default / %}</textarea>
    """


@register("FormSelect", registry=comp_registry)
class FormSelect(Component):
    class Kwargs:
        size: Size | None = None
        disabled: bool = False
        is_valid: bool = False
        is_invalid: bool = False
        html_size: int | None = None
        value: str | None = None
        id: str | None = None
        name: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        classes = ["form-select"]
        if kwargs.size:
            classes.append(f"form-select-{kwargs.size}")
        if kwargs.is_valid:
            classes.append("is-valid")
        if kwargs.is_invalid:
            classes.append("is-invalid")

        html_attrs = {}
        if kwargs.disabled:
            html_attrs["disabled"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "classes": " ".join(classes),
            "html_size": kwargs.html_size,
            "value": kwargs.value,
            "id": kwargs.id,
            "name": kwargs.name,
            "attrs": final_attrs,
        }

    template: types.django_html = """
        <select {% html_attrs attrs class=classes defaults:id=id defaults:name=name defaults:size=html_size %}>
            {% slot "default" / %}
        </select>
    """


@register("FormCheckInput", registry=comp_registry)
class FormCheckInput(Component):
    class Kwargs:
        type: FormCheckType | None = None
        disabled: bool = False
        checked: bool = False
        is_valid: bool = False
        is_invalid: bool = False
        id: str | None = None
        name: str | None = None
        value: str | None = None
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        try:
            formcheck = self.inject("formcheck")
            control_id = formcheck.control_id
            check_type = formcheck.type
            is_valid = formcheck.is_valid if hasattr(formcheck, "is_valid") else kwargs.is_valid
            is_invalid = (
                formcheck.is_invalid if hasattr(formcheck, "is_invalid") else kwargs.is_invalid
            )
            disabled = formcheck.disabled if hasattr(formcheck, "disabled") else kwargs.disabled
            checked = formcheck.checked if hasattr(formcheck, "checked") else kwargs.checked
        except Exception:
            control_id = kwargs.id
            check_type = kwargs.type if kwargs.type else "checkbox"
            is_valid = kwargs.is_valid
            is_invalid = kwargs.is_invalid
            disabled = kwargs.disabled
            checked = kwargs.checked

        input_type = "checkbox" if check_type == "switch" else check_type

        input_classes = ["form-check-input"]
        if is_valid:
            input_classes.append("is-valid")
        if is_invalid:
            input_classes.append("is-invalid")

        html_attrs = {}
        if checked:
            html_attrs["checked"] = True
        if disabled:
            html_attrs["disabled"] = True

        final_attrs = {**html_attrs, **(kwargs.attrs or {})}

        return {
            "input_classes": " ".join(input_classes),
            "input_type": input_type,
            "id": control_id if control_id else kwargs.id,
            "name": kwargs.name,
            "value": kwargs.value,
            "attrs": final_attrs,
        }

    template: types.django_html = """

        <input {% html_attrs attrs class=input_classes defaults:type=input_type defaults:id=id defaults:name=name defaults:value=value %} />
    """


@register("FormCheckLabel", registry=comp_registry)
class FormCheckLabel(Component):
    class Kwargs:
        for_: str | None = None
        title: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        try:
            formcheck = self.inject("formcheck")
            control_id = formcheck.control_id
        except Exception:
            control_id = kwargs.for_

        return {
            "for_": control_id if control_id else kwargs.for_,
            "title": kwargs.title,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """

        <label {% html_attrs attrs defaults:class="form-check-label" defaults:for=for_ defaults:title=title %}>
            {% slot "default" / %}
        </label>
    """


@register("FormCheck", registry=comp_registry)
class FormCheck(Component):
    class Kwargs:
        type: FormCheckType = "checkbox"
        inline: bool = False
        reverse: bool = False
        disabled: bool = False
        checked: bool = False
        is_valid: bool = False
        is_invalid: bool = False
        id: str | None = None
        name: str | None = None
        value: str | None = None
        label: str | None = None
        title: str | None = None
        attrs: dict | None = None

    class Slots:
        default: SlotInput | None = None

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        wrapper_classes = []
        if kwargs.type == "switch":
            wrapper_classes.append("form-check form-switch")
        else:
            wrapper_classes.append("form-check")

        if kwargs.inline:
            wrapper_classes.append("form-check-inline")
        if kwargs.reverse:
            wrapper_classes.append("form-check-reverse")

        has_label = kwargs.label is not None

        control_id = kwargs.id if kwargs.id else f"formcheck-{self.id}"

        return {
            "wrapper_classes": " ".join(wrapper_classes),
            "type": kwargs.type,
            "disabled": kwargs.disabled,
            "checked": kwargs.checked,
            "is_valid": kwargs.is_valid,
            "is_invalid": kwargs.is_invalid,
            "control_id": control_id,
            "name": kwargs.name,
            "value": kwargs.value,
            "label": kwargs.label,
            "title": kwargs.title,
            "has_label": has_label,
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """

        {% provide "formcheck" control_id=control_id type=type is_valid=is_valid is_invalid=is_invalid disabled=disabled checked=checked %}
            <div {% html_attrs attrs class=wrapper_classes %}>
                {% slot "default" default %}
                    {% component "FormCheckInput" type=type disabled=disabled checked=checked is_valid=is_valid is_invalid=is_invalid id=control_id name=name value=value %}{% endcomponent %}
                    {% if has_label %}
                        {% component "FormCheckLabel" for_=control_id title=title %}
                            {{ label }}
                        {% endcomponent %}
                    {% endif %}
                {% endslot %}
            </div>
        {% endprovide %}
    """


@register("FormText", registry=comp_registry)
class FormText(Component):
    class Kwargs:
        attrs: dict | None = None

    class Slots:
        default: SlotInput

    def get_template_data(self, args, kwargs: Kwargs, slots: Slots, context: Context):
        return {
            "attrs": kwargs.attrs or {},
        }

    template: types.django_html = """
        <div {% html_attrs attrs defaults:class="form-text" %}>
            {% slot "default" / %}
        </div>
    """
