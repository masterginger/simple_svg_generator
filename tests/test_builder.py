from ssg.svg_element import SVGElement


def test_builder_attributes():
    e = SVGElement("svg")
    assert e._element is None
    new = e.set_attribute("a", "b")
    assert new._element is None
    assert id(new) != id(e)
    assert e.xml == "<svg/>"
    assert new.xml == '<svg a="b"/>'


def test_builder_children():
    e = SVGElement("svg")
    ee = SVGElement("g")
    eee = e.add_child(ee)
    assert e._element is None
    assert eee.xml == "<svg><g/></svg>"
