# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""panel shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin
from nikola.plugins.compile import markdown


def removePtags(data):
    data = data.replace("<p>", "", 1)
    li = data.rsplit("</p>", 1)
    data = "".join(li)

    return data


class Plugin(ShortcodePlugin):
    """Plugin for panel directive."""

    name = "panel"

    def handler(self, signal="primary", header="", footer="", site=None, data=None, lang=None, post=None):
        """Create HTML for marker."""

        if signal.lower() not in ["primary", "warning", "danger", "info", "success"]:
            signal = "primary"

        signal = signal.lower()

        compiler = markdown.CompileMarkdown()
        compiler.set_site(site)

        data, _ = compiler.compile_string(data)
        data = removePtags(data.strip())

        headTag = ""
        footTag = ""

        if header:
            header, _ = compiler.compile_string(header)
            header = removePtags(header.strip())
            headTag = '<div class="panel-heading">{}</div>'.format(header)

        if footer:
            footer, _ = compiler.compile_string(footer)
            footer = removePtags(footer.strip())
            footTag = '<div class="panel-footer">{}</div>'.format(footer)

        output = '<div class="alert alert-dismissible alert-{0}"> {1} </div>'.format(signal, data)

        output = '''
<div class="panel panel-{0}">
  {2}
  <div class="panel-body">
    {1}
  </div>
  {3}
</div>
'''.format(signal, data, headTag, footTag)

        return output, []
