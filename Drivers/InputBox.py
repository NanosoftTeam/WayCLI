import pytermgui as ptg
from subprocess import run


def input_box(title: str, func) -> ptg.Container:
    """Create a Container with title, containing an InputField"""

    box = ptg.Container()
    box.set_char("corner", ["x- " + title + " -", "x", "x", "x"])
    box.set_char("border", ["| ", "-", " |", "-"])

    style = ptg.MarkupFormatter("[243]{item}")
    box.set_style("border", style)
    box.set_style("corner", style)

    field = ptg.InputField()
    field.bind(ptg.keys.RETURN, lambda field, _: func())
    box += field
    return box
