---
title: "Shortest Non-repeating Substring"
slug: "shortestSubstring"
date: 2015-01-27
tags:
    - "Algorithms"
    - "Python"
categories:
    - "Algorithms"
link:
hasMath: true
readingTime: 8
disqus_identifier: "shortestSubstring.sadanand"
description:
---

Given an alphanumeric string, find the shortest substring that occurs
exactly once as a (contiguous) substring in it. Overlapping occurrences
are counted as distinct. If there are several candidates of the same
length, you must output all of them in the order of occurrence. The
*space* is NOT considered as a valid non-repeating substring.

<!--more-->

{{% panel primary "**Example**" %}}

Consider the following cases:

__Case 1:__ If the given string is `asdfsasa`, the answer should be
`['d', 'f']`

__Case 2:__ If the given string is `sadanands`,

the answer should be `['sa', 'ad', 'da', 'na', 'nd', 'ds']`

__Case 3:__ If the given string is `wwwwwwww`, the answer should be
`['wwwwwwww']`

{{% /panel %}}

My Solution
===========

Here is my solution in *Python*.

It is quite brute force. I am not sure about the order of `find()` and
`rfind()` built-in methods in _Python_. Assuming these are $O(n)$, my
algorithm is in $O(n^3)$. Please put your answers in comments below,
if your answer has a better scaling.

The function definition that I use for finding non-empty non-repeating
strings is _recursive_.

{{< code-block code="python" lines="1" hl="4-6" >}}
def findNsubString(s,n):
    subS = []
    for index in range(len(s)+1) :
        x = s[index:index+n]
        if s.find(x)==s.rfind(x) :
            subS.append(x)
    if subS :
        return subS
    else :
        return findNsubString(s,n+1)
{{< /code-block >}}

I call this method as follows to get the desired results:

{{< code-block code="python" lines="1" >}}
#! /usr/bin/python
import argparse
# Parse Command Line Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-s", "--string", default = "asda", help="Input")
args = parser.parse_args()
s = args.string
# Call Method to find smallest non-repeating sub-string
ans = findNsubString(s,1)
print(ans)
{{< /code-block >}}

A similar solution can also be written in `JAVA` or `C++`. The corresponding
`find()` and `rfind()` methods in JAVA are called `indexOf()` and
`lastIndexOf()`, respectively. In C++, these methods are called same as
in Python.

Please feel free to put your method definition in any programming
language.
