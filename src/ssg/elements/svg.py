from typing import Self
from ssg.svg_element import SVGElement


class svg(SVGElement):
    def __init__(self) -> None:
        super().__init__()
        self._attributes["xmlns"] = "http://www.w3.org/2000/svg"

    def set_dimensions(self, width: str, height: str) -> Self:
        return self.set_attributes(dict(width=width, height=height))

    def set_view_box(self, view_box) -> Self:
        return self.set_attribute("viewBox", view_box)
