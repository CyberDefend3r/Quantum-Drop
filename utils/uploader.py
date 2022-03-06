"""
    Script to process dropped files.

    https://github.com/trevormiller6
"""

from pathlib import Path
import pyminizip
from hashlib import md5
import utils.password as password
from wonderwords import RandomSentence


def upload(file_object):

    if file_object:

        file_path = Path.cwd() / "files" / file_object["filename"]

        with open(file_path, "wb") as save_file:
            save_file.write(file_object["content"])

        passphrase = (
            RandomSentence().sentence().strip("The ").replace(" ", "-").replace(".", "")
        )

        passwrd = password.generate(passphrase)

        zip_file_name = f"{md5(passphrase.encode()).hexdigest()}.zip"
        zip_file_path = file_path.parent / zip_file_name

        pyminizip.compress(str(file_path), None, str(zip_file_path), passwrd, 5)

        file_path.unlink(missing_ok=True)

        return passphrase
