# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""Code-Prism shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin

def convert2Num(string):
    try:
        num = int(string)
    except Exception:
        num = None

    return num

class Plugin(ShortcodePlugin):
    """Plugin for code directive."""

    name = "figure"

    def handler(self, src, width=None, height=None, align=None, alt=None, scale=None, css=None, site=None, data=None, lang=None, post=None):
        """Create HTML for figure."""

        output = '<div class="figure img-responsive '

        if css:
            output += '{} '.format(css)

        if not align:
            align = "left"
        output += 'align-{}"> '.format(align)

        if not alt:
            alt = src

        output += '<img alt="{0}" src="{1}" '.format(alt, src)

        if width or height:
            if scale:
                if "%" in scale:
                    scale = convert2Num(scale.split("%")[0])
                if width:
                    width = convert2Num(width)
                    if scale and width:
                        width *= (scale / 100.0 )
                if height:
                    height = convert2Num(height)
                    if scale and height:
                        height *= (scale / 100.0 )
        if width or height:
            output += 'style="'
            if width:
                output += 'width: {}px; '.format(width)
            if height:
                output += 'height: {}px; '.format(height)

        output += '"> </div>'

        return output, []
