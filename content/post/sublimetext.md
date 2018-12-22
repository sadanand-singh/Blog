---
title: "Sublime Text Setup"
slug: "sublimetext"
date: 2018-11-10
tags:
    - "Editor"
categories:
    - "Computers"
link:
authors:
    - "Sadanand Singh"
description:
disqus_identifier: "sublimetext.sadanand"
---

**UPDATE: This post has been updated with my latest sublime settings.**

I have been using [Sublime text](https://www.sublimetext.com/) as my primary editor for some time
now. Here I wanted to share my current setup for the editor including all settings, packages,
shortcut keys and themes.

<!--more-->

{{< load-photoswipe >}}
{{< gallery >}}
{{< figure-thumb link="https://res.cloudinary.com/sadanandsingh/image/upload/v1544988652/images/sublime/Settings.png" caption="Settings" >}}
{{< figure-thumb link="https://res.cloudinary.com/sadanandsingh/image/upload/v1544988653/images/sublime/CommandPallette.png" caption="Command Pallette" >}}
{{< figure-thumb link="https://res.cloudinary.com/sadanandsingh/image/upload/v1544988652/images/sublime/PythonAnaconda.png" caption="Python Autocompletion" >}}
{{< figure-thumb link="https://res.cloudinary.com/sadanandsingh/image/upload/v1544988652/images/sublime/MarkdownEditing.png" caption="MarkDown" >}}
{{< figure-thumb link="https://res.cloudinary.com/sadanandsingh/image/upload/v1544988653/images/sublime/JsonEditing.png" caption="Json" >}}
{{< figure-thumb link="https://res.cloudinary.com/sadanandsingh/image/upload/v1544988653/images/sublime/ImageView.png" caption="View Images" >}}
{{< /gallery >}}

<!--toc-->


Packages
========

First thing you will need to install is the [Package
Control](https://packagecontrol.io). This can be easily done by
following the directions at their [installation instructions](https://packagecontrol.io/installation).

Once you have installed the package manager and restarted sublime text,
now you can install all other packages using the powerful command
pallet. Hit `ctrl + shift + P` and type *Install*, choose *Package
Control : Install Package*. Now you can search for any package that you
wish to install, and then press *Enter* to install it.

Here is a list of packages that I currently use:

-   [Alignment](https://github.com/wbond/sublime_alignment)
-   [Bracket Highlighter](https://github.com/facelessuser/BracketHighlighter)
-   [C++11](https://github.com/noct/sublime-cpp11)
-   [Column Select](https://github.com/ehuss/Sublime-Column-Select)
-   [DocBlockr Python](https://github.com/adambullmer/sublime_docblockr_python)
-   [GitGutter](https://github.com/jisaacks/GitGutter)
-   [Anaconda](https://damnwidget.github.io/anaconda/)
-   [MagicPython](https://github.com/MagicStack/MagicPython)
-   [rsub](https://github.com/henrikpersson/rsub)
-   [Sidebar Enhancements](https://github.com/SideBarEnhancements-org/SideBarEnhancements)
-   [A File Icon](https://github.com/ihodev/a-file-icon)
-   [sublack](https://github.com/jgirardet/sublack)
-   [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter3)
-   [SublimeLinter flake8](https://github.com/SublimeLinter/SublimeLinter-flake8)
-   [SublimeLinter addon black for flake](https://github.com/kaste/SublimeLinter-addon-black-for-flake)

**Alignment** provides a simple key-binding for aligning multi-line and multiple selections.

**Bracket Highlighter**, as the name suggests, matches a variety of brackets such
as: `[], (), {}, "", '', <tag></tag>`, and even custom brackets.

**C++11** provides better coloring scheme and syntax highlighting for C++11 and beyond syntax.

**Column Select** plug-in provides an alternate behavior for Sublime keyboard column selection.
The major differences are:

-   Allows reversing direction (go down too far, just go back up).
-   Added PageUp/PageDown, Home/End, and mouse selection.
-   Skip rows that are too short.
-   If you start at the end of a line, then it will stay at the end of
    each line.

**DocBlockr_Python** makes writing documentation a breeze for python
code. I typically use google docstring format, so I modify settings as follows:

```json
{
    /**
     * This option dictates which style of docstrings to use, when parsing docstrings
     *
     * Available Options:
     * [PEP0257, docblock, google, numpy, sphinx]
     */
    "formatter": "google"
}
```

**GitGutter** is a handy plug-in to show information about files
in a git repository. Main Features are:

-   Gutter Icons indicating inserted, modified or deleted lines
-   Diff Popup with details about modified lines
-   Status Bar Text with information about file and repository
-   Jumping Between Changes to easily navigate between modified lines


**Anaconda** is a plugin that turns your SublimeText 3 into a rich featured Python development
stack that boost your productivity and helps you to ensure the quality and style of your code.
The plugin works out of the box with no configuration but, I prefer to specify the python
interpreter explicitly. I also like to use SublimeLinter with flake for linting, hence I disable
linting via Anaconda.

```json
{
    /*
        Default python interpreter

        This can (and should) be overridden by project settings.

        NOTE: if you want anaconda to lint and complete using a remote
        python interpreter that runs the anaconda's minserver.py script
        in a remote machine just use it's address:port as interpreter
        for example:

            "python_interpreter": "tcp://my_remote.machine.com:19360"
    */
    "python_interpreter": "python",

    /*
        Set to false to disable Anaconda linting entirely.
    */
    "anaconda_linting": false,
}
```

**MagicPython** is a package with preferences and syntax highlighter for
cutting edge Python 3. It is meant to be a drop-in replacement for the
default Python package. MagicPython correctly highlights all Python 3.5
and 3.6 syntax features, including type annotations, f-strings and
regular expressions. It is built from scratch for robustness with an
extensive test suite.

**sublack** is plugin to run black. [Black] is the uncompromising Python code formatter. Blackened
code looks the same regardless of the project you're reading. Formatting becomes transparent after
a while and you can focus on the content instead. I prefer to use a line width of 99. By default
black likes to convert all strings to double quotes, while I prefer single quotes. Following
configuration is needed for these modifications:


[Black]: https://github.com/ambv/black

```json
{
      // ########################
      // Black specific options #
      // ########################

      // line length
      // uses black default, if not modified
      "black_line_length": 99,

      // prevent black from changing single quote to double quotes
      // default is false
      // add --black_skip_string_normalization
      "black_skip_string_normalization": true,

      // Don't normalize underscores in numeric literals.
      "black_skip_numeric_underscore_normalization": false,

      // force py36 syntax mode
      "black_py36": true,

      // ##########################
      // Sublack specific options #
      // ##########################

      // run black before saving document
      "black_on_save": true
}
```

**rsub** is an implementation of TextMate 2's [rmate] feature for
Sublime Text, allowing files to be edited on a remote server using ssh
port forwarding / tunneling. Please make sure you have installed a
version of [rmate] and are using
correct [port forwarding](https://atom.io/packages/remote-atom).

[rmate]: https://github.com/aurora/rmate

**SidebarEnhancements** Provides enhancements to the operations on Sidebar of Files and Folders for
Sublime Text. The main features are:

- Provides delete as "move to trash", open with.. and a clipboard.
- Close, move, open and restore buffers affected by a rename/move command (even on folders).
- Provides new file/folder, edit, open/run, reveal, find in selected/parent/project, cut, copy,
paste, paste in parent, rename, move, delete, refresh etc.
- Provides copy paths as URIs, URLs, content as UTF8, content as data:uri base64 ( nice for
embedding into CSS! ), copy as tags img/a/script/style, duplicate etc.
- Allows to display "file modified date" and "file size" on status bar.

**A File Icon** is a further enhancement to SidebarEnhancements plugin to provide fancy icons for
different types of files and folders.

**SublimeLinter** and **SublimeLinter-flake8** is plug-in that provides
an interface to [flake8](https://flake8.pycqa.org/en/latest/). It will be
used with files that have the `Python` syntax. **SublimeLinter addon black for flake** is tiny
add-on package to make sublack fully compatible with flake linter.

```json
// SublimeLinter Settings - User
{
    "linters": {
        "flake8": {
            "args": [
                "--max-line-length=99",
                "--exclude=.git,__pycache__,.direnv,node_modules"
            ]
        }
    }
}
```

Shortcut Keys
=============

Here is a summary of my key map:

```json
[
    { "keys": ["shift+alt+a"], "command": "find_all_under" },
    { "keys": ["control+v"], "command": "paste_and_indent" },
    { "keys": ["control+shift+v"], "command": "paste" },
    { "keys": ["ctrl+alt+;"], "command": "alignment" },
    { "keys": ["alt+shift+up"], "command": "column_select", "args": {"by": "lines", "forward": false}},
    { "keys": ["alt+shift+down"], "command": "column_select", "args": {"by": "lines", "forward": true}},
    { "keys": ["alt+shift+pageup"], "command": "column_select", "args": {"by": "pages", "forward": false}},
    { "keys": ["alt+shift+pagedown"], "command": "column_select", "args": {"by": "pages", "forward": true}},
    { "keys": ["alt+shift+home"], "command": "column_select", "args": {"by": "all", "forward": false}},
    { "keys": ["alt+shift+end"], "command": "column_select", "args": {"by": "all", "forward": true}}
]
```

Theme and Color Scheme
======================

I like a simple and clean UI for my editors. [AYU] provides the perfect minimal theme and
color scheme for my purpose. Please see above screen shots to see if this attracts you!
The settings related to this can be found in my settings below.

[AYU]: https://github.com/dempfi/ayu

User Settings / Preferences
===========================

Here is my complete set of settings for Sublime Text. Please feel free
to leave comments below for any questions or suggestions.

```json
{
    "always_show_minimap_viewport": true,
    "auto_complete": true,
    "bold_folder_labels": true,
    "caret_extra_width": 1.5,
    "color_scheme": "Packages/ayu/ayu-mirage.tmTheme",
    "default_line_ending": "unix",
    "drag_text": false,
    "draw_white_space": "all",
    "enable_tab_scrolling": false,
    "font_face": "Roboto mono",
    "font_options":
    [
        "directwrite",
        "gray_antialias",
        "subpixel_antialias"
    ],
    "font_size": 15,
    "hot_exit": false,
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
    "overlay_scroll_bars": "enabled",
    "remember_open_files": false,
    "rulers":
    [
        100
    ],
    "scroll_past_end": true,
    "soda_classic_tabs": true,
    "soda_folder_icons": true,
    "tab_completion": false,
    "tab_size": 4,
    "theme": "ayu-mirage.sublime-theme",
    "translate_tabs_to_spaces": true,
    "trim_trailing_white_space_on_save": true,
    "ui_big_tabs": true,
    "ui_fix_tab_labels": true,
    "ui_font_default": true,
    "ui_font_size_small": true,
    "ui_font_source_code_pro": true,
    "ui_separator": true,
    "ui_wide_scrollbars": true,
    "word_wrap": true
}
```
