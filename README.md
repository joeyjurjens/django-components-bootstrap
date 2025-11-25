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
{% load component_tags %}

{% component "Button" variant="primary" %}
    Click me!
{% endcomponent %}

{% component "Alert" variant="success" dismissible=True %}
    <strong>Success!</strong> Your changes have been saved.
{% endcomponent %}
```

## Configuration

By default, all Bootstrap components are automatically registered when the app loads. To disable auto-registration:

```python
DJANGO_COMPONENTS_BOOTSTRAP = {
    "AUTO_REGISTER": False,
}
```

When auto-registration is disabled, you can manually import and register components:

```python
from django_components import registry
from django_components_bootstrap.components.bootstrap5 import Button, Alert

registry.register("Button", Button)
registry.register("MyAlert", Alert)  # Register under a custom name
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
