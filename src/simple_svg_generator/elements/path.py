from simple_svg_generator.svg_element import SVGElement


class path(SVGElement):
    def set_definition(self, d: str) -> None:
        self["d"] = d

    def set_transform(self, transform: str) -> None:
        self["transform"] = transform
