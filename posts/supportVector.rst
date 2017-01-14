.. title: Support Vector Machines
.. slug: svmModels
.. date: 2016-10-10 20:30:00 UTC-07:00
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


Introduction
------------

SVM is a `supervised machine learning
<https://en.wikipedia.org/wiki/Supervised_learning>`__ algorithm which can be
used for both classification and regression.

.. figure:: ../../images/binaryclass_2d-300x284.png
    :alt: SVC
    :align: right

In the simplest classification problem, given some data points each belonging to
one of two classes, the goal is to decide which class a new data point will
be in. A simple linear solution to this problem can be viewed in a framework
where a data point is viewed as a *p*-dimensional vector, and we want to know
whether we can separate such points with a
(*p-1*)-dimensional hyperplane.

There are many hyperplanes that might classify the data. One reasonable choice
as the best hyperplane is the one that represents the largest separation, or
margin, between the two classes. So we choose the hyperplane so that the
distance from it to the nearest data point on each side is maximized. If such a
hyperplane exists, it is known as the maximum- margin hyperplane and the linear
classifier it defines is known as a **maximum margin classifier**; or
equivalently, the perceptron of optimal stability.

The figure on the right is a binary classification problem (points labeled
:math:`y_i = \pm 1`) that is linearly separable in space defined by the vector
**x**. Green and purple line separate two classes with a small margin, whereas
yellow line separates them with the maximum margin.

.. figure:: ../../images/binaryclass_margin-300x266.png
    :alt: MaxMarginClassification
    :align: left

Mathematically, for the linearly separable case, any point **x** lying on the
separating hyperplane satisfies: :math:`\mathbf{w} . \mathbf{x} = 0`, where
**w** is the vector normal to the hyperplane, and *b* is a constant that
describes how much plane is shifted relative to the origin. The distance of the
hyperplane from the origin is :math:`\frac{b}{\lVert \mathbf{w} \rVert}`.

Now draw parallel planes on either side of the decision boundary, so we have
what looks like a channel, with the decision boundary as the central line, and
the additional planes as gutters. The margin, i.e. the width of the channel, is
:math:`(d_+ + d_-)` and is restricted by the data points closest to the
boundary, which lie on the gutters. The two bounding hyperplanes of the channel
can be represented by a constant shift in the decision boundary. In other words,
these planes ensure that all the points are at least a signed distance `d` away
from the decision boundary. The channel region can be also represented by the
following equations:

.. math::

    \mathbf{w.x} + b \ge +a, \text{for  } y_i = +1 \\
    \mathbf{w.x} + b \le -a, \text{for  } y_i = -1

These two conditions can be put more succinctly as:

.. math::

    y_i (\mathbf{w.x} + b) \ge a, \forall i

Using the formulation of distance from origin of three hyper planes, we can show
that, :math:`d_+ + d_- = 2a / \lVert \mathbf{w} \rVert`. Without any loss of
generality, we can set :math:`a = 1`, since it only sets the scale (units) of
`b` and **w**. So to maximize the margin, we have to maximize
:math:`1 / \lVert \mathbf{w} \rVert`.
Such a non-convex objective function can be avoided if we
choose in stead to minimize :math:`{\lVert \mathbf{w} \rVert}^2`.

In summary for a problem with `m` numbers of training data points, we need to solve
the following quadratic programming problem:

.. math::

    \begin{aligned}
    & {\text{minimize  }}
    f(w)  \equiv \frac{1}{2} {\lVert \mathbf{w} \rVert}^2 \\
    & \text{subject to  }
    g(\mathbf{w}, b) \equiv -y_i (\mathbf{w.x} + b) + 1 \le 0, i = 1 \ldots m
    \end{aligned}

The maximal margin classifier is a very natural way to perform classification,
if a separating hyperplane exists. However, in most real-life cases no
separating hyperplane exists, and so there is no maximal margin classifier.

Support Vector Classifier
-------------------------

.. figure:: ../../images/softmargin-300x266.png
    :alt: MaxMarginClassification
    :align: right

We can extend the concept of a separating hyperplane in order to develop a
hyperplane that almost separates the classes, using a so- called *"soft
margin"*. The generalization of the maximal margin classifier to the non-
separable case is known as the *"support vector"* classifier.

For non-separable data, we relax the constraints in the above objective function
while penalizing misclassified points via a cost parameter `C` and slack
variables :math:`\xi_i` that define the amount by which data points are on the
wrong side of the margin.

.. math::

    \begin{aligned}
    & {\text{minimize  }}
    \frac{1}{2} {\lVert \mathbf{w} \rVert}^2 + C \sum_{i}^{m} \xi_i\\
    & \text{subject to  }
    y_i (\mathbf{w.x} + b) \ge 1 - \xi_i, \text{  }
    \text{   and   } \xi_i \ge 0, \text{   } i = 1 \ldots m
    \end{aligned}

Now, the question before us is to find a way to solve this optimization problem efficiently.

For simplicity, let us start with the first optimization problem for the separable case.
