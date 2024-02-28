import ssg


def test_generate_svg_element():
    children = [
        ssg.generate_svg_element(
            "rect", attributes=dict(x="10", y="20", width="30", height="40")
        ),
        ssg.generate_svg_element("circle", dict(cx="10", cy="20", r="30")),
    ]
    assert (
        ssg.generate_svg_element(
            "svg",
            dict(width="100", height="200", xmlns="http://www.w3.org/2000/svg"),
            children=children,
        ).toxml()
        == """<svg width="100" height="200" xmlns="http://www.w3.org/2000/svg">"""
        + """<rect x="10" y="20" width="30" height="40"/>"""
        + """<circle cx="10" cy="20" r="30"/>"""
        + """</svg>"""
    )
