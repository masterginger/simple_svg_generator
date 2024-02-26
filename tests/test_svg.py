import simple_svg_generator


def test_generate_svg_element():
    children = [
        simple_svg_generator.generate_svg_element(
            '<rect x="10" y="20" width="30" height="40" />'
        ),
        simple_svg_generator.generate_svg_element('<circle cx="10" cy="20" r="30" />'),
    ]
    assert (
        simple_svg_generator.generate_svg_element(
            '<svg width="100" height="200" xmlns="http://www.w3.org/2000/svg" />',
            children=children,
        ).toxml()
        == """<svg xmlns="http://www.w3.org/2000/svg" width="100" height="200">"""
        + """<rect x="10" y="20" width="30" height="40"/>"""
        + """<circle cx="10" cy="20" r="30"/>"""
        + """</svg>"""
    )
