from xml.dom.minidom import (
    DOMImplementation,
    Element,
    getDOMImplementation,
)
from typing import Dict, List, cast


def generate_svg_element(
    tag_name: str,
    attributes: Dict[str, str] = {},
    children: List[Element] = [],
) -> Element:
    # Use cast to force non-null typing.
    impl = cast(DOMImplementation, getDOMImplementation())
    element = impl.createDocument(None, "doc", None).createElement(tag_name)
    for key, value in attributes.items():
        element.attributes[key] = value
    for child in children:
        element.appendChild(child)
    return element
