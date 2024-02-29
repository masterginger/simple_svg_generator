from typing import Dict, Self, cast
from xml.dom.minidom import Element, parseString
from ssg.svg_element import SVGElement


class SVGSnippet(SVGElement):
    def __init__(self, svg_snippet: str) -> None:
        svg_element = cast(Element, parseString(svg_snippet).documentElement)
        super().__init__(svg_element.tagName)
        self._element = svg_element

    def _copy(self) -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")

    def __getitem__(self, key: str) -> str:
        return cast(Element, self._element).attributes[key].value

    def set_attributes(self, attributes: Dict[str, str]) -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")

    def set_attribute(self, key: str, value: str) -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")

    def add_child(self, element: "SVGElement") -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")
