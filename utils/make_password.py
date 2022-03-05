"""
    Generate Password for Zip File.

    https://github.com/trevormiller6
"""

from hashlib import md5


def generate(passphrase):
    return md5(md5(passphrase.encode()).hexdigest().encode()).hexdigest()


def get(passphrase):
    return md5(md5(passphrase.encode()).hexdigest().encode()).hexdigest()
