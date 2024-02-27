import copy
from typing import Dict, Optional, Self, cast
from xml.dom import getDOMImplementation
from xml.dom.minidom import DOMImplementation


class SVGElement:
    xml_doc = cast(DOMImplementation, getDOMImplementation()).createDocument(
        None, "svg_doc", None
    )

    def __init__(self, tag_name: Optional[str] = None) -> None:
        self._element = self.__class__.xml_doc.createElement(
            tag_name if tag_name else self.__class__.__name__
        )

    def __getitem__(self, key: str) -> str:
        return self._element.attributes[key].value

    def set_attributes(self, attributes: Dict[str, str]) -> Self:
        new = copy.deepcopy(self)
        for key, value in attributes.items():
            new._element.attributes[key] = value
        return new

    def set_attribute(self, key: str, value: str) -> Self:
        new = copy.deepcopy(self)
        new._element.attributes[key] = value
        return new

    def add_child(self, element: "SVGElement") -> Self:
        new = copy.deepcopy(self)
        new._element.appendChild(element._element)
        return new

    @property
    def xml(self) -> str:
        return self._element.toxml()

    @property
    def pretty_xml(self) -> str:
        return self._element.toprettyxml()
