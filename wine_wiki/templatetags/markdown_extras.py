"""
Template tags for markdown
"""

import markdown as md
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def markdown(mkdwn: str):
    """
    template filter for parsing markdown.
    """

    # re to enable correct markdown parsing

    html = md.markdown(mkdwn, extensions=[])

    return html
