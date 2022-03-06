from utils import uploader, retriever, cleanup
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
                        "# Quantum Drop - Anonymous File Sharing  \n  \n  Upload a file to share anonymously or enter passphrase to retrieve a file.\n  \n   ----\n  \n  The file you upload is deleted immediately and stored as an password protected zip file. Passphrases are generated randomly and not stored. There is no way to get it after it is displayed to you.\n  \n  **IP addresses are not stored or any other data that can identify you.**\n  \n  ----\n  When retrieving a file with the passphrase a password for the zip file will be displayed and a link to download the zip file will appear once you close the password popup.\n  "
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
        put_input("phrase", label="Enter passphrase to retrieve file:")
        put_button("submit", onclick=lambda: submit_passphrase(pin.phrase))
        # put_file()

    with use_scope("1-2"):
        popup(
            "Terms of Use",
            put_markdown(
                "### Closing this means you agree to these rules:  \n  1) No adult content.\n  2) No illegal content.\n  3) You will not hold me liable for any files that are malicious or damaging to your computer or your life.\n  3) Files uploaded will only be stored for 3 days. However, there is no guarantee the file will be available when requested.\n  4) Any access to your file is your responsibility and I am not liable for any unintended access to your file.\n  5) There is no guarantee of privacy or anonymity. Though, every effort, to my ability, is made to maintain privacy and anonymity."
            ),
        )
        a = file_upload("Upload File Anonymously - 50Mb max", max_size="50m")
        passphrase = uploader.upload(a)
        popup(
            "Use this passphrase to retrieve the file",
            put_markdown(f"**{passphrase}**"),
        )


def submit_passphrase(passphrase):
    password, zip_bytes = retriever.get(passphrase)
    put_file(name="quantum-drop.zip", content=zip_bytes)
    popup(
        "Password",
        put_markdown(f"**{password}**"),
    )
    cleanup.delete()


start_server(main, port=80, debug=True)
popup(
    "Terms of Use",
    put_markdown(
        "# By Closing this popup you agree to the following rules  \n  1) No adult content\n  2) No illegal content\n  3) You will not hold me liable for any files that are malicious or damaging to your computer or your life.\n  3) There is no guarantee the file will be available when requested\n  4) Files uploaded will only be stored for 3 days"
    ),
)
