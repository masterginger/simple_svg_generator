from typing import Self
import uuid
from xml.dom.minidom import Element
from ssg.elements.path import path
from ssg.svg_element import SVGElement


class text(SVGElement):
    def __init__(self, text: str, text_path: path | None = None) -> None:
        super().__init__("text")
        self._text = text
        if text_path is not None:
            text_path_uuid = str(uuid.uuid4())
            text_path_element = (
                SVGElement("textPath")
                .set_attributes(
                    dict(
                        href=f"#{text_path_uuid}",
                        startOffset="50%",
                    )
                )
                .set_attribute("text-anchor", "middle")
            )
            self._children.append(text_path.set_attribute("id", text_path_uuid))
            self._children.append(text_path_element)

    def _build_element(self) -> Element:
        text_node = self.__class__.xml_doc.createTextNode(self._text)
        element = super()._build_element()
        if len(self._children) == 0:
            # Plain text
            element.appendChild(text_node)
        else:
            # The second child is the textPath element
            element.childNodes[1].appendChild(text_node)

        return element

    def _copy(self) -> Self:
        copied = super()._copy()
        copied._text = self._text
        return copied

    def set_font_family(self, font_family: str) -> Self:
        return self.set_attribute("font-family", font_family)

    def set_font_size(self, font_size: str) -> Self:
        return self.set_attribute("font-size", font_size)
