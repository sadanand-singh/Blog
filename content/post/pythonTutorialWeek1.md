---
title: "Python Tutorial - Week 1"
slug: "PythonTutWeek1"
date: 2015-08-30
tags:
    - "Programming"
    - "Python"
categories:
    - "Tutorials"
link:
authors:
    - "Sadanand Singh"
hasMath: true
notebook: true
disqus_identifier: "PythonTutWeek1.sadanand"
description:
---

[Python](https://docs.python.org/3/library/index.html) is a widely used general-purpose, high-level programming language. Due to its focus on readability, wide-spread popularity and existence of a plethora of libraries (also called modules), it is one of the most preferred programming languages for scientists and engineers.

<!--more-->


Python for Non-Programmers
=============================

In this series of python tutorials, I will provide a set of lectures on various basic topics of python. The prime target audience for this series are scientist in non-programming fields like microbiology, genetics, psychology etc. who have some to none programming experience.


Here is a brief list of topics I will cover per week. I will also post exercises at the end of each session, along with the expected outputs. You should plan to complete these exercises within 5-6 days, before the new tutorial is posted. You will be judging your exercises on your own. The goal should be to match your program's output to the expected output.

-  **Week 1 :** Working with Python on Windows, Concept of Variables &amp; Math Operations, Displaying Outputs
-  **Week 2 :** User Inputs, Modules, Comments and Basics of Strings
-  **Week 3 :** More on Strings, Lists and Other Containers
-  **Week 4 :** Looping/iterating, if/else Conditions
-  **Week 5 :** Advanced String Operations
-  **Week 6 :** Regular Expressions and Strings
-  **Week 7 :** Reading and Writing Files
-  **Week 8 :** Functions and Writing Scripts
-  **Week 9 :** Interacting with Operating System
-  **Week 10 :** Handling and Plotting Data in Python
-  **Week 11 :** Basic Statistics in Python using Pandas
-  **Week 12 :** Introduction to BioPython



Week 1. Introduction to Python
--------------------------------

To start working with any programming language, first thing you need is a working installation of that language. Today, we will go through installation of python on Windows machines.

To keep things simple, We will be running our simple programs in google chrome browser, without any need of an installation.

For later exercises, from Week 7 onwards, I would highly recommend getting access to a Linux/Mac machine. However, I will also provide doing the same things on Windows machines and Google Chrome as well.

In this week's session, I will be assuming you will be using online python in google chrome.

To follow these tutorials, please run any code and observe output that you see in code blocks.

### Installing Python

Go to the following website to get access to [python](https://repl.it/languages/python3).

You should get a window like this:

{{< figure src="https://res.cloudinary.com/sadanandsingh/image/upload/v1545502114/project/python-online-editor.jpg" alt="Python Online" class="figure img-responsive align-center" >}}

You can work with this system in two ways:
A. Write your code interactively (one command at a time) on the dark screen on the left. Pressing `ENTER` will show you the output of that particular command.

Lets' try our first program:


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[1]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;My Name is so-and-so&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>My Name is so-and-so
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
<p>The above program will simply output whatever was put under "quotes". We will learn more about the print() method (what is a method/function in python?) towards the end of this session.</p>
<h3 id="Variables">Variables<a class="anchor-link" href="#Variables">&#182;</a></h3><p>A variable is a symbol or name that stands for a value. For example, in the expression
x = 23</p>
<p>x is a name/symbol whose value is numerical and equal to 23. if we write something like this:
y = x+12-5, then y is a new variable whose value should be equal to 23+12-5.</p>
<p>Let's try these in a program</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[2]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">x</span><span class="o">=</span><span class="mi">23</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;x = &quot;</span><span class="p">,</span><span class="n">x</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>x =  23
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[3]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">y</span><span class="o">=</span><span class="n">x</span><span class="o">+</span><span class="mi">12</span><span class="o">-</span><span class="mi">5</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;y =&quot;</span><span class="p">,</span><span class="n">y</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>y = 30
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="mi">23</span><span class="o">+</span><span class="mi">12</span><span class="o">-</span><span class="mi">5</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>30
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
<p>We ran 3 commands. First we created a variable 'x' with a value of 23. We verified it value by using a print() method!
Second, we created another variable called 'y' whose values is equal to mathematical operation of 'x+12-5'. If you remember basic algebra, this is exactly that. Finally, we confirmed that value of 'y' is exactly equal to 23+12-5.</p>
<p>Hopefully, you got a feel of variables. Variables are not limited to just numbers though. We can also store text. For example:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[5]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">name</span> <span class="o">=</span> <span class="s2">&quot;Sadanand Singh&quot;</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;My Name is:&quot;</span><span class="p">,</span> <span class="n">name</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>My Name is: Sadanand Singh
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
<p>Here, we saved my name <em>Sadanand Singh</em> in a variable called "name".</p>
<p>Concept of variable is very fundamental to any programming language. You can think of them as tokens that store some value.</p>
<p>Lets consider this example to understand variable in more detail.</p>
<p>You are doing your taxes, all of your calculations depend on your net income. If you do all your calculation in terms of actual value of net income, every time you write the number, your chances of making a mistake increases. Furthermore, suppose, you want to update the income due to some mistake in the beginning, now you have update every place where you used your income.</p>
<p>Lets consider a second case where you declare a variable called "income", and store income = 30000. Now, any time you do any calculation with income, you will be using the variable "income". In this framework, because you have to type your income just once, chances of making mistakes are least and changing it needs just one change!</p>
</div>
</div>
</div>

### Math Operations

Now that we know how to declare and use variables, we will look at first what all we can do with numbers in python.
Using simple math operations are extremely easy in Python. Here are all the basic math operations that one can do in Python.


| Syntax   |           Math          | Operation Name |
|--------|-----------------------|--------------|
| `a+b`    | $a + b$                   | Addition       |
| `a-b`    | $a - b$                   | Subtraction    |
| `a*b`    | $a \\times b$             | Multiplication |
| `a/b`    | $a \\div b$              | Division       |
| `a**b`   | $a^b$                   | Power/Exponent |
| `abs(a)` |  $\\lvert a \\rvert$    | Absolute Value |
| `-a `    |  $-1 \\times a$          | Negation       |
| `a//b`   | quotient of $a \\div b$  | Quotient       |
| `a%b`    | Remainder of $a \\div b$ | Remainder         |

Here are some example operation. Please repeat these and observe the use of parenthesis in using the BODMAS principle.


<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[6]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="mi">3</span> <span class="o">+</span> <span class="mi">5</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[6]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>8</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="mi">2</span> <span class="o">*</span> <span class="mi">3</span> <span class="o">+</span> <span class="mf">3.34</span> <span class="o">+</span> <span class="mi">4</span> <span class="o">-</span> <span class="mf">45.67</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[7]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>-32.33</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="mf">12.7</span> <span class="o">-</span> <span class="mi">10</span> <span class="o">*</span> <span class="mf">23.5</span> <span class="o">/</span> <span class="mf">0.5</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[8]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>-457.3</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="mi">12</span> <span class="o">-</span> <span class="p">(</span><span class="mi">11</span> <span class="o">+</span> <span class="mi">34</span><span class="p">)</span> <span class="o">/</span> <span class="mi">2</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[9]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>-10.5</pre>
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span><span class="p">,</span><span class="n">b</span><span class="o">=</span><span class="mi">5</span><span class="p">,</span><span class="mi">6</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Above is a special case of assigning multiple variables together. In the above example we stored a=5 and b=6. Lets confirm these:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[11]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;a = &quot;</span><span class="p">,</span><span class="n">a</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;b = &quot;</span><span class="p">,</span><span class="n">b</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>a =  5
b =  6
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[12]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c</span> <span class="o">=</span> <span class="n">a</span><span class="o">**</span><span class="n">b</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot; a raised to the power b is:&quot;</span><span class="p">,</span><span class="n">c</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre> a raised to the power b is: 15625
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
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">b</span> <span class="o">=</span> <span class="o">-</span><span class="n">b</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[14]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;b = &quot;</span><span class="p">,</span><span class="n">b</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>b =  -6
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
<p>Can you guess what we did here? First we use negation operation to get "-b" i.e. -6. Then, we we redefined b to be equal to -6! Let consider the following example: a = a-b-3. What do you expect the value to be? Now lets check if you are correct:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[15]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span> <span class="o">=</span> <span class="n">a</span><span class="o">-</span><span class="n">b</span><span class="o">-</span><span class="mi">3</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;new value of a is: &quot;</span><span class="p">,</span><span class="n">a</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>new value of a is:  8
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
<p>What do you expect if we do b = -b again?</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">b</span> <span class="o">=</span> <span class="o">-</span><span class="n">b</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;New Value of b is:&quot;</span><span class="p">,</span><span class="n">b</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>New Value of b is: 6
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span><span class="o">//</span><span class="n">b</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[17]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>1</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">a</span><span class="o">%</span><span class="k">b</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[18]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>2</pre>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">b</span><span class="o">**-</span><span class="mi">2</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt output_prompt">Out[19]:</div>



<div class="output_text output_subarea output_execute_result">
<pre>0.027777777777777776</pre>
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
<p>You can perform many other advanced math operations using the "math module". To use them, first you will need to import the math module in your code like this:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">math</span>
</pre></div>

</div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered">
<div class="prompt input_prompt">
</div>
<div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<p>Then, you use operations like the following:</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">c</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">sqrt</span><span class="p">(</span><span class="mi">25</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">log10</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
<span class="n">c</span> <span class="o">=</span> <span class="n">math</span><span class="o">.</span><span class="n">cos</span><span class="p">(</span><span class="n">math</span><span class="o">.</span><span class="n">pi</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">c</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>5.0
2.302585092994046
1.0
-1.0
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
<p>You can all other available mathematical operation in this module on the <a href="https://docs.python.org/3/library/math.html">python website</a>.</p>

</div>
</div>
</div>


### print() Function in Python

Primary way to see and print information on your screen in python is using a method/function called `print()`. We will learn more about functions in python later. For today, you can think of functions as a program that "does something". For example, the function `print()`, does the job of printing things on screen.

Notice the use of `()` in functions. `()` separates a function from a variable. For example, "foo" is a variable, whereas `foo()` is a function, sometimes also called as _method_.

Functions also have a concept of arguments. Arguments can be thought as inputs to functions. For example, we have function that adds 2 numbers, then this function will need 2 arguments, the two numbers that we want to add. We can denote this function as, `addition(a,b)`.

Similarly, functions also have a concept of return values. Return value can be thought as the output of that function. For example, in the above example of `addition(a,b)` function, sum of two numbers will be the "return value" of the function. We can write this as, `c = addition(a,b)`. Here, a and b are arguments to function addition() and c is the return value of this function.

A function can have any number of arguments, zero to any number; where it can have either zero or 1 return values.

Now, coming back to the `print()` method, that we have been using throughout this tutorial.

`print()` method can take any number of arguments separated by commas. All it does is to "print" those on your screen. Lets look at some examples:

<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="mi">3</span><span class="p">,</span><span class="mi">4</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;My Name is Sadanand Singh&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;My Name is &quot;</span><span class="p">,</span><span class="s2">&quot;Sadanand Singh&quot;</span><span class="p">,</span><span class="s2">&quot;and My age is: &quot;</span><span class="p">,</span> <span class="mi">29</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>3 4
My Name is Sadanand Singh
My Name is  Sadanand Singh and My age is:  29
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
<p>Now, lets try something fun.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;My Name is&quot;</span><span class="p">,</span><span class="s2">&quot;Sadanand&quot;</span><span class="p">,</span> <span class="n">sep</span><span class="o">=</span><span class="s2">&quot;***&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>My Name is***Sadanand
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;My Name is&quot;</span><span class="p">,</span><span class="s2">&quot;Sadanand&quot;</span><span class="p">,</span><span class="s2">&quot;Singh&quot;</span><span class="p">,</span><span class="s2">&quot;My Age is&quot;</span><span class="p">,</span><span class="s2">&quot;12&quot;</span><span class="p">,</span><span class="s2">&quot;&quot;</span><span class="p">,</span><span class="n">sep</span><span class="o">=</span><span class="s2">&quot;***&quot;</span><span class="p">)</span>
</pre></div>

</div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">
<div class="prompt"></div>

<div class="output_subarea output_stream output_stdout output_text">
<pre>My Name is***Sadanand***Singh***My Age is***12***
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
<p>Can you explain what is happening here!</p>
</div>
</div>
</div>

## Excercise

We will all things we have learned today using the exercise below.</p>
<p>We will follow the tax preparation example:

1. Create a variable to store "income"
2. Create another variable called "taxRate" which is equal to 1/100000th of "income".
3. Net federal tax will be equal to 1.5 times income times taxRate
4. Net state tax will be equal to square root on federal tax
5. Net tax will be federal tax + state tax
6. Total final tax will be Net tax + log to the base of 2 of Net Tax
7. Print following values clearly using print(): income, taxRate, Federal Tax, State Tax, Net Tax and Final Tax.
8. First run with an income of 60000
9. Repeat with an income of 134675


Your output should look like the following in two cases.

__Case 1: income = 60000__

1. Total Income is: 60000
2. Tax Rate is: 0.059999999999999998
3. Total Federal Tax is: 1800.0
4. Total State Tax is: 42.426406871192853
5. Net Tax is: 1842.4264068711927
6. Total Tax is: 1853.2737981499038

__Case 2: income = 134675__

1. Total Income is: 134675
2. Tax Rate is: 0.13467499999999999
3. Total Federal Tax is: 9068.6778125000001
4. Total State Tax is: 95.229605756298284
5. Net Tax is: 9163.9074182562981
6. Total Tax is: 9177.0691654243201

Great! [Next week]({{< relref "pythonTutorialWeek2.md" >}}) we dive into Python further.

<br>
