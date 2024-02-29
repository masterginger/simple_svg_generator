import copy
from typing import Dict, List, Optional, Self, cast
from xml.dom import getDOMImplementation
from xml.dom.minidom import DOMImplementation, Element


class SVGElement:
    xml_doc = cast(DOMImplementation, getDOMImplementation()).createDocument(
        None, "svg_doc", None
    )

    def __init__(self, tag_name: Optional[str] = None) -> None:
        self._attributes: Dict[str, str] = {}
        self._tag_name = tag_name if tag_name else self.__class__.__name__
        self._children: List["SVGElement"] = []

    def _copy(self) -> Self:
        new: Self = copy.copy(self)
        new._attributes = copy.copy(self._attributes)
        new._children = copy.copy(self._children)
        return new

    def __getitem__(self, key: str) -> str:
        return self._attributes[key]

    def set_attributes(self, attributes: Dict[str, str]) -> Self:
        new = self._copy()
        new._attributes.update(attributes)
        return new

    def set_attribute(self, key: str, value: str) -> Self:
        new = self._copy()
        new._attributes[key] = value
        return new

    def add_child(self, element: "SVGElement") -> Self:
        new = self._copy()
        new._children.append(element)
        return new

    def _build_element(self) -> Element:
        element = self.__class__.xml_doc.createElement(self._tag_name)
        for key, value in self._attributes.items():
            element.attributes[key] = value
        for child in self._children:
            element.appendChild(child._build_element())
        return element

    @property
    def xml(self) -> str:
        return self._build_element().toxml()

    @property
    def pretty_xml(self) -> str:
        return self._build_element().toprettyxml()
