#!/usr/bin/env python3

import shutil
from pathlib import Path


def copy_static_to_public() -> None:

    script_dir = Path(__file__).parent
    static_dir = script_dir.parent / "static"
    public_dir = script_dir.parent / "public"

    if public_dir.exists():
        shutil.rmtree(public_dir)

    public_dir.mkdir(parents=True, exist_ok=True)

    copy_recursive(static_dir, public_dir)


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


def main() -> None:
    copy_static_to_public()


if __name__ == "__main__":
    main()
