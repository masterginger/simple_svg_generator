from xml.dom.minidom import Element
from simple_svg_generator import generate_svg_element
from simple_svg_generator.elements.g import g
from simple_svg_generator.elements.path import path
from simple_svg_generator.elements.svg import svg
from simple_svg_generator.svg_element import SVGElement


def sun() -> SVGElement:
    path1 = path()
    path1.set_attributes(
        dict(
            d="m12 0l-4 4h-5v5l-3 3 3 3v6h6l3 3 3-3h6v-6l3-3-3-3v-5h-5l-4-4z",
            transform="translate(0 1028.4)",
            fill="#f39c12",
        )
    )
    path2 = path()
    path2.set_attributes(
        dict(
            d="m24 13c0 6.075-5.149 11-11.5 11-6.3513 0-11.5-4.925-11.5-11 0-6.0751 5.1487-11 11.5-11 6.351 0 11.5 4.9249 11.5 11z",
            transform="matrix(.78261 0 0 .81818 2.2174 1029.7)",
            fill="#f1c40f",
        )
    )
    path_group = g()
    path_group.add_child(path1)
    path_group.add_child(path2)
    transform = g()
    transform.set_attributes(dict(transform="translate(0 -1028.4)"))
    transform.add_child(path_group)
    s = svg("800px", "800px")
    s.set_view_box("0 0 24 24")
    s.add_child(transform)
    return s
