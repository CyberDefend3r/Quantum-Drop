from utils import uploader, retriever
from pywebio import start_server, config
from pywebio.output import *
from pywebio.input import *
from pywebio.pin import *


@config(theme="dark")
def main():
    put_grid(
        [
            [
                span(
                    put_markdown(
                        "# Quantum Drop - Anonymous File Sharing  \n  \n  Upload a file to share anonymously or enter passphrase to retrieve a file.\n  \n   ----\n  \n  The file you upload is deleted immediately and stored as an encrypted zip file. The only person that can see the file you upload is anyone you shared the passphrase with. Passphrases are generated randomly and not stored. There is no way to get it after it is displayed to you.\n  \n  IP addresses are not stored or any other data that can identify you.\n  \n  When retrieving a file with the passphrase a password for the zip file will be displayed and a link to download the encrypted zip file will appear once you close the password popup.\n  \n  ----"
                    ),
                    col=5,
                )
            ],
            [
                span(
                    put_row(put_scope("1-2")),
                    col=5,
                    row=1,
                )
            ],
            [
                span(
                    put_row(
                        [put_scope("1-3")],
                    ),
                    col=5,
                    row=2,
                )
            ],
            [span(put_image("img_link"), col=3, row=1), put_scope("2-3")],
        ],
        cell_widths="25% 25% 25% 25%",
    )

    with use_scope("1-3"):
        put_input("something", label="Enter passphrase to retrieve file.")
        put_button("submit", onclick=lambda: submit_passphrase(pin.something))
        # put_file()

    with use_scope("1-2"):
        a = file_upload("Upload File Anonymously")
        passphrase = uploader.upload(a)
        popup(
            "Use this passphrase to retrieve the file",
            put_html(f"<h3>{passphrase}"),
        )


def submit_passphrase(passphrase):
    name, password, zip_bytes = retriever.get(passphrase)
    put_file(name=name, content=zip_bytes)
    popup(
        "Password",
        put_html(f"<h3>{password}"),
    )


if __name__ == "__main__":
    start_server(main, port=8080, debug=True)
