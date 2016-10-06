.. title: Support Vector Machines
.. slug: svmModels
.. date: 2016-10-15 20:30:00 UTC-07:00
.. tags: ML, mathjax, Python
.. category: ML
.. link:
.. disqus_identifier: svmModels.sadanand
.. description:
.. type: text
.. author: Sadanand Singh

In this post we will explore a class of machine learning methods called `Support
Vector Machines <https://en.wikipedia.org/wiki/Support_vector_machine>`__ also
known commonly as *SVM*.

What is SVM?
~~~~~~~~~~~~~~

SVM is a `supervised machine learning
<https://en.wikipedia.org/wiki/Supervised_learning>`__ algorithm which can be
used for both classification and regression.

In the simplest classification problem, given some data points each belonging to
one of two classes, and the goal is to decide which class a new data point will
be in. A simple linear solution to this problem can be viewed in a framework
where a data point is viewed as a *p*-dimensional vector (a list of *p*
numbers), and we want to know whether we can separate such points with a
(*p-1*)-dimensional hyperplane. There are many hyperplanes that might classify
the data. One reasonable choice as the best hyperplane is the one that
represents the largest separation, or margin, between the two classes. So we
choose the hyperplane so that the distance from it to the nearest data point on
each side is maximized. If such a hyperplane exists, it is known as the maximum-
margin hyperplane and the linear classifier it defines is known as a maximum
margin classifier; or equivalently, the perceptron of optimal stability.

.. figure:: https://upload.wikimedia.org/wikipedia/commons/thumb/b/b5/Svm_separating_hyperplanes_(SVG).svg/2000px-Svm_separating_hyperplanes_(SVG).svg.png
   :alt: SVM

In the figure above, H\ :sub:`1`  does not separate the classes, H\ :sub:`2`
does but only with a small margin. H\ :sub:`3` separates with maximum margin.

The maximal margin classifier is a very natural way to perform classification,
if a separating hyperplane exists. However, in most real-life cases no
separating hyperplane exists, and so there is no maximal margin classifier.
However, we can extend the concept of a separating hyperplane in order to
develop a hyperplane that almost separates the classes, using a so-called
*"soft margin"*. The generalization of the maximal margin classifier to the
non-separable case is known as the *"support vector"* classifier.





