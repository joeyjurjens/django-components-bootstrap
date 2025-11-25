from django.template import Context
from django_components import Component, types



class CloseButton(Component):
    class Kwargs:
        variant: str | None = None
        disabled: bool = False
        attrs: dict | None = None

    class Slots:
        pass

    def get_template_data(self, args, kwargs: Kwargs, slots, context: Context):
        classes = ["btn-close"]
        if kwargs.variant:
            classes.append(f"btn-close-{kwargs.variant}")

        disabled = True if kwargs.disabled else None

        return {
            "classes": " ".join(classes),
            "disabled": disabled,
            "attrs": kwargs.attrs,
        }

    template: types.django_html = """
        {% load component_tags %}

        <button {% html_attrs attrs type="button" class=classes defaults:aria-label="Close" disabled=disabled %}></button>
    """
