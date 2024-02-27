from simple_svg_generator.elements.g import g
from simple_svg_generator.elements.path import path
from simple_svg_generator.elements.svg import svg
from simple_svg_generator.svg_element import SVGElement


def sun() -> SVGElement:
    path1 = path()
    path1 = path1.set_definition(
        "m12 0l-4 4h-5v5l-3 3 3 3v6h6l3 3 3-3h6v-6l3-3-3-3v-5h-5l-4-4z"
    )
    path1 = path1.set_transform("translate(0 1028.4)")
    path1 = path1.set_fill_color("#f39c12")
    path2 = path()
    path2 = path2.set_definition(
        "m24 13c0 6.075-5.149 11-11.5 11-6.3513 0-11.5-4.925-11.5-11 0-6.0751 5.1487-11 11.5-11 6.351 0 11.5 4.9249 11.5 11z"
    )
    path2 = path2.set_transform("matrix(.78261 0 0 .81818 2.2174 1029.7)")
    path2 = path2.set_fill_color("#f1c40f")
    path_group = g()
    path_group = path_group.add_child(path1)
    path_group = path_group.add_child(path2)
    transform = g()
    transform = transform.set_transform("translate(0 -1028.4)")
    transform = transform.add_child(path_group)
    s = svg()
    s = s.set_dimensions("800px", "800px")
    s = s.set_view_box("0 0 24 24")
    s = s.add_child(transform)
    return s
