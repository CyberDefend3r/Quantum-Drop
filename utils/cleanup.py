"""
Cleanup old files.

https://github.com/trevormiller6
"""
from pathlib import Path
import arrow


def delete():

    file_path = Path.cwd() / "files"

    delete_time = arrow.now().shift(days=-3)

    for file in file_path.rglob("*.zip"):
        if file.is_file():
            file_Time = arrow.get(file.stat().st_mtime)
            if file_Time < delete_time:
                file.unlink(missing_ok=True)
