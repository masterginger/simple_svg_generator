from typing import Self
from simple_svg_generator.elements.mixins.transform import TransformMixin
from simple_svg_generator.elements.mixins.stroke_fill import StrokeFillMixin
from simple_svg_generator.svg_element import SVGElement


class path(TransformMixin, StrokeFillMixin, SVGElement):
    def set_definition(self, d: str) -> Self:
        return self.set_attribute("d", d)
