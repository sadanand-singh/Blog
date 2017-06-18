# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""figure shortcode."""

import requests
import re

from nikola.plugin_categories import ShortcodePlugin

def convert2Num(string):
    try:
        num = int(string)
    except Exception:
        num = None

    return num

def extractScale(quantity):
    newNum = convert2Num(quantity)
    unit = "px"
    if newNum:
        unit = "px"
        quantity = newNum
    else:
        matchObj = re.match( r'(\s*\d+)\s*(.+)', quantity, re.M|re.I)
        if matchObj:
            quantity = matchObj.group(1)
            unit = matchObj.group(2)
            unit = unit.lower()
            if unit not in ["pt", "px"]:
                unit = "px"

    return quantity, unit

class Plugin(ShortcodePlugin):
    """Plugin for figure directive."""

    name = "figure"

    def handler(self, src, width=None, height=None, align=None, alt=None, scale=None, css=None, responsive=None, site=None, data=None, lang=None, post=None):
        """Create HTML for figure."""

        output = '<div class="figure img-responsive '

        if responsive:
            output = '<div class="figure '

        if css:
            output += '{} '.format(css)

        if align:
            output += 'align-{}'.format(align)

        output = output.strip() + '"> '

        if not alt:
            alt = src

        output += '<img alt="{0}" src="{1}" '.format(alt, src)

        wunit = None
        hunit = None

        if width or height:
            # first check if it just number of has units
            if width:
                width, wunit = extractScale(width)
            if height:
                height, hunit = extractScale(height)
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
                output += 'width: {0}{1}; '.format(width, wunit.strip())
            if height:
                output += 'height: {0}{1}; '.format(height, hunit.strip())
            output += '"'

        output = output.strip() + '> </div>'

        return output, []
