from typing import Optional, Self
from ssg.elements.mixins.stroke_fill import StrokeFillMixin
from ssg.elements.mixins.transform import TransformMixin
from ssg.svg_element import SVGElement


class rect(TransformMixin, StrokeFillMixin, SVGElement):
    def set_radius(
        self, rx: Optional[float] = None, ry: Optional[float] = None
    ) -> Self:
        if rx is not None and ry is not None:
            return self.set_attributes(dict(rx=str(rx), ry=str(ry)))
        if rx is not None:
            return self.set_attributes(dict(rx=str(rx)))
        return self.set_attributes(dict(ry=str(ry)))

    def set_rect(self, x: float, y: float, width: float, height: float) -> Self:
        return self.set_attributes(
            dict(x=str(x), y=str(y), width=str(width), height=str(height))
        )
