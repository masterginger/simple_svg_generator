from ssg.elements.animate import animate
from ssg.elements.animateTransform import animateTransform
from ssg.elements.mixins.set_id import SetIdMixin
from ssg.elements.mixins.stroke_fill import StrokeFillMixin
from ssg.elements.mixins.transform import TransformMixin
from ssg.elements.path import path
from ssg.elements.svg import svg
from utils import verify_set_attribute


def test_path():
    p = path()
    verify_set_attribute(p, "definition", "d")


def test_animate():
    a = animate()
    verify_set_attribute(a, "attribute_name", "attributeName")
    verify_set_attribute(a, "values", "values")
    verify_set_attribute(a, "duration", "dur")
    verify_set_attribute(a, "repeat_count", "repeatCount")


def test_animate_transform():
    a = animateTransform()
    verify_set_attribute(a, "from", "from")
    verify_set_attribute(a, "to", "to")
    verify_set_attribute(a, "by", "by")
    verify_set_attribute(a, "type", "type")


def test_svg():
    s = svg()
    verify_set_attribute(s, "view_box", "viewBox")


def test_transform_mixin():
    t = TransformMixin()
    verify_set_attribute(t, "transform", "transform")
    verify_set_attribute(t, "transform_origin", "transform-origin")


def test_set_id_mixin():
    s = SetIdMixin()
    verify_set_attribute(s, "id", "id")


def test_stroke_fill_mixin():
    s = StrokeFillMixin()
    verify_set_attribute(s, "stroke_color", "stroke")
    verify_set_attribute(s, "stroke_width", "stroke-width")
    verify_set_attribute(s, "stroke_linecap", "stroke-linecap")
    verify_set_attribute(s, "fill_color", "fill")
