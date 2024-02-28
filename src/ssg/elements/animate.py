from typing import Self
from ssg.svg_element import SVGElement


class animate(SVGElement):
    def set_attribute_name(self, attribute_name: str) -> Self:
        return self.set_attribute("attributeName", attribute_name)

    def set_values(self, values: str) -> Self:
        return self.set_attribute("values", values)

    def set_duration(self, dur: str) -> Self:
        return self.set_attribute("dur", dur)

    def set_repeat_count(self, repeat_count: str) -> Self:
        return self.set_attribute("repeatCount", repeat_count)
