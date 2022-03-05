"""
    Retrieve file link and password.

    https://github.com/trevormiller6
"""

from pathlib import Path
from hashlib import md5
import utils.make_password as make_password


def get(passphrase):

    file_path = Path.cwd() / "files" / f"{md5(passphrase.encode()).hexdigest()}.zip"

    if file_path.is_file():

        with open(file_path, "rb") as zipfile:
            zip_bytes = zipfile.read()

        return file_path.name, make_password.get(passphrase), zip_bytes

    else:
        return "", "UH-OH... Passphrase is wrong. Try again.", b""
