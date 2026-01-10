import os
import re
from pathlib import Path
from unittest.mock import patch

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tests.settings")
django.setup()

from django.template import Context, Template  # noqa: E402

_component_id_counter = {"value": 0}


def mock_gen_id():
    _component_id_counter["value"] += 1
    return f"ctest{_component_id_counter['value']:02d}"


_id_patcher = patch("django_components.component._gen_component_id", side_effect=mock_gen_id)


def render_example(template_code, use_mock_ids=False):
    try:
        template_str = f"{{% load component_tags %}}\n{template_code}"
        if use_mock_ids:
            # When using mock IDs, we need to create template AND render within the patch context
            with _id_patcher:
                template = Template(template_str)
                rendered = template.render(Context({}))
        else:
            template = Template(template_str)
            rendered = template.render(Context({}))

        # Make Modal and Toast visible in docs by adding 'show' class and display:block
        # Modal: add 'show' class and style="display: block" (only to main modal div, not modal-header/body/footer)
        rendered = re.sub(
            r'class="modal fade"',
            r'class="modal fade show" style="display: block; position: relative;"',
            rendered,
        )
        # Toast: add 'show' class
        rendered = re.sub(r'(<div[^>]*class="[^"]*toast[^"]*)"', r'\1 show"', rendered)

        return rendered
    except Exception as e:
        import traceback

        error_details = traceback.format_exc()
        print(f"\n\nError rendering example:\n{error_details}\n")
        return f'<div class="alert alert-danger">Error rendering: {str(e)}</div>'


def humanize_test_name(test_name):
    return test_name.replace("test_", "").replace("_", " ").title()


def extract_examples_from_test_file(test_file_path):
    content = test_file_path.read_text()
    examples = []

    test_methods = re.findall(
        r"def (test_\w+)\(self\):(.*?)(?=\n    def |\nclass |\Z)", content, re.DOTALL
    )

    for test_name, test_body in test_methods:
        templates = re.findall(
            r'template = Template\((?:"""|\'\'\')(.*?)(?:"""|\'\'\')\)', test_body, re.DOTALL
        )

        if templates:
            template_code = templates[0].strip()
            template_code = re.sub(r"{%\s*load\s+component_tags\s*%}\s*", "", template_code).strip()

            examples.append(
                {
                    "title": humanize_test_name(test_name),
                    "code": template_code,
                }
            )

    return examples


def get_component_name_from_test_file(test_file):
    name = test_file.stem.replace("test_", "")
    return "".join(word.capitalize() for word in name.split("_"))


def create_component_page(component_name, examples, snippets_dir):
    md_content = f"# {component_name}\n\n"

    if not examples:
        md_content += "_No examples available yet._\n"
        return md_content

    for idx, example in enumerate(examples):
        _component_id_counter["value"] = 0

        md_content += f"## {example['title']}\n\n"
        md_content += f"```django\n{example['code']}\n```\n\n"
        md_content += "**Preview:**\n\n"

        rendered_html = render_example(example["code"], use_mock_ids=False).strip()

        wrapped_html = f'<div class="bs-example">\n{rendered_html}\n</div>'

        snippet_file = f"{component_name.lower()}_example_{idx + 1}.html"
        (snippets_dir / snippet_file).write_text(wrapped_html)

        md_content += f'--8<-- "snippets/{snippet_file}"\n\n'
        md_content += "---\n\n"

    return md_content


def create_index_page(component_docs):
    md_content = """# Django Components Bootstrap

Bootstrap 5 components for Django, inspired by the React-Bootstrap API.

## Installation

```bash
pip install django-components-bootstrap
```

## Quick Start

Add to your `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    # ...
    "django_components",
    "django_components_bootstrap",
]
```

## Components

"""
    for component_name in sorted(component_docs.keys()):
        md_content += f"- [{component_name}](components/{component_name.lower()}.md)\n"

    return md_content


def main():
    docs_dir = Path("source")
    docs_dir.mkdir(exist_ok=True)
    (docs_dir / "components").mkdir(exist_ok=True)
    (docs_dir / "snippets").mkdir(exist_ok=True)

    snippets_dir = docs_dir / "snippets"
    tests_dir = Path("..") / "tests"
    test_files = sorted(tests_dir.glob("test_*.py"))

    test_files = [f for f in test_files if f.name not in ["test_components.py", "__init__.py"]]

    component_docs = {}

    for test_file in test_files:
        component_name = get_component_name_from_test_file(test_file)
        examples = extract_examples_from_test_file(test_file)

        if examples:
            component_docs[component_name] = examples

    for component_name, examples in sorted(component_docs.items()):
        page_content = create_component_page(component_name, examples, snippets_dir)
        output_file = docs_dir / "components" / f"{component_name.lower()}.md"
        output_file.write_text(page_content)

    index_content = create_index_page(component_docs)
    (docs_dir / "index.md").write_text(index_content)

    print(f"Generated documentation for {len(component_docs)} components:\n")
    for name, examples in sorted(component_docs.items()):
        print(f"  {name:20} ({len(examples)} examples)")

    print(f"\nOutput directory: {docs_dir.absolute()}")


if __name__ == "__main__":
    main()
