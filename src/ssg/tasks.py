import importlib
import os
import tempfile
from invoke import task

from ssg.svg_element import SVGElement


@task
def gen(c, name, show=False):
    try:
        module = importlib.import_module(name)
    except ModuleNotFoundError:
        module = importlib.import_module(f"ssg.{name}")
    svg_element: SVGElement = getattr(module, "gen")()
    if show:
        svg_filename = tempfile.mktemp(".svg")
        with open(svg_filename, "wt") as f:
            f.write(svg_element.pretty_xml)
        os.system(f"open {svg_filename}")
    else:
        print(svg_element.pretty_xml)
