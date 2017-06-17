# -*- coding: utf-8 -*-
# This file is public domain according to its author, Sadanand Singh

"""Marker shortcode."""

import requests

from nikola.plugin_categories import ShortcodePlugin


class Plugin(ShortcodePlugin):
    """Plugin for marker directive."""

    name = "marker"

    def handler(self, signal="warning", site=None, data=None, lang=None, post=None):
        """Create HTML for marker."""

        if signal.lower() not in ["error", "warning", "red", "yellow", "green", "cyan", "blue", "purple"]:
            signal = "warning"

        signal = signal.lower()

        output = '<span class="highlight-short-{0}"> {1} </span>'.format(signal, data.strip())

        return output, []