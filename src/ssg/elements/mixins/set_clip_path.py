from typing import Self
from ssg.svg_element import SVGElement


class SetClipPathMixin(SVGElement):
    def set_clip_path(self, clip_path: str) -> Self:
        return self.set_attribute("clip-path", clip_path)
