from simple_svg_generator.elements.mixins.set_attribute_protocol import (
    SetAttributeProtocol,
)


class StrokeFillMixin:
    def set_stroke_color(self: SetAttributeProtocol, stroke_color: str) -> None:
        self["stroke"] = stroke_color

    def set_stroke_width(self: SetAttributeProtocol, stroke_width: str) -> None:
        self["stroke-width"] = stroke_width

    def set_fill_color(self: SetAttributeProtocol, fill_color: str) -> None:
        self["fill"] = fill_color
