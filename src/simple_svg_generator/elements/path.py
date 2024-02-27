from simple_svg_generator.svg_element import SVGElement
from simple_svg_generator.elements.mixins.transform import TransformMixin
from simple_svg_generator.elements.mixins.stroke_fill import StrokeFillMixin


class path(SVGElement, TransformMixin, StrokeFillMixin):
    def set_definition(self, d: str) -> None:
        self["d"] = d
