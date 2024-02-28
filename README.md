# simple_svg_generator
This is a simple helper library for generating SVGs.

# Why I'm doing this?
I created this tool for two main purposes:
1. I needed a library to conveniently create SVGs for illustrations in my posts.
2. I found this is an good opportunity to write something about creating a project from scratch and apply (some) design patterns to the technical design process.

Please find the series on [Medium](https://medium.masterginger.com/list/the-journey-to-a-simple-svg-generator-a18e0922608f).

# Getting started
## Install via pip
```
pip install git+https://github.com/masterginger/simple_svg_generator.git
```
(I currently don't have a plan to publish it to PyPI yet)

## See the demo
```
python -m ssg gen examples.heart --show
```

## Use it in your code
Create `sun.py`
```Python
from ssg.elements.g import g
from ssg.elements.path import path
from ssg.elements.svg import svg
from ssg.svg_element import SVGElement


def sun() -> SVGElement:
    path1 = (
        path()
        .set_definition("m12 0l-4 4h-5v5l-3 3 3 3v6h6l3 3 3-3h6v-6l3-3-3-3v-5h-5l-4-4z")
        .set_transform("translate(0 1028.4)")
        .set_fill_color("#f39c12")
    )
    path2 = (
        path()
        .set_definition(
            "m24 13c0 6.075-5.149 11-11.5 11-6.3513 0-11.5-4.925-11.5-11 0-6.0751 5.1487-11 11.5-11 6.351 0 11.5 4.9249 11.5 11z"
        )
        .set_transform("matrix(.78261 0 0 .81818 2.2174 1029.7)")
        .set_fill_color("#f1c40f")
    )
    path_group = g().add_child(path1).add_child(path2)
    transform = g().set_transform("translate(0 -1028.4)").add_child(path_group)
    s = (
        svg()
        .set_dimensions("800px", "800px")
        .set_view_box("0 0 24 24")
        .add_child(transform)
    )
    return s


if __name__ == "__main__":
    print(sun().pretty_xml)
```
Then
```
python sun.py > /tmp/sun.svg
open /tmp/sun.svg
```

Please feel free to let me know your questions, comments and feedback :)
