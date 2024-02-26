from typing import List


def generate_svg_element(
    element_markup: str, inner_element_markups: List[str] = []
) -> str:
    # Hacky way to figure out the tag name of the element
    tag_name = element_markup.split(" ")[0][1:]
    should_generate_closing_tag = len(inner_element_markups) > 0
    closing_tag = f"</{tag_name}>" if should_generate_closing_tag else ""
    return f"{element_markup}{''.join(inner_element_markups)}{closing_tag}"
