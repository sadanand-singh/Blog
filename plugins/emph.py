# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""emph shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin
from nikola.plugins.compile import markdown

def removePtags(data):
    data = data.replace("<p>", "", 1)
    li = data.rsplit("</p>", 1)
    data = "".join(li)

    return data

class Plugin(ShortcodePlugin):
    """Plugin for marker directive."""

    name = "emph"

    def handler(self, signal="primary", site=None, data=None, lang=None, post=None):
        """Create HTML for emphasis."""

        if signal.lower() not in ["muted", "primary", "warning", "danger", "success", "info"]:
            signal = "primary"

        signal = signal.lower()

        compiler = markdown.CompileMarkdown()
        compiler.set_site(site)

        data, _ = compiler.compile_string(data)
        data = removePtags(data.strip())

        output = '<p class="text-{0}">{1}</p>'.format(signal, data)

        return output, []
