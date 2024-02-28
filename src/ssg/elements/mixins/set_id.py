from typing import Self
from ssg.svg_element import SVGElement


class SetIdMixin(SVGElement):
    def set_id(self, id: str) -> Self:
        return self.set_attribute("id", id)
