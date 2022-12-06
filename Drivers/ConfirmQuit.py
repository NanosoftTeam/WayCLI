import pytermgui as ptg


def confirm_quit(manager: ptg.WindowManager) -> None:
    modal = ptg.Window(
        "[app.title]Are you sure you want to quit Way App?",
        "",
        ptg.Container(
            ptg.Splitter(
                ptg.Button("Yes", lambda *_: manager.stop()),
                ptg.Button("No", lambda *_: modal.close()),
            ),
        ),
    ).center()

    modal.select(1)
    manager.add(modal)
