from simple_svg_generator.svg_element import SVGElement
from simple_svg_generator.elements.mixins.transform import TransformMixin


class g(SVGElement, TransformMixin): ...
