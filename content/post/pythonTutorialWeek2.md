---
title: "Python Tutorial - Week 2"
slug: "pythontutorialweek2"
date: 2016-10-03
tags:
    - "Programming"
    - "Python"
categories:
    - "Tutorials"
link:
readingTime: 16
hasMath: true
notebook: true
disqus_identifier: "pythontutorialweek2.sadanand"
description:
---


In the [Week 1]({{< relref "pythonTutorialWeek1.md" >}}) we got started with Python. Now that we can interact with python, lets dig deeper into it.

This week we will go over some additional fundamental things common in any program - interactive input from users, adding comments to your code, use of conditional logic i.e. `if - else` conditions, loops, formatted output with strings and `print()` statements.

<!--more-->

### Python Week 2

#### User Inputs

There are hardly any programs without any input. Input can come in various ways, for example from a database, another computer, mouse clicks and movements or from the internet. Yet, in most cases the input stems from the keyboard. For this purpose, Python provides the function input(). `input()` has an optional parameter, which is the prompt string, i.e. the text that will be shown when asking for input.


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">name</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;What&#39;s your name? &quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Nice to meet you &quot;</span> <span class="o">+</span> <span class="n">name</span> <span class="o">+</span> <span class="s2">&quot;!&quot;</span><span class="p">)</span>
<span class="n">age</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Your age? &quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;So, you are already &quot;</span> <span class="o">+</span> <span class="n">age</span> <span class="o">+</span> <span class="s2">&quot; years old, &quot;</span> <span class="o">+</span> <span class="n">name</span> <span class="o">+</span> <span class="s2">&quot;!&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>What&#39;s your name? Sadanand
Nice to meet you Sadanand!
Your age? 30
So, you are already 30 years old, Sadanand!
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>What if you try to do some mathematical operation on the age? You will get a TypeError as follows:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">age</span> <span class="o">=</span> <span class="mi">12</span> <span class="o">+</span> <span class="n">age</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-fg">---------------------------------------------------------------------------</span>
<span class="ansi-red-fg">TypeError</span>                                 Traceback (most recent call last)
<span class="ansi-green-fg">&lt;ipython-input-2-3d9ce720d6f3&gt;</span> in <span class="ansi-cyan-fg">&lt;module&gt;</span><span class="ansi-blue-fg">()</span>
<span class="ansi-green-fg">----&gt; 1</span><span class="ansi-red-fg"> </span>age <span class="ansi-blue-fg">=</span> <span class="ansi-cyan-fg">12</span> <span class="ansi-blue-fg">+</span> age

<span class="ansi-red-fg">TypeError</span>: unsupported operand type(s) for +: &#39;int&#39; and &#39;str&#39;</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This says that by default all data is read as raw input i.e. strings. If we want numbers we need to convert them ourselves. For example:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="n">cities_canada</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Largest cities in Canada: &quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Largest cities in Canada: [&#34;Montreal&#34;, &#34;Ottawa&#34;, &#34;Calgary&#34;, &#34;Toronto&#34;]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[4]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="nb">print</span><span class="p">(</span><span class="n">cities_canada</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">cities_canada</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#34;Montreal&#34;, &#34;Ottawa&#34;, &#34;Calgary&#34;, &#34;Toronto&#34;] &lt;class &#39;str&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">cities_canada</span> <span class="o">=</span> <span class="nb">eval</span><span class="p">(</span><span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Largest cities in Canada: &quot;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Largest cities in Canada: [&#34;Montreal&#34;, &#34;Ottawa&#34;, &#34;Calgary&#34;, &#34;Toronto&#34;]
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="nb">print</span><span class="p">(</span><span class="n">cities_canada</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">cities_canada</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>[&#39;Montreal&#39;, &#39;Ottawa&#39;, &#39;Calgary&#39;, &#39;Toronto&#39;] &lt;class &#39;list&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[7]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">population</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Population of Portland? &quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Population of Portland? 604596
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[8]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="nb">print</span><span class="p">(</span><span class="n">population</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">population</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>604596 &lt;class &#39;str&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[9]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">population</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Population of Portland? &quot;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Population of Portland? 604596
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[10]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="nb">print</span><span class="p">(</span><span class="n">population</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">population</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>604596 &lt;class &#39;int&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[13]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pi</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Value of PI is?&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Value of PI is?3.14
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="nb">print</span><span class="p">(</span><span class="n">pi</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">pi</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>3.14 &lt;class &#39;str&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">pi</span> <span class="o">=</span> <span class="nb">float</span><span class="p">(</span><span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Value of PI is?&quot;</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Value of PI is?3.14
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> <span class="nb">print</span><span class="p">(</span><span class="n">pi</span><span class="p">,</span> <span class="nb">type</span><span class="p">(</span><span class="n">pi</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>3.14 &lt;class &#39;float&#39;&gt;
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Notice the use of various methods like eval(), int() and float() to get user input in correct formats. In summary, eval() is used to get data into various native python formats, e.g. lists, dictionaries etc. <em>We will look at these in more detail in next few tutorials</em>. int() is used to convert input to integer numbers (numbers without decimals), while float() is used to get floating point numbers.</p>
<p>Also, of interest above is the type() method used in print statements. You can get the type of any variable in python using this method. In the output of this we see something like: &lt; class 'float'&gt; - if variable is of float type. For the time being we will ignore the "class" in this.</p>
<h4 id="Indentation-Blocks">Indentation Blocks<a class="anchor-link" href="#Indentation-Blocks">&#182;</a></h4><p>Python programs get structured through indentation, i.e. code blocks are defined by their indentation (The amount of blank space before any line). This principle makes it easier to read and understand other people's Python code.</p>
<p>All statements with the same distance to the right belong to the same block of code, i.e. the statements within a block line up vertically. The block ends at a line less indented or the end of the file. If a block has to be more deeply nested, it is simply indented further to the right.</p>
<p>In the following sections below we will see extensive use of such indentation blocks. Consider the following example to calculate Pythagorean triples. You do not need to understand the full code right here. We will revisit this code at the end of this tutorial.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">math</span> <span class="k">import</span> <span class="n">sqrt</span>
<span class="n">n</span> <span class="o">=</span> <span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Maximum Number? &quot;</span><span class="p">)</span>
<span class="n">n</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">n</span><span class="p">)</span><span class="o">+</span><span class="mi">1</span>
<span class="k">for</span> <span class="n">a</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="n">n</span><span class="p">):</span>
    <span class="k">for</span> <span class="n">b</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">a</span><span class="p">,</span><span class="n">n</span><span class="p">):</span>
        <span class="n">c_square</span> <span class="o">=</span> <span class="n">a</span><span class="o">**</span><span class="mi">2</span> <span class="o">+</span> <span class="n">b</span><span class="o">**</span><span class="mi">2</span>
        <span class="n">c</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">sqrt</span><span class="p">(</span><span class="n">c_square</span><span class="p">))</span>
        <span class="k">if</span> <span class="p">((</span><span class="n">c_square</span> <span class="o">-</span> <span class="n">c</span><span class="o">**</span><span class="mi">2</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">):</span>
            <span class="nb">print</span><span class="p">(</span><span class="n">a</span><span class="p">,</span> <span class="n">b</span><span class="p">,</span> <span class="n">c</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Maximum Number? 10
3 4 5
6 8 10
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In the above code, we see three indentation blocks, first and second "for" loops and the third "if" condition. There is another aspect of structuring in Python, which we haven't mentioned so far, which you can see in the example. Loops and Conditional statements end with a colon ":" - the same is true for functions and other structures introducing blocks. So, we should have said Python structures by colons and indentation.</p>
<h4 id="Comments-in-Python">Comments in Python<a class="anchor-link" href="#Comments-in-Python">&#182;</a></h4><p>Python has two ways to annotate/comment Python code. One is by using comments to indicate what some part of the code does. Single-line comments begin with the hash character ("#") and are terminated by the end of line. Here is an example:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># This is a comment in Python before print statement</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Hello World&quot;</span><span class="p">)</span> <span class="c1">#This is also a comment in Python</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Hello World
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Conditionals">Conditionals<a class="anchor-link" href="#Conditionals">&#182;</a></h4><p>Conditionals, - mostly in the form of if statements - are one of the essential features of a programming language. A decision has to be taken when the script or program comes to a point where it has a choice of actions, i.e. different computations, to choose from.</p>
<p>The decision depends in most cases on the value of variables or arithmetic expressions. These expressions are evaluated to the Boolean values <em>True</em> or <em>False</em>. The statements for the decision taking are called <em>conditional statements</em>. Alternatively they are also known as <em>conditional expressions</em> or <em>conditional constructs</em>.</p>
<p>Conditional statements in Python use indentation blocks to <em>conditionally</em> execute certain code. The general form of the if statement in Python looks like this:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">if</span> <span class="n">condition_1</span><span class="p">:</span>
    <span class="n">statement_block_1</span>
<span class="k">elif</span> <span class="n">condition_2</span><span class="p">:</span>
    <span class="n">statement_block_2</span>

<span class="o">...</span>

<span class="k">elif</span> <span class="n">another_condition</span><span class="p">:</span>    
    <span class="n">another_statement_block</span>
<span class="k">else</span><span class="p">:</span>
    <span class="n">else_block</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre></pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>If the condition "condition_1" is True, the statements of the block statement_block_1 will be executed. If not, condition_2 will be evaluated. If condition_2 evaluates to True, statement_block_2 will be executed, if condition_2 is False, the other conditions of the following elif conditions will be checked, and finally if none of them has been evaluated to True, the indented block below the else keyword will be executed.</p>
<p>Typical examples of "condition" statements follow some of following operations:
mathematical comparisons like, "&lt;", "&gt;", "&lt;=", "&gt;=", "=="
object comparisons like "is" i.e. this is exactly something or not.
boolean logic operators like "not", "or", "and", "xor" etc.</p>
<p>The following objects are evaluated by Python as <em><strong>False</strong></em>:</p>
<ul>
<li>numerical zero values (0, 0L, 0.0, 0.0+0.0j),</li>
<li>the Boolean value False,</li>
<li>empty strings,</li>
<li>empty lists and empty tuples,</li>
<li>empty dictionaries.</li>
<li>the special value None.</li>
</ul>
<p>All other values are considered to be <em><strong>True</strong></em>.</p>
<p>Let us try to solve this simple DNA sequence problem:
<strong>Given the an input DNA sequence, print the sequence if its length is less than equal to 20. Print "Error" if the sequence is empty or its length is larger than 25. If length is between 21 and 25, print the last 5 bases only.</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCCGATTTATCGGGAACCNNNAATTCCGG&quot;</span>

<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">25</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">[</span><span class="o">-</span><span class="mi">5</span><span class="p">:])</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>ERROR!
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCAATGCN&quot;</span>

<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">25</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">[</span><span class="o">-</span><span class="mi">5</span><span class="p">:])</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>ATGCAATGCN
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span>

<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">25</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">[</span><span class="o">-</span><span class="mi">5</span><span class="p">:])</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>ERROR!
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCCGATTTATCGGGAACCNNN&quot;</span>

<span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span><span class="p">:</span>
    <span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
<span class="k">elif</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">25</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">[</span><span class="o">-</span><span class="mi">5</span><span class="p">:])</span>
<span class="k">else</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;ERROR!&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>CCNNN
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><em>if else</em> conditions can also be combined in a regular assignment expression to assign values. For example,
In the DNA case, we want to store length of DNA. However, we want length to number only if length of sequence is between 1 and 25. In all other cases, we want to store the length of sequence as -1. A typical way to do this would be:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCCGATTTATCGGGAACCNNN&quot;</span>
<span class="n">length</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
<span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span><span class="p">:</span>
    <span class="n">length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span>
    
<span class="nb">print</span><span class="p">(</span><span class="n">length</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>-1
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;CCGGGAACCTCACG&quot;</span>
<span class="n">length</span> <span class="o">=</span> <span class="o">-</span><span class="mi">1</span>
<span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span><span class="p">:</span>
    <span class="n">length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span>
    
<span class="nb">print</span><span class="p">(</span><span class="n">length</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>14
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>This example can be written in a much shorter fashion as well. Such conditions are commonly called as <em>ternary if</em> statements.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCCGATTTATCGGGAACCNNN&quot;</span>
<span class="n">length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span> <span class="k">else</span> <span class="o">-</span><span class="mi">1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">length</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>-1
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;CCGGGAACCTCACG&quot;</span>
<span class="n">length</span> <span class="o">=</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="k">if</span> <span class="mi">0</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="mi">20</span> <span class="k">else</span> <span class="o">-</span><span class="mi">1</span>
<span class="nb">print</span><span class="p">(</span><span class="n">length</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>14
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Loops">Loops<a class="anchor-link" href="#Loops">&#182;</a></h4><p>Many algorithms make it necessary for a programming language to have a construct which makes it possible to carry out a sequence of statements repeatedly. The code within the loop, i.e. the code carried out repeatedly, is called the body of the loop.</p>
<p>There are two types of loops in Python -</p>
<ol>
<li><em>while</em> Loop</li>
<li><em>for</em> Loop</li>
</ol>
<p><strong>The <em>while</em> Loop</strong></p>
<p>These are a type of loop called "Condition-controlled loop". As suggested by the name, the loop will be repeated until a given condition changes, i.e. changes from True to False or from False to True, depending on the kind of loop.</p>
<p>Let us consider the following example of DNA sequence:
<strong>We want to print every base of a given sequence, until we have found 2 <code>A</code>s.</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCCGATTTATCGGGAACCNNN&quot;</span>
<span class="n">countA</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">while</span> <span class="n">countA</span> <span class="o">&lt;</span> <span class="mi">2</span><span class="p">:</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
    <span class="k">if</span> <span class="n">dna</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;A&#39;</span><span class="p">:</span>
        <span class="n">countA</span> <span class="o">=</span> <span class="n">countA</span> <span class="o">+</span> <span class="mi">1</span>
    <span class="n">index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>A
T
G
C
C
G
A
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>In the above example, the loop (code under the <em>while</em> block) was executed until <em>countA &lt; 2</em> statement remained true.</p>
<p>The loops can be made to exit before its actual completion using the <strong><em>break</em></strong> statements.
Consider the following example of DNA sequence.
<strong>We want to print every base of a given sequence, until we have found 2 As. However, we want to stop printing as soon as we have found an 'N' base.</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[29]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCNCGATTTATCGGGAACCNNN&quot;</span>
<span class="n">countA</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">while</span> <span class="n">countA</span> <span class="o">&lt;</span> <span class="mi">2</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">dna</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;N&#39;</span><span class="p">:</span>
        <span class="k">break</span>
    <span class="k">if</span> <span class="n">dna</span><span class="p">[</span><span class="n">index</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;A&#39;</span><span class="p">:</span>
        <span class="n">countA</span> <span class="o">=</span> <span class="n">countA</span> <span class="o">+</span> <span class="mi">1</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">[</span><span class="n">index</span><span class="p">])</span>
    <span class="n">index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>A
T
G
C
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Now, let us consider another case while looping over something. We want to skip over a part of code at certain condition. In such cases, <em>continue</em> statement comes handy.</p>
<p>Consider the following example wrt to DNA sequencing.
<strong>Given a sequence of dna, we do NOT want to print the base name if it is 'N'</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[30]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCNCN&quot;</span>
<span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">while</span> <span class="n">index</span> <span class="o">&lt;</span> <span class="nb">len</span><span class="p">(</span><span class="n">dna</span><span class="p">):</span>
    <span class="n">index</span> <span class="o">=</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span>
    <span class="k">if</span> <span class="n">dna</span><span class="p">[</span><span class="n">index</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s1">&#39;N&#39;</span><span class="p">:</span>
        <span class="k">continue</span>
    <span class="nb">print</span><span class="p">(</span><span class="n">dna</span><span class="p">[</span><span class="n">index</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>A
T
G
C
C
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p><strong>The <em>for</em> Loop</strong></p>
<p>A <em>for</em> loop is similar to while loop, except it is used to loop over certain elements, unlike while loop that continues until certain condition is satisfied. In the case DNA sequences, say, one case of <em>for</em> loop would be to loop over all bases in a sequence.</p>
<p>Consider the following example:
<strong>Given a DNA sequence, we want to count the number of all 'A', and 'T bases.</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGCNCGATTTATCGGGAACCNNN&quot;</span>
<span class="n">count</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="n">dna</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">base</span> <span class="o">==</span> <span class="s1">&#39;A&#39;</span> <span class="ow">or</span> <span class="n">base</span> <span class="o">==</span> <span class="s1">&#39;T&#39;</span><span class="p">:</span>
        <span class="n">count</span> <span class="o">+=</span> <span class="mi">1</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number of A, T bases is:&quot;</span><span class="p">,</span> <span class="n">count</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Number of A, T bases is: 10
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Similar to <em>while</em> loops, we can use <em>break</em> and <em>continue</em> statements with <em>for</em> loops as well.</p>
<p>Let us look at somewhat complicated use of <em>for</em> loop:</p>
<p><strong>Given a DNA sequence, we want to count the number of doublets of bases, i.e. no. of times certain bases come twice exactly. If some base occur more than twice, we do not want to count that.</strong></p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[32]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dna</span> <span class="o">=</span> <span class="s2">&quot;ATGGCNCGAATTTAAATCGGGAACCNNN&quot;</span>
<span class="n">countPairs</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">pairFound</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">prevBase</span> <span class="o">=</span> <span class="s1">&#39;&#39;</span>
<span class="k">for</span> <span class="n">base</span> <span class="ow">in</span> <span class="n">dna</span><span class="p">:</span>
    <span class="k">if</span> <span class="p">(</span><span class="n">base</span> <span class="o">==</span> <span class="n">prevBase</span><span class="p">):</span>
        <span class="n">pairFound</span> <span class="o">+=</span> <span class="mi">1</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">pairFound</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">countPairs</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">pairFound</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">prevBase</span> <span class="o">=</span> <span class="n">base</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number of paired bases is:&quot;</span><span class="p">,</span> <span class="n">countPairs</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Number of paired bases is: 4
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h4 id="Formatting-of-Output">Formatting of Output<a class="anchor-link" href="#Formatting-of-Output">&#182;</a></h4><p>Final topic for this week is the formatting of text in the print statements. Consider the following case:</p>
<p>We have following variables:
<em>name = "Sadanand"</em>, <em>age = 30</em>, and <em>gender = "male"</em>.</p>
<p>We would like to print a quite cumbersome statement like as follows. This can be quite easily done using the <em>format</em> method.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[33]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;Sadanand&quot;</span>
<span class="n">age</span> <span class="o">=</span> <span class="mi">30</span>
<span class="n">gender</span> <span class="o">=</span> <span class="s2">&quot;male&quot;</span>
<span class="n">msg</span> <span class="o">=</span> <span class="s2">&quot;Hi </span><span class="si">{0}</span><span class="s2">, You are a </span><span class="si">{1}</span><span class="s2">, and you have seen </span><span class="si">{2}</span><span class="s2"> winters as you are </span><span class="si">{2}</span><span class="s2"> years old! Thanks </span><span class="si">{0}</span><span class="s2">!&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="n">msg</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">name</span><span class="p">,</span> <span class="n">gender</span><span class="p">,</span> <span class="n">age</span><span class="p">))</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>Hi Sadanand, You are a male, and you have seen 30 winters as you are 30 years old! Thanks Sadanand!
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Thus <em>format</em> method provides us with easy way to mix different types of variables in the strings.</p>
<p>Thats it for this week. Next we will look at strings and lists in Python in more detail.</p>
<p><strong>Exercise</strong></p>
<p>Given the following sequence of dna - "ATGGCNCGAATTTAAATCGGGAACCNNN",</p>
<ol>
<li><p>Write a program to count number of all triplets in it.</p>
</li>
<li><p>Write a program that prints all non 'T' bases that come after 'T', but stops when two or more continuous 'T' has been found.</p>
</li>
<li><p>Write a program to generate new sequence with every 3rd base from the above sequence.</p>
</li>
<li><p>Write a program to calculate sum of all numbers from 1 to 10. HINT: Please take a look at the <a href="https://docs.python.org/3/library/stdtypes.html#range">range</a> method.</p>
</li>
</ol>

</div>
</div>
</div>
