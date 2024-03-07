import cairosvg  # type: ignore
import importlib
import os
import tempfile
from invoke import task

from ssg.svg_element import SVGElement


@task
def gen(c, name, show=False, png=False, png_scale=1, args=""):
    try:
        module = importlib.import_module(name)
    except ModuleNotFoundError:
        module = importlib.import_module(f"ssg.{name}")
    svg_element: SVGElement = getattr(module, "gen")(args=args)
    if show:
        svg_filename = tempfile.mktemp(".svg")
        with open(svg_filename, "wt") as f:
            f.write(svg_element.pretty_xml)
        os.system(f"open {svg_filename}")
    elif png:
        svg_filename = tempfile.mktemp(".svg")
        png_filename = tempfile.mktemp(".png")
        with open(svg_filename, "wt") as f:
            f.write(svg_element.pretty_xml)
        cairosvg.svg2png(url=svg_filename, write_to=png_filename, scale=png_scale)
        os.system(f"open {png_filename}")
    else:
        print(svg_element.pretty_xml)
