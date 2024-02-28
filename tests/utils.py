from typing import Callable, cast
from ssg.svg_element import SVGElement


def verify_set_attribute(
    element: SVGElement, function_name: str, attribute_name: str
) -> None:
    function = cast(
        Callable[[str], SVGElement],
        getattr(element, f"set_{function_name}"),
    )
    value = "abc"
    new_object = function(value)
    assert new_object._attributes[attribute_name] == value
