from simple_svg_generator.elements.g import g
from simple_svg_generator.elements.path import path
from simple_svg_generator.elements.svg import svg
from simple_svg_generator.svg_element import SVGElement


def test_svg_element():
    e = SVGElement("svg")
    ee = SVGElement("g")
    assert e._element.tagName == "svg"
    assert e.xml == "<svg/>"
    assert e.pretty_xml == "<svg/>\n"
    e.add_child(ee)
    assert len(e._element.childNodes) == 1
    assert e._element.childNodes[0].tagName == "g"
    assert e.xml == "<svg><g/></svg>"
    assert (
        e.pretty_xml
        == """<svg>
\t<g/>
</svg>
"""
    )


def test_set_attributes():
    e = SVGElement("svg")
    e.set_attributes({"a": "b", "c": "d"})
    assert e._element.attributes["a"].value == "b"
    assert e._element.attributes["c"].value == "d"
    e["x"] = "y"
    assert e._element.attributes["x"].value == "y"
    assert e["x"] == "y"


def test_svg():
    s = svg()
    assert s._element.tagName == "svg"
    assert s["width"] == "0"
    assert s["height"] == "0"
    s.set_dimensions("100", "200")
    assert s["width"] == "100"
    assert s["height"] == "200"
    assert s["xmlns"] == "http://www.w3.org/2000/svg"
    s.set_view_box("0 1 2 3")
    assert s["viewBox"] == "0 1 2 3"


def test_g():
    ge = g()
    assert ge._element.tagName == "g"
    ge.add_transform("rotate(4, 5, 6)")
    assert ge["transform"] == "rotate(4, 5, 6)"
    ge.set_transform("rotate(1, 2, 3)")
    assert ge["transform"] == "rotate(1, 2, 3)"
    ge.add_transform("scale(0.5)")
    assert ge["transform"] == "rotate(1, 2, 3) scale(0.5)"


def test_path():
    p = path()
    assert p._element.tagName == "path"
    p.set_transform("rotate(1, 2, 3)")
    assert p["transform"] == "rotate(1, 2, 3)"
    p.set_definition("M 1 2")
    assert p["d"] == "M 1 2"
    p.set_stroke_color("red")
    assert p["stroke"] == "red"
    p.set_stroke_width("3")
    assert p["stroke-width"] == "3"
    p.set_fill_color("blue")
    assert p["fill"] == "blue"
