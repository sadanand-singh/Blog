# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""Code-Prism shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin


class Plugin(ShortcodePlugin):
    """Plugin for code directive."""

    name = "code"

    def handler(self, code, site=None, data=None, lang=None, post=None):
        """Create HTML for gist."""

        output = '<code>{}</code></pre>'.format(code)

        return output, []