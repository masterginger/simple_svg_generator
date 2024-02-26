from simple_svg_generator.svg_element import SVGElement


class g(SVGElement):
    def set_transform(self, transform: str) -> None:
        self["transform"] = transform
