# Headers

# H1
## H2
### H3
#### H4
##### H5
###### H6

Alternatively, for H1 and H2, an underline-ish style:

Alt-H1
======

Alt-H2
------


# Different Emphasis

Emphasis, aka italics, with *asterisks* or _underscores_.

Strong emphasis, aka bold, with **asterisks** or __underscores__.

Combined emphasis with **asterisks and _underscores_**.

Strike through uses two tildes. ~~Scratch this.~~


# Links

[I'm an inline-style link](https://www.google.com)

[I'm an inline-style link with title](https://www.google.com "Google's Homepage")

[I'm a reference-style link][Arbitrary case-insensitive reference text]

[I'm a relative reference to a repository file](../blob/master/LICENSE)

[You can use numbers for reference-style link definitions][1]

Or leave it empty and use the [link text itself].

URLs and URLs in angle brackets will automatically get turned into links.
http://www.example.com or <http://www.example.com> and sometimes
example.com (but not on Github, for example).

Some text to show that the reference links can follow later.

[arbitrary case-insensitive reference text]: https://www.mozilla.org
[1]: http://slashdot.org
[link text itself]: http://www.reddit.com

# Images

Here's our logo (hover to see the title text):

Inline-style:
![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

Reference-style:
![alt text][logo]

[logo]: https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 2"

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")
{: .align-right style="width: 280pt;" }


{{% figure https://res.cloudinary.com/sadanandsingh/image/upload/v1496963550/st3_wdpsqu.png alt="Sublime Text" width=300 height=300 align=center scale=50% css=img-circle %}}

# Horizontal Rule

There or more...

---

Hyphens

***

Asterisks, or

___

Underscores

# Alerts (warning, danger, info or success )

**In the original post this problem was ill defined.
Please solve this problem with the constraints that only up and right
moves are allowed.**
{: class="alert alert-dismissible" .alert-danger}

# Admonitions (attention, caution, danger, error, hint, important, note, tip, warning)

!!! important ""
    This is a admonition box without a title.

!!! danger "Don't try this at home"
    ...

# Highligh Text / Marker  (error, warning, red, yellow, green, cyan, blue, purple)

Copy our current _wifi_ setup file into the new system. This will enable
wifi at first boot. Next, _chroot_ into our newly installed system:
{: .highlight-short-warning}

{{% marker cyan %}}
Copy our current _wifi_ setup file into the new system. This will enable
wifi at first boot. Next, _chroot_ into our `newly` installed system:
{{% /marker %}}

# Emphasis text (muted, primary, warning, danger, success or info)

Please see this text is colored correctly or not.
{: .text-success}

# Code With highlighted text

## Code blocks

{{% code-block code=json lines=1 start=5 hl=10-15 %}}
[
    { "keys": ["shift+alt+a"], "command": "find_all_under" },
    { "keys": ["control+v"], "command": "paste_and_indent" },
    { "keys": ["control+shift+v"], "command": "paste" },
    { "keys": ["ctrl+alt+;"], "command": "alignment" },
    { "keys": ["ctrl+alt+up"], "command": "column_select", "args": {"by": "lines", "forward": false}},
    { "keys": ["ctrl+alt+down"], "command": "column_select", "args": {"by": "lines", "forward": true}},
    { "keys": ["ctrl+alt+pageup"], "command": "column_select", "args": {"by": "pages", "forward": false}},
    { "keys": ["ctrl+alt+pagedown"], "command": "column_select", "args": {"by": "pages", "forward": true}},
    { "keys": ["ctrl+alt+home"], "command": "column_select", "args": {"by": "all", "forward": false}},
    { "keys": ["ctrl+alt+end"], "command": "column_select", "args": {"by": "all", "forward": true}}
]
{{% /code-block %}}

## In-line Code

{{% code Python %}}

# Table of content

**Table of Content**

[TOC]

# Math

Write your $p^2-1 = (p-1)\times (p+1)$ post here.

$$p-1=2K, \text{and } p+1=2K+2=2(K+1)$$

## multi-line math

{{% math %}}
F_{n} = \begin{cases} F_{n-2} + F_{n-1} & \text{if } n > 1 \\
 1 & \text{if } n = 1 \\
 0 & \text{if } n = 0
\end{cases}
{{% /math %}}


# Abbreviations

The HTML specification
is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium

# Definition Lists

Apple
:   Pomaceous fruit of plants of the genus Malus in
    the family Rosaceae.

Orange
:   The fruit of an evergreen tree of the genus Citrus.

# Footnotes

Footnotes[^1] have a label[^@#$%] and the footnote's content.

[^1]: This is a footnote content.
[^@#$%]: A footnote on the label: "@#$%".


# Tables

Colons can be used to align columns.

| Tables        | Are           | Cool  |
| ------------- |:-------------:| -----:|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

There must be at least 3 dashes separating each header cell.
The outer pipes (|) are optional, and you don't need to make the
raw Markdown line up prettily. You can also use inline Markdown.

Markdown | Less | Pretty
--- | --- | ---
*Still* | `renders` | **nicely**
1 | 2 | 3

# Sane Lists

Sane Lists do not allow the mixing of list types. In other words, an ordered list will not continue when an unordered list item is encountered and vice versa. For example:

1. Ordered item 1
2. Ordered item 2

* Unordered item 1
* Unordered item 2

Note that, unlike the default Markdown behavior, if a blank line is not included between list items, the different list type is ignored completely. This corresponds to the behavior of paragraphs. For example:

A Paragraph.
* Not a list item.

1. Ordered list item.
* Not a separate list item.
