from xml.dom.minidom import Element
from simple_svg_generator import generate_svg_element


def sun() -> Element:
    paths = [
        generate_svg_element(
            "path",
            attributes=dict(
                d="m12 0l-4 4h-5v5l-3 3 3 3v6h6l3 3 3-3h6v-6l3-3-3-3v-5h-5l-4-4z",
                transform="translate(0 1028.4)",
                fill="#f39c12",
            ),
        ),
        generate_svg_element(
            "path",
            attributes=dict(
                d="m24 13c0 6.075-5.149 11-11.5 11-6.3513 0-11.5-4.925-11.5-11 0-6.0751 5.1487-11 11.5-11 6.351 0 11.5 4.9249 11.5 11z",
                transform="matrix(.78261 0 0 .81818 2.2174 1029.7)",
                fill="#f1c40f",
            ),
        ),
    ]
    path_group = generate_svg_element(
        "g",
        children=paths,
    )
    transform = generate_svg_element(
        "g",
        attributes=dict(transform="translate(0 -1028.4)"),
        children=[path_group],
    )
    return generate_svg_element(
        "svg",
        attributes=dict(
            width="800px",
            height="800px",
            viewBox="0 0 24 24",
            xmlns="http://www.w3.org/2000/svg",
        ),
        children=[transform],
    )
