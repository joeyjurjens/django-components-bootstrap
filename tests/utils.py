import re
from unittest.mock import patch


def normalize_html(html):
    # Remove data-djc-id attributes
    html = re.sub(r'\s*data-djc-id-[^=]*="[^"]*"', "", html)
    html = re.sub(r"\s*data-djc-id-[^=]*='[^']*'", "", html)
    # Remove <template djc-render-id="...">...</template> tags (keep content)
    html = re.sub(r'<template djc-render-id="[^"]*">(.*?)</template>', r"\1", html, flags=re.DOTALL)
    # Normalize whitespace
    html = re.sub(r"\s+", " ", html)
    html = re.sub(r">\s+<", "><", html)
    html = html.strip()
    return html


def mock_component_id():
    """Context manager to mock component IDs for predictable testing."""
    counter = {"value": 0}

    def mock_gen_id():
        counter["value"] += 1
        # Generate simple sequential IDs (alphanumeric only, no hyphens)
        # The format matches django-components: 'c' prefix + 6-char ID (total 7 chars)
        # Pad the counter to ensure consistent length
        return f"ctest{counter['value']:02d}"

    return patch("django_components.component._gen_component_id", side_effect=mock_gen_id)


def mock_component_ids(cls):
    """
    Class decorator to mock component IDs for all test methods in a test class.
    Handles cache cleanup and ID mocking for predictable component testing.
    """
    original_setup = getattr(cls, "setUp", None)
    original_teardown = getattr(cls, "tearDown", None)

    def new_setup(self):
        # Clear django-components caches to prevent ID collisions between tests
        from django_components.component import component_context_cache
        from django_components.provide import component_provides, provide_cache
        from django_components.slots import slot_fills_cache

        component_context_cache.clear()
        component_provides.clear()
        provide_cache.clear()
        slot_fills_cache.clear()

        # Reset the counter before each test
        self._id_counter = {"value": 0}

        def mock_gen_id():
            self._id_counter["value"] += 1
            return f"ctest{self._id_counter['value']:02d}"

        self._id_patcher = patch(
            "django_components.component._gen_component_id", side_effect=mock_gen_id
        )
        self._id_patcher.start()

        if original_setup:
            original_setup(self)

    def new_teardown(self):
        try:
            if hasattr(self, "_id_patcher"):
                self._id_patcher.stop()
        finally:
            if original_teardown:
                original_teardown(self)

    cls.setUp = new_setup
    cls.tearDown = new_teardown
    return cls
