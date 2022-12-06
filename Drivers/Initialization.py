from argparse import ArgumentParser, Namespace

import pytermgui as ptg
import Drivers.Palletes


def process_arguments(argv: list[str] | None = None) -> Namespace:
    parser = ArgumentParser(description="Args")
    return parser.parse_args(argv)


def create_aliases() -> None:
    ptg.tim.alias("app.text", "#cfc7b0")

    ptg.tim.alias("app.header", f"bold #B8B8B8")
    ptg.tim.alias("app.header.fill", f"@{Drivers.Palletes.PALETTE_MID}")

    ptg.tim.alias("app.title", f"bold #858585")
    ptg.tim.alias("app.button.label", f"bold @{Drivers.Palletes.PALETTE_DARK} app.text")
    ptg.tim.alias("app.button.highlight", "inverse app.button.label")

    ptg.tim.alias("app.footer", f"@{Drivers.Palletes.PALETTE_MID}")


def configure_widgets() -> None:
    ptg.boxes.DOUBLE.set_chars_of(ptg.Window)
    ptg.boxes.ROUNDED.set_chars_of(ptg.Container)

    ptg.Button.styles.label = "app.button.label"
    ptg.Button.styles.highlight = "app.button.highlight"

    ptg.Slider.styles.filled__cursor = Drivers.Palletes.PALETTE_MID
    ptg.Slider.styles.filled_selected = Drivers.Palletes.PALETTE_LIGHT

    ptg.Label.styles.value = "app.text"

    ptg.Window.styles.border__corner = "#C2B280"
    ptg.Container.styles.border__corner = Drivers.Palletes.PALETTE_DARK

    ptg.Splitter.set_char("separator", "")


def define_layout() -> ptg.Layout:
    layout = ptg.Layout()

    # A header slot with a height of 1
    layout.add_slot("Header", height=1)
    layout.add_break()

    # A body slot that will fill the entire width, and the height is remaining
    layout.add_slot("Body")

    # A slot in the same row as body, using the full non-occupied height and
    # 20% of the terminal's height.
    layout.add_slot("Body right", width=0.2)

    layout.add_break()

    # A footer with a static height of 1
    layout.add_slot("Footer", height=1)

    return layout
