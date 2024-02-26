import simple_svg_generator


def test_generate_svg_element():
    inner_markups = [
        simple_svg_generator.generate_svg_element(
            '<rect x="10" y="20" width="30" height="40" />'
        ),
        simple_svg_generator.generate_svg_element('<circle cx="10" cy="20" r="30" />'),
    ]
    assert (
        simple_svg_generator.generate_svg_element(
            '<svg width="100" height="200" xmlns="http://www.w3.org/2000/svg">',
            inner_element_markups=inner_markups,
        )
        == """<svg width="100" height="200" xmlns="http://www.w3.org/2000/svg">"""
        + """<rect x="10" y="20" width="30" height="40" />"""
        + """<circle cx="10" cy="20" r="30" />"""
        + """</svg>"""
    )
