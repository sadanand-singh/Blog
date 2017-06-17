# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""label shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin
from nikola.plugins.compile import markdown

def removePtags(data):
    data = data.replace("<p>", "", 1)
    li = data.rsplit("</p>", 1)
    data = "".join(li)

    return data

class Plugin(ShortcodePlugin):
    """Plugin for label directive."""

    name = "label"

    def handler(self, signal="default", site=None, data=None, lang=None, post=None):
        """Create HTML for label."""

        if signal.lower() not in ["default", "primary", "warning", "danger", "success", "info"]:
            signal = "default"

        signal = signal.lower()

        compiler = markdown.CompileMarkdown()
        compiler.set_site(site)

        data, _ = compiler.compile_string(data)
        data = removePtags(data.strip())

        output = '<span class="label label-{0}">{1}</span>'.format(signal, data)

        return output, []
