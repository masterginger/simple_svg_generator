from xml.dom.minidom import parseString, Element
from typing import List


def generate_svg_element(element_markup: str, children: List[Element] = []) -> Element:
    element = parseString(element_markup).documentElement
    for child in children:
        element.appendChild(child)
    return element
