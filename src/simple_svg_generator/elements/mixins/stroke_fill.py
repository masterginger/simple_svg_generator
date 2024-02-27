from typing import Self
from simple_svg_generator.svg_element import SVGElement


class StrokeFillMixin(SVGElement):
    def set_stroke_color(self, stroke_color: str) -> Self:
        return self.set_attribute("stroke", stroke_color)

    def set_stroke_width(self, stroke_width: str) -> Self:
        return self.set_attribute("stroke-width", stroke_width)

    def set_fill_color(self, fill_color: str) -> Self:
        return self.set_attribute("fill", fill_color)
