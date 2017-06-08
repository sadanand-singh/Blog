.. title: Support Vector Machines
.. slug: svmModels
.. date: 2016-11-11 10:30:00 UTC-07:00
.. tags: mathjax, Algorithms, Machine Learning
.. category: Algorithms, Machine Learning
.. link:
.. disqus_identifier: svmModels.sadanand
.. description:
.. type: text
.. author: Sadanand Singh

In this post we will explore a class of machine learning methods called
`Support Vector Machines
<https://en.wikipedia.org/wiki/Support_vector_machine>`__ also known commonly
as *SVM*.

.. TEASER_END

.. contents:: Table of Contents

Introduction
------------

SVM is a `supervised machine learning
<https://en.wikipedia.org/wiki/Supervised_learning>`__ algorithm which can be
used for both classification and regression.

.. figure:: https://res.cloudinary.com/sadanandsingh/image/upload/v1496959802/binaryclass_2d-300x284_u4bkzu.png
    :alt: SVC
    :align: right

In the simplest classification problem, given some data points each belonging
to one of the two classes, the goal is to decide which class a new data point
will be in. A simple linear solution to this problem can be viewed in a
framework where a data point is viewed as a *p*-dimensional vector, and we want
to know whether we can separate such points with a (*p-1*)-dimensional
hyperplane.

There are many hyperplanes that might classify the data. One reasonable choice
as the best hyperplane is the one that represents the largest separation, or
margin, between the two classes. So we choose the hyperplane so that the
distance from it to the nearest data point on each side is maximized. If such a
hyperplane exists, it is known as the maximum-margin hyperplane and the linear
classifier it defines is known as a **maximum margin classifier**; or
equivalently, the perceptron of optimal stability.

The figure on the right is a binary classification problem (points labeled
:math:`y_i = \pm 1`) that is linearly separable in space defined by the vector
**x**. Green and purple line separate two classes with a small margin, whereas
yellow line separates them with the maximum margin.

.. figure:: https://res.cloudinary.com/sadanandsingh/image/upload/v1496959803/binaryclass_margin-300x266_lq3h3q.png
    :alt: MaxMarginClassification
    :align: left

Mathematically, for the linearly separable case, any point **x** lying on the
separating hyperplane satisfies: :math:`\mathbf{x}^T\mathbf{w} = 0`, where
**w** is the vector normal to the hyperplane, and *b* is a constant that
describes how much plane is shifted relative to the origin. The distance of the
hyperplane from the origin is :math:`\frac{b}{\lVert \mathbf{w} \rVert}`.

Now draw parallel planes on either side of the decision boundary, so we have
what looks like a channel, with the decision boundary as the central line, and
the additional planes as gutters. The margin, i.e. the width of the channel, is
:math:`(d_+ + d_-)` and is restricted by the data points closest to the
boundary, which lie on the gutters. The two bounding hyperplanes of the channel
can be represented by a constant shift in the decision boundary. In other
words, these planes ensure that all the points are at least a signed distance
`d` away from the decision boundary. The channel region can be also
represented by the following equations:

.. math::
    \begin{aligned}
    & \mathbf{x}_i^T\mathbf{w} + b \ge +a, \text{for  } y_i = +1 \\
    & \mathbf{x}_i^T\mathbf{w} + b \le -a, \text{for  } y_i = -1
    \end{aligned}

These conditions can be put more succinctly as:

.. math::
    y_i (\mathbf{x}_i^T\mathbf{w} + b) \ge a, \forall i

Using the formulation of distance from origin of three hyper planes, we can
show that, the margin, `M` is equivalent to
:math:`d_+ + d_- = 2a / \lVert \mathbf{w} \rVert`.
Without any loss of generality, we can set :math:`a = 1`, since it only
sets  the scale (units) of :math:`b` and :math:`\mathbf{w}`.
So to maximize the margin, we have to maximize
:math:`1 / \lVert \mathbf{w} \rVert`. Such a non-convex
objective function can be avoided if we choose in stead to minimize
:math:`{\lVert \mathbf{w} \rVert}^2`.

In summary, for a problem with `m` numbers of training data points, we need to
solve the following quadratic programming problem:

.. math::
    \begin{aligned}
    & {\text{maximize  }}
    M \\
    & \text{subject to  }
    y_i (\mathbf{x}_i^T\mathbf{w} + b) \ge M, \forall \text{ } i = 1 \ldots m
    \end{aligned}

This can be more conveniently put as:

.. math::
    \begin{aligned}
    & {\text{minimize  }}
    f(w)  \equiv \frac{1}{2} {\lVert \mathbf{w} \rVert}^2 \\
    & \text{subject to  }
    g(\mathbf{w}, b) \equiv -y_i (\mathbf{x}_i^T\mathbf{w} + b) + 1 \le 0, i = 1 \ldots m
    \end{aligned}

The maximal margin classifier is a very natural way to perform classification,
if a separating hyperplane exists. However, in most real-life cases no
separating hyperplane exists, and so there is no maximal margin classifier.

Support Vector Classifier
-------------------------

.. figure:: https://res.cloudinary.com/sadanandsingh/image/upload/v1496959808/softmargin-300x266_qunbnb.png
    :alt: MaxMarginClassification
    :align: right

We can extend the concept of a separating hyperplane in order to develop a
hyperplane that *almost* separates the classes, using a so-called *"soft
margin"*. The generalization of the maximal margin classifier to the non-
separable case is known as the *"support vector"* classifier.

Assuming the classes overlap in the given feature space. One way to deal with
the overlap is to still maximize `M`, but allow for some points to be on the
wrong side of the margin. In order to allow these, we can define the slack variables as,
:math:`\xi = ( \xi_1, \xi_2 \ldots \xi_m)`.
Now, keeping the above optimization problem as a convex problem,
we can modify the constraints as:

.. math::
    \begin{aligned}
    & y_i (\mathbf{x}_i^T\mathbf{w} + b) \ge M(1-\xi_i), \forall \text{  } i = 1 \ldots m, \\
    & \xi_i \ge 0 \text{   and   } \sum_{i=1}^{m}\xi_i \le C \text{  }\forall \text{   } i = 1 \ldots m,
    \end{aligned}

We can think of this formulation in the following context. The value
:math:`\xi_i` in the constraint
:math:`y_i (\mathbf{x}_i^T\mathbf{w} + b) \ge M(1-\xi_i)`
is the proportional amount by which the prediction
:math:`f(x_i)=x_i^T\mathbf{w} + b` is on the wrong side of its margin. Hence by
bounding the sum :math:`\sum \xi_i`, we can bound the total proportional amount by
which predictions fall on the wrong side of their margin. Mis-classifications
occur when :math:`\xi_i > 1`, so bounding :math:`\sum \xi_i` at a value `K`
say, bounds the total number of training mis-classifications at `K`.

Similar to the case of maximum margin classifier, we can rewrite the
optimization problem more conveniently as,

.. math::
    \begin{aligned}
    & {\text{minimize  }}
    \frac{1}{2} {\lVert \mathbf{w} \rVert}^2 + C \sum_{i}^{m} \xi_i\\
    & \text{subject to  }
    y_i (\mathbf{x}_i^T\mathbf{w} + b) \ge 1 - \xi_i, \text{  }
    \text{   and   } \xi_i \ge 0, \text{   } i = 1 \ldots m
    \end{aligned}

Now, the question before us is to find a way to solve this optimization
problem efficiently.

The problem above is quadratic with linear constraints, hence is a convex
optimization problem. We can describe a quadratic programming solution using
Lagrange multipliers and then solving using the Wolfe dual problem.

The Lagrange (primal) function for this problem is:

.. math::
    L_P = \frac{1}{2} {\lVert \mathbf{w} \rVert}^2 + C \sum_{i}^{m} \xi_i - \sum_{i=1}^{m} \alpha_i[y_i (\mathbf{x}_i^T\mathbf{w} + b) - (1 - \xi_i)] - \sum_{i=1}^{m} \mu_i \xi_i,

which we can minimize w.r.t. :math:`\mathbf{w}`, `b`, and :math:`\xi_i`.
Setting the respective derivatives to zero, we get,

.. math::
    \begin{aligned}
    & \mathbf{w} = \sum_{i=1}^{m} \alpha_i y_i \mathbf{x_i} \\
    & 0 = \sum_{i=1}^{m} \alpha_i y_i \\
    & \alpha_i = C - \mu_i, \forall i,
    \end{aligned}

as well as the positivity constraints, :math:`\alpha_i`, :math:`\mu_i`,
:math:`\xi_i \ge 0, \text{  } \forall i`. By substituting these conditions back
into the Lagrange primal function, we get the Wolfe dual of the problem as,

.. math::
    L_D = \sum_{i=1}^{m} \alpha_i - \frac{1}{2} \sum_{i=1}^{m} \sum_{j=1}^{m} \alpha_i \alpha_j y_i y_j x_i^T x_j

which gives a lower bound on the original objective function of the quadratic
programming problem for any feasible point. We maximize :math:`L_D` subject to
:math:`0 \le \alpha_i \le C` and :math:`\sum_{i=1}^{m} \alpha_i y_i = 0`. In
addition to above constraints, the Karush-Kuhn-Tucker (KKT) conditions include
the following constraints,

.. math::
    \begin{aligned}
    & \alpha_i[y_i (\mathbf{x}_i^T\mathbf{w} + b) - (1 - \xi_i)] = 0, \\
    & \mu_i \xi_i = 0, \\
    & y_i (\mathbf{x}_i^T\mathbf{w} + b) - (1 - \xi_i) \ge 0,
    \end{aligned}

for :math:`i = 1 \ldots m`. Together these equations uniquely characterize the
solution to the primal and the dual problem.

Let us look at some special properties of the solution. We can see that the
solution for :math:`\mathbf{w}` has the for

.. math::
    \mathbf{\hat{w}} = \sum_{i=1}^{m} \hat{\alpha_i} y_i \mathbf{x_i}

with nonzero coefficients :math:`\hat{\alpha}_i` only for those `i` for which
:math:`y_i (\mathbf{x}_i^T\mathbf{w} + b) - (1 - \xi_i) = 0`. These `i`
observations are called *"support vectors"*  since :math:`\mathbf{w}` is
represented in terms of them alone. Among these support points, some will lie
on the edge of the margin :math:`(\hat{\xi}_i = 0)`, and hence characterized by
:math:`0 < \hat{\alpha}_i < C`; the remainder :math:`(\hat{\xi}_i > 0)` have
:math:`\hat{\alpha}_i = C`. Any of these margin points can be used to solve for
`b`. Typically, once can use an average value from all of the solutions from
the support points.

In this formulation, `C` is model hyper parameter and can be used as a
regularizer to control the capacity and generalization error of the model.

The Kernel Trick
----------------

The support vector classifier described so far finds linear boundaries in the
input feature space. As with other linear methods, we can make the procedure
more flexible by enlarging the feature space using basis expansions such as
polynomials or splines. Generally linear boundaries in the enlarged space
achieve better training-class separation, and translate to nonlinear boundaries
in the original space. Once the basis functions :math:`h_i(x), i=1 \ldots m`
are selected, the procedure remains same as before.

Now recall that in calculating the actual classifier, we needed only support
vector points, i.e. we need smaller amount of computation if data has better
training-class separation. Furthermore, if one looks closely, we can find an
additional trick. The separating plane can be given by the function:

.. math::
    \begin{aligned}
    f(x) & = \mathbf{x}^T \mathbf{w} + b \\
         & = \mathbf{x}^T \sum_{i=1}^{m} \hat{\alpha_i} y_i \mathbf{x_i} + b\\
         & = \sum_{i=1}^{m} \hat{\alpha_i} y_i \mathbf{x}^T \mathbf{x}_i + b\\
         & = \sum_{i=1}^{m} \hat{\alpha_i} y_i \langle\mathbf{x} \mathbf{x}_i\rangle + b
    \end{aligned}

where, :math:`\langle \mathbf{x} \mathbf{y} \rangle` denotes inner product of
vectors :math:`\mathbf{x}` and :math:`\mathbf{y}`. This shows us that we can
rewrite training phase operations completely in terms of inner products!

If we were to replace linear terms with a predefined non-linear operation
:math:`h(x)`, the above formulation of the separating plane will simply modify
into:

.. math::
    \begin{aligned}
    f(x) & = h(\mathbf{x})^T \mathbf{w} + b \\
         & = h(\mathbf{x})^T \sum_{i=1}^{m} \hat{\alpha_i} y_i h(\mathbf{x}_i) + b\\
         & = \sum_{i=1}^{m} \hat{\alpha_i} y_i h(\mathbf{x})^T h(\mathbf{x}_i) + b\\
         & = \sum_{i=1}^{m} \hat{\alpha_i} y_i \langle h(\mathbf{x}) h(\mathbf{x}_i) \rangle + b
    \end{aligned}

As before, given :math:`\hat{\alpha_i}`, `b` can be determined by solving
:math:`y_i f(\mathbf{x}_i) = 1` for any (or all) :math:`x_i` for which
:math:`0 < \hat{\alpha}_i < C`.
More importantly, this tells us that we do not need to
specify the exact nonlinear transformation :math:`h(x)` at all, rather only the
knowledge of the Kernel function :math:`K(x, x') = \langle h(x)h(x') \rangle`
that computes inner products in the transformed space is enough.
**Note that for the dual problem to be convex quadratic programming problem,
`K` would need to be symmetric positive semi-definite.**

Some common choices of kernels are:

:math:`d^{th}` degree polynomial:
:math:`K(x, x') = (1+\langle x x' \rangle )^d`

Radial basis:
:math:`K(x, x') = \exp (-\gamma  \lVert \mathbf{x - x'} \rVert^2 )`

Neural network:
:math:`K(x, x') = \tanh (\kappa_1 \langle x x' \rangle + \kappa_2)`

The role of the hyper-parameter `C` is clearer in an enlarged feature
space, since perfect separation is often achievable there. A large value of C
will discourage any positive :math:`\xi_i`, and lead to an over-fit wiggly
boundary in the original feature space; a small value of `C` will encourage a
small value of :math:`\lVert w \rVert`, which in turn causes :math:`f(x)` and
hence the boundary to be smoother, potentially at the cost of more points as
support vectors.


Curse of Dimensionality.... huh!!!
---------------------------------------

With `m` training examples, `p` predictors and `M` support vectors, the SVM
requires :math:`M^3 + Mm + mpM` operations. This suggests the choice of the
kernel and hence number of support vectors `M` will play a big role in
feasibility of this method. For a really good choice of kernel that leads to
very high training-class separation, i.e. :math:`M <<< m`, the method can be
viewed as linear in `m`. However, for a bad choice case, :math:`M \approx m`
we will be looking at an :math:`O (m^3)` algorithm.

The modern incarnation of deep learning was designed to overcome these
limitations (large order of computations and clever problem-specific choice of
kernels) of kernel machines. We will look at the details of a generic deep
learning algorithm in a future post.
