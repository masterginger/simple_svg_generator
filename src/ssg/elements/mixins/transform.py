from typing import Optional, Self
from ssg.svg_element import SVGElement


class TransformMixin(SVGElement):
    def set_transform(self, transform: str) -> Self:
        return self.set_attribute("transform", transform)

    def translate(self, tx: float, ty: float) -> Self:
        return self.add_transform(f"translate({tx}, {ty})")

    def scale(self, sx: float, sy: Optional[float] = None) -> Self:
        if sy is not None:
            return self.add_transform(f"scale({sx}, {sy})")
        return self.add_transform(f"scale({sx})")

    def set_transform_origin(self, origin: str) -> Self:
        return self.set_attribute("transform-origin", origin)

    def add_transform(self, transform: str) -> Self:
        try:
            new_transform = f"{self['transform']} {transform}"
        except KeyError:
            new_transform = transform
        return self.set_attribute("transform", new_transform)
