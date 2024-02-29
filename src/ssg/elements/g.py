from ssg.elements.mixins.set_clip_path import SetClipPathMixin
from ssg.elements.mixins.transform import TransformMixin
from ssg.svg_element import SVGElement


class g(TransformMixin, SetClipPathMixin, SVGElement):
    @staticmethod
    def fit(
        source_width: float,
        source_height: float,
        target_width: float,
        target_height: float,
        source_element: SVGElement,
        additional_scale: float = 1,
        rotation: float = 0,
    ) -> "g":
        sx = target_width / source_width
        sy = target_height / source_height
        inner = g().scale(sx, sy).add_child(source_element)
        return (
            g()
            .set_transform_origin(f"{target_width / 2} {target_height / 2}")
            .scale(additional_scale)
            .rotate(rotation)
            .add_child(inner)
        )

    @staticmethod
    def translate_wrapper(tx: float, ty: float, source_element: SVGElement) -> "g":
        return g().translate(tx, ty).add_child(source_element)
