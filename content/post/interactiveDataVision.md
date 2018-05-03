---
title: "Interactive Data Visualization in Python"
date: 2018-04-28
tags:
    - "Data Science"
    - "Python"
categories:
    - "Data Science"
slug: "interactivedatavis"
link:
authors:
    - "Sadanand Singh"
hasMath: false
notebook: false
draft: false
bokeh: "interactivePlots_min.js"
disqus_identifier: "interactivedatavis.sadanand"
description:
---

There are two types of data visualizations: _exploratory_ and _explanatory_.
Explanatory analysis is what happens when you have something specific you want 
to show an audience. The aim of **explanatory** visualizations is to tell 
stories - they’re carefully constructed to surface key findings.

<!--more-->

Exploratory analysis, on the other hand, is what you do to get familiar with 
the data. You may start out with a hypothesis or question, or you may just 
really be delving into the data to determine what might be interesting about 
it. **Exploratory** visualizations, "create an interface into a dataset or 
subject matter... they facilitate the user exploring the data, letting them 
unearth their own insights: findings they consider relevant or interesting."

In a previous series of posts on
[exploratory data analysis (EDA)][EDA] - [EDA 1], [EDA 2], [EDA 3] and
[EDA 4], we have covered static plotting in python using major libraries
like [matplotlib], [seaborn], [plotnine], and [pandas]. `plotnine` is an implementation of a grammar of graphics in Python, based on the [ggplot2] library in R. The grammar allows users to compose plots by explicitly mapping data to the visual objects that make up the plot.

[EDA]: https://en.wikipedia.org/wiki/Exploratory_data_analysis
[EDA 1]: {{< relref "reddit.md" >}}
[EDA 2]: {{< relref "oneVarEDA.md" >}}
[EDA 3]: {{< relref "twoVarEDA.md" >}}
[EDA 4]: {{< relref "multiVarEDA.md" >}}
[matplotlib]: https://matplotlib.org/
[pandas]: https://pandas.pydata.org/
[seaborn]: https://seaborn.pydata.org/
[plotnine]: https://plotnine.readthedocs.io/en/stable/
[ggplot2]: http://ggplot2.org/

In this article, we will focus on EDA using interactive plots. More often than not, exploratory visualizations are easier when they are interactive!

<!--TOC-->

# Python Libraries

Although there are few libraries in python that can help us make interactive 
plots, I find [bokeh] and [holoviews] to be the only ones that can cover most 
use cases. Others like [plotly] and [pygal] seem to be too specific and [mpld3]
is no longer being actively maintained.

[bokeh]: https://bokeh.pydata.org/en/latest/
[holoviews]: https://holoviews.org/
[plotly]: https://plot.ly/
[pygal]: http://pygal.org/en/stable/
[mpld3]: https://github.com/mpld3/mpld3

`bokeh` provides fundamental blocks for making interactive plots, following 
the grammar of graphics. `holoviews` on the hand uses bokeh as back-end to 
provide high level APIs for making plots. All of these interactive plots can 
be viewed in a browser and are aided by corresponding bokeh javascript and css 
files.

{{< card "" "**Embedding bokeh Plots in Web Pages**" >}}
In order to incorporate bokeh figures in a web page, you will first need to include following `css` and `js` files in your page:

{{< highlight lang="html" linenos="true" >}}
<!-- css -->
<link href="//cdnjs.cloudflare.com/ajax/libs/bokeh/0.12.15/bokeh.min.css" rel="stylesheet" type="text/css">
<link href="//cdnjs.cloudflare.com/ajax/libs/bokeh/0.12.15/bokeh-widgets.min.css" rel="stylesheet" type="text/css">
<link href="//cdnjs.cloudflare.com/ajax/libs/bokeh/0.12.15/bokeh-tables.min.css" rel="stylesheet" type="text/css">

<!-- java script -->
<script src="//cdnjs.cloudflare.com/ajax/libs/bokeh/0.12.15/bokeh.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/bokeh/0.12.15/bokeh-widgets.min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/bokeh/0.12.15/bokeh-tables.min.js"></script>
{{< /highlight >}}

The "-widgets" files are only necessary if your document includes bokeh widgets. Similarly, the "-tables" files are only necessary if you are using Bokeh data tables in your document.

Then you can use the `bokeh.embed.components()` to generate relevant code for 
your plots. This function returns a `<script>` that contains the data for your 
plot, together with an accompanying `<div>` tag that the plot view is loaded 
into. These tags can be used in HTML documents however you like:

{{< highlight lang="python" linenos="true" >}}
from bokeh.plotting import figure
from bokeh.embed import components

plot = figure()
plot.circle([1,2], [3,4])

script, div = components(plot)
{{< /highlight >}}

The returned `<script>` will look something like:

{{< highlight lang="html" linenos="true" >}}
<script type="text/javascript">
    (function() {
  var fn = function() {
    Bokeh.safely(function() {
      var docs_json = { DOCUMENT DATA HERE };
      var render_items = [{
        "docid":"6833819f-9b5b-4904-821e-3f5eec77de9b",
        "elementid":"9574d123-9332-4b5f-96cc-6323bef37f40",
        "modelid":"7b328b27-9b14-4f7b-a5d8-0138bc7b0f59"
      }];

      Bokeh.embed.embed_items(docs_json, render_items);
    });
  };
  if (document.readyState != "loading") fn();
  else document.addEventListener("DOMContentLoaded", fn);
})();

</script>
{{< /highlight >}}

The resulting `<div>` will look something like:

{{< highlight lang="html" linenos="true" >}}
<div class="bk-root">
    <div class="bk-plotdiv" id="9574d123-9332-4b5f-96cc-6323bef37f40"></div>
</div>
{{< /highlight >}}

There will be one `<div>` for each of your plots and they should be placed at 
where you want your plot to appear. The `<script>` section should be placed 
in a typical place - the bottom of the `<body>` section for late loading.

{{< /card >}}

# Examples

Bokeh has built-in support for various types of interactions (like pan, wheel zoom, box zoom, reset and save etc.) on all plots. Additionally, all of such interactions can be customized.

In the following sections, we will look at few major types of interactions that are required typically in an exploratory plot.

## Hover/ Tool-tips

Visualization of high dimensional data is a pretty common task in data science projects. The two most common algorithms to project high dimensional data to 2-dimensional space are [t-sne] and [UMAP]. The [scikit-learn][sklearn] and [umap-learn] python libraries provide a neat implementation of these algorithms.

ss

[t-sne]: https://lvdmaaten.github.io/tsne/
[umap]: https://arxiv.org/abs/1802.03426
[sklearn]: http://scikit-learn.org/stable/modules/generated/sklearn.manifold.TSNE.html
[umap-learn]: https://github.com/lmcinnes/umap

<div style="display:table; margin:0 auto;">
  <div class="bk-root">
      <div class="bk-plotdiv" id="e50aea6c-81ff-4db9-b1ff-4a666e47aa94"></div>
  </div>
</div> 

## Linked Plots

## Interacting via Data


# High level bokeh plots using holoviews Library

<!-- GMap API KEY: AIzaSyAVRy9HYHhRWrZQwjSdTMJuEo-63Gjoak4 -->

