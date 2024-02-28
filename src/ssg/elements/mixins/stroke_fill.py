from typing import Self
from ssg.svg_element import SVGElement


class StrokeFillMixin(SVGElement):
    def set_stroke_color(self, stroke_color: str) -> Self:
        return self.set_attribute("stroke", stroke_color)

    def set_stroke_width(self, stroke_width: str) -> Self:
        return self.set_attribute("stroke-width", stroke_width)

    def set_stroke_linecap(self, linecap: str) -> Self:
        return self.set_attribute("stroke-linecap", linecap)

    def set_fill_color(self, fill_color: str) -> Self:
        return self.set_attribute("fill", fill_color)
