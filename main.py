from __future__ import annotations

import sys

import pytermgui as ptg
from pytermgui import *
import Drivers.ConfirmQuit
import Drivers.Palletes
import Drivers.Initialization
import Controllers.UserController
import Drivers.InputBox


def main(argv: list[str] | None = None) -> None:
    user = Controllers.UserController.UserControllerClass()

    Drivers.Initialization.create_aliases()
    Drivers.Initialization.configure_widgets()

    args = Drivers.Initialization.process_arguments(argv)

    with ptg.WindowManager() as manager:
        manager.layout = Drivers.Initialization.define_layout()

        header = ptg.Window(
            "[app.header] WayApp ",
            box="EMPTY",
            is_persistant=True,
        )

        header.styles.fill = "app.header.fill"

        # Since header is the first defined slot, this will assign to the correct place
        manager.add(header)

        footer = ptg.Window(
            ptg.Button("Quit", lambda *_: Drivers.ConfirmQuit.confirm_quit(manager)),
            box="EMPTY",
        )
        footer.styles.fill = "app.footer"

        # Since the second slot, body was not assigned to, we need to manually assign
        # to "footer"
        manager.add(footer, assign="footer")

        # manager.add(
        #     ptg.Window("My sidebar"),
        #     assign="body_right",
        # )

        manager.add(
            ptg.Window(
                ptg.Collapsible(
                    "[app.title]Warning!",
                    ptg.Container(
                        "You have to be connected to the World Wide Web (internet)",
                        static_width=70
                    )
                ),
                "",
                ptg.Container(
                    "Login",
                    "",
                    Drivers.InputBox.input_box("E-Mail", user.handleemail('l')),
                    Drivers.InputBox.input_box("Password", user.handlepassword('l')),
                    "",
                    "Register",
                    "",
                    Drivers.InputBox.input_box("E-Mail", user.handleemail('r')),
                    Drivers.InputBox.input_box("Password", user.handlepassword('r')),
                    Drivers.InputBox.input_box("Repeat Password", user.handlerepeatpassword()),
                    "",
                    # ptg.Button("Register", lambda *_: )
                    static_width=70,
                    align="center"
                ),
                vertical_align=ptg.VerticalAlignment.TOP,
                overflow=ptg.Overflow.SCROLL,
            ),
            assign="body",
        )

    ptg.tim.print(f"[{Drivers.Palletes.PALETTE_LIGHT}]Goodbye!")


if __name__ == "__main__":
    main(sys.argv[1:])
