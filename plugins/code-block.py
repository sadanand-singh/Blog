# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""Code-Prism shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin


class Plugin(ShortcodePlugin):
    """Plugin for code-block directive."""

    name = "code-block"

    def handler(self, code, lines=None, hl=None, offset=None, start=None, site=None, data=None, lang=None, post=None):
        """Create HTML for code-blocks."""

        output = '<pre'

        if lines and lines.lower() in ['true', '1', 't', 'y', 'yes']:
            lines = True
        else:
            lines = False

        if lines:
            output += ' class="line-numbers {}" '.format(lines)
            if start:
                output += ' data-start="{}" '.format(start)
        if hl:
            output += ' data-line="{}"" '.format(hl)
            if offset:
                output += 'data-line-offset="{}" '.format(offset)

        output += '> <code class="language-{0}">{1}</code></pre>'.format(code, data.strip())

        return output, []