from typing import Self
from simple_svg_generator.svg_element import SVGElement


class TransformMixin(SVGElement):
    def set_transform(self, transform: str) -> Self:
        return self.set_attribute("transform", transform)

    def add_transform(self, transform: str) -> Self:
        try:
            new_transform = f"{self['transform']} {transform}"
        except KeyError:
            new_transform = transform
        return self.set_attribute("transform", new_transform)
