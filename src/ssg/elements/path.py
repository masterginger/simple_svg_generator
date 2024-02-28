from typing import Self
from ssg.elements.mixins.transform import TransformMixin
from ssg.elements.mixins.stroke_fill import StrokeFillMixin
from ssg.svg_element import SVGElement


class path(TransformMixin, StrokeFillMixin, SVGElement):
    def set_definition(self, d: str) -> Self:
        return self.set_attribute("d", d)
