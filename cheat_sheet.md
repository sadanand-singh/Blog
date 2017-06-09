# Images

![Image](https://res.cloudinary.com/sadanandsingh/image/upload/v1496963333/sadanand_navmqu.jpg){: style="width: 280pt;" .img-responsive .align-center}

# Alerts (warning, danger, info or success )

{{% alert info %}}

In the original post this problem was ill defined.

Please solve this problem with the constraints that only up and right
moves are allowed.

{{% /alert %}}

# Admonitions (attention, caution, danger, error, hint, important, note, tip, warning)

!!! important ""
    This is a admonition box without a title.

!!! danger "Don't try this at home"
    ...

# Highligh Text (error, warning, red, yellow, green, cyan, blue, purple)

{{% hl-text warning %}}
Copy our current wifi setup file into the new system. This will enable
wifi at first boot. Next, chroot into our newly installed system:
{{% /hl-text %}}

# Code With highligh text

```python hl_lines="4 5"
# This line is emphasized
# This line is emphasized

def new_func():
   return None
```

# Table of contents

**Table of Contents**

[TOC]

# Maths

Write your $p^2-1 = (p-1)\times (p+1)$ post here.

$$p-1=2K, \text{and } p+1=2K+2=2(K+1)$$

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


|First Header  | Second Header|
|------------- | -------------|
|Content Cell  | Content Cell |
|Content Cell  | Content Cell |

Add this class

.mbtablestyle {
        border-collapse: collapse;

   > table, td, th {
        border: 1px solid black;
        }
}

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

