import pytest
from ssg.elements.g import g
from ssg.elements.path import path
from ssg.elements.svg import svg
from ssg.elements.text import text
from ssg.svg_element import SVGElement
from ssg.svg_snippet import SVGSnippet
from unittest.mock import patch


def test_svg_snippet():
    s = SVGSnippet('<g transform="scale(0.5)"><path/></g>')
    assert s._element is not None
    assert s._tag_name == "g"
    assert s["transform"] == "scale(0.5)"
    with pytest.raises(NotImplementedError):
        s._copy()
    with pytest.raises(NotImplementedError):
        s.add_child(g())
    with pytest.raises(NotImplementedError):
        s.set_attribute("a", "b")
    with pytest.raises(NotImplementedError):
        s.set_attributes(dict(c="d"))

    ge = g().add_child(s)
    assert ge.xml == '<g><g transform="scale(0.5)"><path/></g></g>'


def test_svg_element():
    e = SVGElement("svg")
    ee = SVGElement("g")
    assert e._tag_name == "svg"
    assert e.xml == "<svg/>"
    assert e.pretty_xml == "<svg/>\n"
    e = e.add_child(ee)
    assert len(e._children) == 1
    assert e._children[0]._tag_name == "g"
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
    e = e.set_attributes({"a": "b", "c": "d"})
    assert e._attributes["a"] == "b"
    assert e._attributes["c"] == "d"
    e = e.set_attribute("x", "y")
    assert e._attributes["x"] == "y"
    assert e["x"] == "y"


def test_svg():
    s = svg()
    assert s._tag_name == "svg"
    with pytest.raises(KeyError):
        s["width"]
    with pytest.raises(KeyError):
        s["height"]
    s = s.set_dimensions("100", "200")
    assert s["width"] == "100"
    assert s["height"] == "200"
    assert s["xmlns"] == "http://www.w3.org/2000/svg"
    s = s.set_view_box("0 1 2 3")
    assert s["viewBox"] == "0 1 2 3"


def test_g():
    ge = g()
    assert ge._tag_name == "g"
    ge = ge.rotate(4, 5, 6)
    assert ge["transform"] == "rotate(4, 5, 6)"
    ge = ge.set_transform("rotate(1, 2, 3)")
    assert ge["transform"] == "rotate(1, 2, 3)"
    ge = ge.add_transform("scale(0.5)")
    assert ge["transform"] == "rotate(1, 2, 3) scale(0.5)"
    ge = ge.translate(1, 2)
    assert ge["transform"] == "rotate(1, 2, 3) scale(0.5) translate(1, 2)"
    ge = ge.set_clip_path("abc")
    assert ge["clip-path"] == "abc"
    ge = ge.set_transform_origin("center")
    assert ge["transform-origin"] == "center"
    ge = ge.rotate(7)
    assert ge["transform"] == "rotate(1, 2, 3) scale(0.5) translate(1, 2) rotate(7)"


def test_g_fit():
    fit = g.fit(10, 20, 4, 5, path(), additional_scale=0.5, rotation=3)
    assert (
        fit.xml
        == '<g transform-origin="2.0 2.5" transform="scale(0.5) rotate(3)"><g transform="scale(0.4, 0.25)"><path/></g></g>'
    )


def test_g_translate_wrapper():
    t = g.translate_wrapper(10, 20, g())
    assert t.xml == '<g transform="translate(10, 20)"><g/></g>'


def test_path():
    p = path()
    assert p._tag_name == "path"
    p = p.set_transform("rotate(1, 2, 3)")
    assert p["transform"] == "rotate(1, 2, 3)"
    p = p.set_definition("M 1 2")
    assert p["d"] == "M 1 2"
    p = p.set_stroke_color("red")
    assert p["stroke"] == "red"
    p = p.set_stroke_width("3")
    assert p["stroke-width"] == "3"
    p = p.set_stroke_linecap("round")
    assert p["stroke-linecap"] == "round"
    p = p.set_fill_color("blue")
    assert p["fill"] == "blue"


def test_text():
    # Plain text:
    t = text("abc").set_font_family("Menlo").set_font_size("10")
    assert t.xml == '<text font-family="Menlo" font-size="10">abc</text>'

    # Text path
    with patch("uuid.uuid4", lambda: "abc123"):
        t = (
            text("abc", path().set_definition("M 0 1 L 2 3"))
            .set_font_family("Menlo")
            .set_font_size("10")
        )
        assert (
            t.xml
            == '<text font-family="Menlo" font-size="10"><path d="M 0 1 L 2 3" id="abc123"/><textPath href="#abc123" startOffset="50%" text-anchor="middle">abc</textPath></text>'
        )
