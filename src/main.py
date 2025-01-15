#!/usr/bin/env python3

import shutil
from pathlib import Path
from markdowntohtmlnode import markdown_to_html_node
from extract import extract_title


def copy_static_to_public(static_path: Path, public_path: Path) -> None:

    if public_path.exists():
        shutil.rmtree(public_path)

    public_path.mkdir(parents=True, exist_ok=True)

    copy_recursive(static_path, public_path)


def copy_recursive(source: Path, dest: Path) -> None:

    if source.is_file():
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, dest)

    if source.is_dir():
        dest.mkdir(exist_ok=True)
        for item in source.iterdir():
            relative_path = item.relative_to(source)
            new_dest = dest / relative_path
            copy_recursive(item, new_dest)


def generate_page(from_path: Path, template_path: Path, dest_path: Path) -> None:

    dest_path.parent.mkdir(parents=True, exist_ok=True)

    with open(from_path, "r") as fh:
        markdown = fh.read()

    with open(template_path, "r") as fh:
        template = fh.read()

    html_node = markdown_to_html_node(markdown)
    html_content = html_node.to_html()
    html_title = extract_title(markdown)

    template = template.replace("{{ Title }}", html_title)
    template = template.replace("{{ Content }}", html_content)

    with open(dest_path, "w") as fh:
        fh.write(template)


def generate_pages_recursive(content_path: Path, template_path: Path, dest_path: Path) -> None:

    if content_path.is_dir():
        dest_path.mkdir(parents=True, exist_ok=True)
        for item in content_path.iterdir():
            relative_path = item.relative_to(content_path)
            new_dest = dest_path / relative_path
            generate_pages_recursive(item, template_path, new_dest)

    elif content_path.suffix == ".md":
        new_dest_path = Path(str(dest_path).replace('.md', '.html'))
        new_dest_path.parent.mkdir(parents=True, exist_ok=True)
        generate_page(content_path, template_path, new_dest_path)


def main() -> None:

    script_path = Path(__file__).parent
    static_path = script_path.parent / "static"
    public_path = script_path .parent / "public"
    template_path = script_path.parent / "src/templates/template.html"
    content_path = script_path.parent / "content"
    copy_static_to_public(static_path, public_path)
    generate_pages_recursive(content_path, template_path, public_path)


if __name__ == "__main__":
    main()
