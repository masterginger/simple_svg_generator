from simple_svg_generator.elements.g import g
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


def test_g():
    ge = g()
    assert ge._element.tagName == "g"
