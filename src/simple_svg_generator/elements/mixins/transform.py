from typing import List, Protocol
from simple_svg_generator.elements.mixins.set_attribute_protocol import (
    SetAttributeProtocol,
)


class TransformMixin(SetAttributeProtocol):
    _transforms: List[str]

    def set_transform(self, transform: str) -> None:
        self._transforms: List[str] = []
        self.add_transform(transform)

    def add_transform(self, transform: str) -> None:
        if not hasattr(self, "_transforms"):
            self._transforms = []
        self._transforms.append(transform)
        self["transform"] = " ".join(self._transforms)
