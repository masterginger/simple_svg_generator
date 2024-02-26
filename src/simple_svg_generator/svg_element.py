from typing import Dict, Self, cast
from xml.dom import getDOMImplementation
from xml.dom.minidom import DOMImplementation, Document, Element


class SVGElement:
    xml_doc = cast(DOMImplementation, getDOMImplementation()).createDocument(
        None, "svg_doc", None
    )

    def __init__(self, tag_name: str) -> None:
        self._element = self.__class__.xml_doc.createElement(tag_name)

    def set_attributes(self, attributes: Dict[str, str]) -> None:
        for key, value in attributes.items():
            self._element.attributes[key] = value

    def __getitem__(self, key: str) -> str:
        return self._element.attributes[key].value

    def __setitem__(self, key: str, value: str) -> None:
        self._element.attributes[key] = value

    def add_child(self, element: "SVGElement") -> None:
        self._element.appendChild(element._element)

    @property
    def xml(self) -> str:
        return self._element.toxml()

    @property
    def pretty_xml(self) -> str:
        return self._element.toprettyxml()
