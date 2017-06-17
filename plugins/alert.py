# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""alert shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin
from nikola.plugins.compile import markdown


class Plugin(ShortcodePlugin):
    """Plugin for alert directive."""

    name = "alert"

    def handler(self, signal="imfo", site=None, data=None, lang=None, post=None):
        """Create HTML for marker."""

        if signal.lower() not in ["warning", "danger", "info", "success"]:
            signal = "info"

        signal = signal.lower()

        compiler = markdown.CompileMarkdown()
        compiler.set_site(site)

        data, _ = compiler.compile_string(data)

        output = '<div class="alert alert-dismissible alert-${0}">${1}</div>'.format(signal, data.strip().lstrip('<p>').rstrip('</p>'))

        return output, []
