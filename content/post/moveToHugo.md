---
title: "Switching to Hugo from Nikola"
date: 2017-06-23T17:53:58-07:00
tags:
    - "Blog"
    - "Hugo"
    - "golang"
categories:
    - "Blog"
slug: "nikola2hugo"
link:
hasMath: false
notebook: false
draft: false
disqus_identifier: "nikola2hugo.sadanand"
readingTime: 10
description:
---

I have been using [Nikola] to build this blog. Its a great static site 
build system that is based on Python. However, It has some crazy 
amount of dependencies (to have reasonable looking site). It
uses [restructured text (rst)][rst] as the primary language for 
content creation. Personally, I use markdown for almost every thing 
else - taking notes, making diary, code documentation etc. 
Furthermore, given Nikola tries to support almost everything in a 
static site builder, lately its is becoming more and more bloated.
Case in  point, recently it got support for [shortcodes] and although that did 
enable me to write posts in Markdown, but it is so difficult to 
develop them (It does not help to have almost no documentation/guide 
for their development). They are heavily tied to the [plugin] system 
with light support for template based shortcodes.

<!--more-->

[nikola]: https://getnikola.com
[rst]: http://docutils.sourceforge.net/rst.html
[shortcodes]: https://getnikola.com/handbook.html#shortcodes
[plugin]: https://plugins.getnikola.com

I really have nothing against [Nikola]. However, I did not feel at home - I wanted a light system that focused on markdown and had all the flexibilities that I wanted. My research soon brought me to [Hugo].


[Hugo]: https://gohugo.io

<!--TOC-->

# Hugo - the blazing fast site generator

[Hugo] is a light weight, fast and modern static website engine written in [go]. It literally takes just milliseconds to build your entire site. For the given lightness, it is highly flexible as well. You can organize your content however you want with any URL structure, group your content using your own indexes and categories and define your own _metadata_ in any format: `YAML`, `TOML` or `JSON`. I was impressed! Keep in my mind, `python` is still my primary language of programming for scripting and machine learning. And, I have almost no  programming experience with `go`.

[go]: https://golang.org

I chose `YAML` for all the configuration as well as _metadata_. In my next step to make this move, I had to choose the theme for my blog. If you have been following me, I have been using several flavors
of [Bootswatch] themes. So my first goal was implement my heavily modified version of [bootswatch] theme in Hugo.

[Bootswatch]: https://bootswatch.com

# Bootswatch Theme

Developing a theme from scratch (*Well, the implementation from scratch, as I all I am trying to do is mimic/improvise my current theme from Nikola*) turned out to be a great adventure and learning exercise. It helped me understand the Hugo architecture in great detail. It did help to have some good [documentation] written for developers, not users! Although, Hugo's documentation can surely help itself with some cleaning and some fresher looks!

Hugo uses [go templates] with many extra functions and set of variables provided by Hugo. I personally feel Hugo's template-ing system to be more flexible and easier than [Mako] - the one used by default by Nikola.

[go templates]: https://golang.org/pkg/text/template/
[Mako]: http://www.makotemplates.org
[documentation]: https://gohugo.io/overview/introduction/

I converted almost all of Mako theme from Nikola website to Hugo's format and architecture with additions (copied features and code) from a nice theme called [TranqilPeak](https://themes.gohugo.io/hugo-tranquilpeak-theme/). In particular, I liked their fonts, search feature for taxonomies pages. Copying these features also meant I had to learn a bit of `javascript` and `css`. You can find a working copy of my theme in the `src` branch of [gihub repository](https://github.com/sadanand-singh/sadanand-singh.github.io) of my blog. I plan to release this theme as a standalone theme in near future though.

# Shortcodes

Given I am using a [bootstrap] based theme, I like having a lot of its features available to me when I am writing in Markdown. The powerful template based [shortcodes in Hugo](https://gohugo.io/extras/shortcodes/) provide a great way to write custom html code inside markdown. I feel Hugo shortcodes are so powerful, you could develop your own grammar of markup language in it! :yum:

Some of my shortcodes are basically based on [bootstrap] classes like
panel, label, emphasis, highlighted text, and block quotes. I also liked the figure command provided by restructured text in Nikola. Luckily, same features are available in Hugo using a default shortcode called `figure`. Hugo also provides several other useful default shortcodes like `youtube`, `ref/relref` for referencing other posts etc.

[bootstrap]: http://getbootstrap.com

I have also some additional shortcodes for codeblocks and math. I will be detailing about them in a bit more detail in the next section. All of my shortcodes are available with the theme in the same [github repo](https://github.com/sadanand-singh/sadanand-singh.github.io).

# Other Caveats and Fixes

While converting to Hugo was almost fun, there were some caveats. The issues I faced were mainly with home page, site search, and ipython notebook posts.

## Home Page with Content and Post Lists

Getting home page to work was very simple. Hugo documents page provides a very clear details about order in which various templates are looked. For home page, you will need to provide a template for `index.html`. Then Inside the `content` folder, you can put metadata and content for the home page in a file named `_index.md`. 

I also added following template code in the index.html file to get list of posts with certain tags:

{{< code-block code="html" >}}
{{ $.Scratch.Add "mlposts" slice }}
{{ $tags := (slice "Machine Learning" "EDA" "Kaggle" "ML" "Deep Learning" "DL" "Data Science") }}
{{ range .Site.RegularPages }}
    {{ $page := . }}
    {{ $has_common_tags := intersect $tags .Params.tags | len | lt 0 }}
    {{ if $has_common_tags }}
        {{ $.Scratch.Add "mlposts" $page }}
    {{ end }}
{{ end }}
{{ $cand := .Scratch.Get "mlposts" }}
{{ range first 10 $cand }}
    {{ .Render "li"}}
{{ end }}
{{< /code-block >}}

## tipue Search

Hugo has support for several output formats, including HTML and JSON. For implementing [tipue search](http://www.tipue.com/search/), we need to generate a JSON file with site content. This can be done by adding following to the configuration file:

{{< code-block code="yaml" >}}
# Output formats
outputs:
  home: [ "HTML", "JSON"]
  page: [ "HTML"]
{{< /code-block >}}

and, using the following `index.json` template:

{{< code-block code="html" >}}
{{- $.Scratch.Add "index" slice -}}
{{- range where .Site.RegularPages "Type" "not in"  (slice "page" "json" "nosearch") -}}
{{- $.Scratch.Add "index" (dict "url" .Permalink "title" .Title "text" .Plain "tags" (delimit .Params.tags ", ")) -}}
{{- end -}}
{"pages": {{- $.Scratch.Get "index" | jsonify -}}}
{{< /code-block >}}

Now, include the following `css` in the `<head>` of your pages:

    <link href="//cdnjs.cloudflare.com/ajax/libs/Tipue-Search/5.0.0/tipuesearch.css" rel="stylesheet" type="text/css">

And, the following content in the `foot` of pages:

    <!-- Modal -->
    <div id="search-results" class="modal fade" role="dialog" style="height: 80%;">
        <div class="modal-dialog">
            <!-- Modal content-->
            <div class="modal-content">
              <div class="modal-header">
                <button type="button" class="close" data-dismiss="modal">×</button>
                <h4 class="modal-title">Search Results:</h4>
              </div>
              <div class="modal-body" id="tipue_search_content" style="max-height: 600px; overflow-y: auto;">
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-default" data-dismiss="modal">Close</button>
              </div>
            </div>
        </div>
    </div>

    <script>
    $(document).ready(function() {
        var url1 = "https://cdnjs.cloudflare.com/ajax/libs/Tipue-Search/5.0.0/tipuesearch_set.js";
        var url2 = "https://cdnjs.cloudflare.com/ajax/libs/Tipue-Search/5.0.0/tipuesearch.min.js";
        $.when(
            $.getScript( url1 ),
            $.getScript( url2 ),
            $.Deferred(function( deferred ){
                $( deferred.resolve );
            })
        ).done(function() {
            $('#tipue_search_input').tipuesearch({
                'mode': 'json',
                'contentLocation': '/index.json'
            });
            $('#tipue_search_input').keyup(function (e) {
                if (e.keyCode == 13) {
                    $('#search-results').modal()
                }
            });
        });
    });
    </script>
    <!--SCRIPTS END-->

And, of course you will need a form/input for performing the search:

    <span class="navbar-form navbar-right">
        <input type="text" id="tipue_search_input" class="form-control" placeholder="Search">
    </span>

## Code Highlighting

Although, by default Hugo provides code highlighting using the [pygments](http://pygments.org), I prefer to use client-side highlighting using [prism.js](http://prismjs.com). I also use the following [plugins](http://prismjs.com/#plugins) of `prism.js` for line numbers, highlighting and cleanup of white space:

- [Line Highligh](http://prismjs.com/plugins/line-highlight/)
- [Line Numbers](http://prismjs.com/plugins/line-numbers/)
- [Normalize Whitespace](http://prismjs.com/plugins/normalize-whitespace/)

Finally, I create a shortcode called _code-block_ to add relevant classes and variables around `<code` and `<pre` tags so that prism could highlight code correctly.

## jupyter Notebooks as Posts

One of the advantages of  using Nikola is that, it provides native support for writing blog posts in jupyter notebooks.

But, on some google search, I found this neat solution at the following [Blog](https://sharmamohit.com/post/jupyter-notebooks-in-blog/).

In summary, the solution is very simple - Use the linked [jupyter.css](http://sharmamohit.com/css/jupyter.css) file in your template. Then for any jupyter notebook, convert it to basic html using the following command:

{{< code-block code="bash" >}}
jupyter nbconvert --to html --template basic *source_file.ipynb*
{{< /code-block >}}

Then, finally, create a markdown file for your post, where simply put the contents of this html file as markdown supports including raw HTML code!

## Latex Math Equations

I used [katex](https://github.com/Khan/KaTeX) for using math in markdown. I was having some issue with the multi-line display math equations, so I created shortcode called _tex_ to write html code explicitly so that katex could handle that easily.


So there you have it. I have my blog now up and running with Hugo. Hope I will be more active here, since it now takes only seconds to deploy once I have a post written. No excuses now! :stuck_out_tongue_winking_eye:
