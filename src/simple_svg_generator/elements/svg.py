from simple_svg_generator.svg_element import SVGElement


class svg(SVGElement):
    def __init__(self, width: str = "0", height: str = "0") -> None:
        super().__init__()
        self["xmlns"] = "http://www.w3.org/2000/svg"
        self.set_dimensions(width, height)

    def set_dimensions(self, width: str, height: str) -> None:
        self["width"] = width
        self["height"] = height

    def set_view_box(self, view_box) -> None:
        self["viewBox"] = view_box
