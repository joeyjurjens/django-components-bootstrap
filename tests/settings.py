"""Django settings for testing."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "test-secret-key"

DEBUG = True

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django_components",
    "django_components_bootstrap",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ],
            "builtins": [
                "django_components.templatetags.component_tags",
                "django_components_bootstrap.templatetags.bootstrap5",
            ],
        },
    },
]

USE_TZ = True

ROOT_URLCONF = "django_components_bootstrap.tests.urls"

# Django Components settings
COMPONENTS = {
    "autodiscover": False,
    "dirs": [],
}
