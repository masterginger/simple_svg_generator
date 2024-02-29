from typing import Dict, Self, cast
from xml.dom.minidom import Element, parseString
from ssg.svg_element import SVGElement


class SVGSnippet(SVGElement):
    def __init__(self, svg_snippet: str) -> None:
        self._cached_element = cast(Element, parseString(svg_snippet).documentElement)
        self._svg_snippet = svg_snippet
        super().__init__("__snippet__")

    def _build_element(self) -> Element:
        return cast(Element, parseString(self._svg_snippet).documentElement)

    def _copy(self) -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")

    def __getitem__(self, key: str) -> str:
        return cast(Element, self._cached_element).attributes[key].value

    def set_attributes(self, attributes: Dict[str, str]) -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")

    def set_attribute(self, key: str, value: str) -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")

    def add_child(self, element: "SVGElement") -> Self:
        raise NotImplementedError("SVGSnippet is entirely immutable")
