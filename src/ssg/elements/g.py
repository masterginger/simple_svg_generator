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
        additional_scale: float,
        source_element: SVGElement,
    ) -> "g":
        sx = target_width / source_width
        sy = target_height / source_height
        inner = (
            g()
            .set_transform_origin("center")
            .scale(additional_scale)
            .add_child(source_element)
        )
        return g().scale(sx, sy).add_child(inner)
