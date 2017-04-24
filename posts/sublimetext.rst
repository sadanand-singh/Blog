.. title: Sublime Text Setup
.. slug: sublimetext
.. date: 2017-04-23 16:57:07 UTC-07:00
.. tags: Sublime Text, Editor
.. category: Tools
.. link:
.. description:
.. type: text
.. disqus_identifier: sublimetext.sadanand
.. author: Sadanand Singh

My Sublime Text Setup
~~~~~~~~~~~~~~~~~~~~~~~~

I have been using `Sublime text <https://www.sublimetext.com/>`__ as my primary editor for some time now. Here I wanted to share my current setup for the editor including all settings, packages, shortcut keys and themes.

.. TEASER_END

.. figure:: https://cloud.githubusercontent.com/assets/8487569/25318834/053f9e98-284b-11e7-83e7-c2f1ee945980.png
   :alt: Sublime Text

Packages
~~~~~~~~~

First thing you will need to install is the `Package Control <https://packagecontrol.io>`__. This can be easily done by following the
directions at their installation `instructions <https://packagecontrol.io/installation>`__.

Once you have installed the package manager and restarted sublime text, now you
can install all other packages using the powerful command pallet. Hit *ctrl +
shift + P* and type *"Install"*, choose *"Package Control : Install Package"*.
Now you can search for any package that you wish to install, and then press
*Enter* to install it.

Here is a list of packages that I currently use:

-  `Alignment <https://github.com/wbond/sublime_alignment>`__
-  `Bracket Highlighter <https://github.com/facelessuser/BracketHighlighter>`__
-  `C++11 <https://github.com/noct/sublime-cpp11>`__
-  `Column Select <https://github.com/ehuss/Sublime-Column-Select>`__
-  `DocBlockr_Python <https://github.com/adambullmer/sublime_docblockr_python>`__
-  `GitGutter <https://github.com/jisaacks/GitGutter>`__
-  `MagicPython <https://github.com/MagicStack/MagicPython>`__
-  `rsub <https://github.com/henrikpersson/rsub>`__
-  `Search In Project <https://github.com/leonid-shevtsov/SearchInProject_SublimeText>`__
-  `SublimeLinter <https://github.com/SublimeLinter/SublimeLinter3>`__
-  `SublimeLinter-flake8 <https://github.com/SublimeLinter/SublimeLinter-flake8>`__

**Alignment** provides a simple key-binding for aligning multi-line and multiple
selections. **Bracket Highlighter**, as the name suggests, matches a variety of
brackets such as: [], (), {}, "", '', #!xml <tag></tag>, and even custom
brackets. **C++11** provides better coloring scheme for c++11 syntax.

**Column Select** plug-in provides an alternate behavior for Sublime keyboard
column selection. The differences are:

-  Allows reversing direction (go down too far, just go back up).
-  Added PageUp/PageDown, Home/End, and mouse selection.
-  Skip rows that are too short.
-  If you start at the end of a line, then it will stay at the end of each line.

**DocBlockr_Python** makes writing documentation a breeze for python code.
**GitGutter** is a handy plug-in to show information about files in a git
repository. Main Features are:

-  Gutter Icons indicating inserted, modified or deleted lines
-  Diff Popup with details about modified lines
-  Status Bar Text with information about file and repository
-  Jumping Between Changes to easily navigate between modified lines

**MagicPython** is a package with preferences and syntax highlighter for cutting
edge Python 3. It is meant to be a drop-in replacement for the default Python
package. MagicPython correctly highlights all Python 3.5 and 3.6 syntax
features, including type annotations, f-strings and regular expressions. It is
built from scratch for robustness with an extensive test suite.

**rsub** is an implementation of TextMate 2's 'rmate' feature for Sublime Text,
allowing files to be edited on a remote server using SSH port forwarding /
tunneling. Please make sure you have installed a version of
`rmate <https://github.com/aurora/rmate>`__ and are using correct
`port forwarding <https://atom.io/packages/remote-atom>`__.

**Search in Project** lets you use your favorite search tool (grep, ack, ag,
pt, rg, git grep, or findstr) to find strings across your entire current Sublime
Text project. I personally use
`the silver_seracher <https://geoff.greer.fm/ag/>`__ (ag) for this purpose.

**SublimeLinter** and **SublimeLinter-flake8** is plug-in that provides an
interface to `flake8 <http://flake8.pycqa.org/en/latest/>`__.
It will be used with files that have the “Python” syntax.

Shortcut Keys
~~~~~~~~~~~~~~~

Here is a summary of my user-defined key map:

.. code:: json

    [
        { "keys": ["shift+alt+a"], "command": "find_all_under" },
        { "keys": ["control+v"], "command": "paste_and_indent" },
        { "keys": ["control+shift+v"], "command": "paste" },
        { "keys": ["ctrl+alt+;"], "command": "alignment" },
        // Column mode
        { "keys": ["ctrl+alt+up"], "command": "column_select", "args": {"by": "lines", "forward": false}},
        { "keys": ["ctrl+alt+down"], "command": "column_select", "args": {"by": "lines", "forward": true}},
        { "keys": ["ctrl+alt+pageup"], "command": "column_select", "args": {"by": "pages", "forward": false}},
        { "keys": ["ctrl+alt+pagedown"], "command": "column_select", "args": {"by": "pages", "forward": true}},
        { "keys": ["ctrl+alt+home"], "command": "column_select", "args": {"by": "all", "forward": false}},
        { "keys": ["ctrl+alt+end"], "command": "column_select", "args": {"by": "all", "forward": true}}
    ]

Theme and Color Scheme
~~~~~~~~~~~~~~~~~~~~~~~

I like using the material theme. In particular, I use the "Materialize" theme.
You can use this by installing following packages:

-  `Materialize <https://github.com/saadq/Materialize>`__
-  `Materialize-Appbar <https://github.com/saadq/Materialize-Appbar>`__
-  `Materialize-White-Panels <https://github.com/saadq/Materialize-White-Panels>`__

With these installation, you will also a lot of color schemes to use with this
theme. I prefer to use the *"Material Oceanic Next"* color scheme.
All other settings for this theme can be seen in my settings summary below.

User Settings / Preferences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is my complete user-defined settings for Sublime Text. Please feel free to
leave comments below for any questions or suggestions.

.. code:: json

    {
        "always_show_minimap_viewport": true,
        "auto_complete": true,
        "bold_folder_labels": true,
        "caret_extra_width": 1.5,
        "color_scheme": "Packages/User/SublimeLinter/Material Oceanic Next (SL).tmTheme",
        "default_line_ending": "unix",
        "drag_text": false,
        "draw_white_space": "all",
        "enable_tab_scrolling": false,
        "font_face": "DejaVu Sans Mono",
        "font_options":
        [
            "directwrite",
            "gray_antialias",
            "subpixel_antialias"
        ],
        "font_size": 13,
        "ignored_packages":
        [
            "C++",
            "Python",
            "Vintage"
        ],
        "indent_guide_options":
        [
            "draw_normal",
            "draw_active"
        ],
        "line_padding_bottom": 1,
        "line_padding_top": 1,
        "material_theme_bold_tab": true,
        "material_theme_compact_panel": true,
        "material_theme_compact_sidebar": false,
        "material_theme_contrast_mode": true,
        "material_theme_disable_fileicons": false,
        "material_theme_disable_folder_animation": true,
        "material_theme_disable_tree_indicator": true,
        "material_theme_panel_separator": true,
        "material_theme_small_statusbar": true,
        "material_theme_small_tab": true,
        "material_theme_tabs_autowidth": true,
        "material_theme_tabs_separator": true,
        "material_theme_tree_headings": true,
        "overlay_scroll_bars": "enabled",
        "rulers":
        [
            80
        ],
        "scroll_past_end": true,
        "soda_classic_tabs": true,
        "soda_folder_icons": true,
        "tab_completion": false,
        "tab_size": 4,
        "theme": "Material Oceanic Next.sublime-theme",
        "translate_tabs_to_spaces": true,
        "trim_trailing_white_space_on_save": true,
        "word_wrap": true
    }

