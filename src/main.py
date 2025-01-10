#!/usr/bin/env python3

import shutil
from pathlib import Path
from typing import NoReturn


def copy_static_to_public() -> NoReturn:

    script_dir = Path(__file__).parent
    static_dir = script_dir / "static"
    public_dir = script_dir / "public"

    if public_dir.exists():
        shutil.rmtree(public_dir)

    public_dir.mkdir(parents=True, exist_ok=True)

    for item in static_dir.iterdir():
