# Django Components Bootstrap

Bootstrap 5 components for Django with React-Bootstrap API parity.

## Installation

```bash
pip install django-components-bootstrap
```

Add to your Django settings:

```python
INSTALLED_APPS = [
    ...
    "django_components",
    "django_components_bootstrap",
]
```

## Quick Start

```django
{% load bootstrap5 %}

{% component "Button" variant="primary" %}
    Click me!
{% endcomponent %}

{% component "Alert" variant="success" dismissible=True %}
    <strong>Success!</strong> Your changes have been saved.
{% endcomponent %}
```

## Documentation

Full documentation with examples: [https://joeyjurjens.github.io/django-components-bootstrap/](https://joeyjurjens.github.io/django-components-bootstrap/)

## Development

### Setup

```bash
git clone https://github.com/joeyjurjens/django-components-bootstrap.git
cd django-components-bootstrap
uv sync --all-extras
```

### Running Tests

```bash
pytest
```

### Building Documentation

```bash
cd docs
python generate_docs.py
mkdocs serve
```

## License

MIT License
