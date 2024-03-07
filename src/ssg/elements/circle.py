from typing import Self
from ssg.elements.mixins.stroke_fill import StrokeFillMixin
from ssg.elements.mixins.transform import TransformMixin
from ssg.svg_element import SVGElement


class circle(TransformMixin, StrokeFillMixin, SVGElement):
    def set_center(self, x: float, y: float) -> Self:
        return self.set_attributes(dict(cx=str(x), cy=str(y)))

    def set_radius(self, r: float) -> Self:
        return self.set_attribute("r", str(r))
