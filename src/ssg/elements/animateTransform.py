from typing import Self

from ssg.elements.animate import animate


class animateTransform(animate):
    def __init__(self) -> None:
        super().__init__()
        self._attributes["attributeName"] = "transform"
        self._attributes["attributeType"] = "XML"

    def set_from(self, from_value: str) -> Self:
        return self.set_attribute("from", from_value)

    def set_to(self, to: str) -> Self:
        return self.set_attribute("to", to)

    def set_by(self, by: str) -> Self:
        return self.set_attribute("by", by)

    def set_type(self, type_value: str) -> Self:
        return self.set_attribute("type", type_value)
