---
title: "Understanding Linear Regression with Examples"
date: 2018-11-28T21:09:21-07:00
tags:
    - "Machine Learning"
    - "Data Science"
    - Python
categories:
    - "Machine Learning"
slug: "linear-regression"
link:
authors:
    - "Sadanand Singh"
hasMath: true
notebook: false
draft: true
disqus_identifier: "linear-regression.sadanand"
description:
---

Modeling the relationship between a scalar response (or dependent variable)
and one or more explanatory variables (or independent variables) is commonly
referred as a **regression** problem. The simplest model of such a
relationship can be described by a linear function - referred
as _linear regression_.

<!--more-->

<!--TOC-->

# Mathematical formulations

Linear Regression represents a linear relationship between the input
variables ($X$) and single output variable($y$). When the input ($X$) is a
single variable, this model is called **Simple Linear Regression** and when
there are multiple input variables ($X$), it is called
**Multiple Linear Regression**. Mathematically, a simple linear regression
model can be represented as,

{{< tex display="y_i \approx b + w x_i" >}}

For $n$ data points, we can write these equations in matrix form as,

{{< tex display="\begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix} \approx \begin{bmatrix} x_1 & 1 \\ x_2 & 1\\ \vdots & \vdots \\ x_n & 1 \end{bmatrix} \begin{bmatrix} w \\ b \end{bmatrix}" >}}

For the general case of multi-dimensional input variable, $X \equiv$
{{< tex "x_{i1}, x_{i2}, \ldots x_{im}" >}},
we can write the above matrix equation as,

{{< tex display="\begin{bmatrix} y_1 \\ y_2 \\ \vdots \\ y_n \end{bmatrix} \approx \begin{bmatrix} x_{11} & x_{12} & \ldots & x_{1m} & 1 \\ x_{21} & x_{22} & \ldots & x_{2m} & 1\\ \vdots & \vdots & \ldots & \vdots \\ x_{n1} & x_{n2} & \ldots & x_{nm} & 1 \end{bmatrix} \begin{bmatrix} w_1 \\ w_2 \\ \vdots \\ w_m \\ b \end{bmatrix}" >}}

In matrix notation, this can be written as,
$$y \approx \mathbf{X}w$$

In terms of a regression problem, given the data $\mathbf{X}$ and the
true response $y$, we want to estimate the weights vector $w$, such
that the predicted response $\hat{y} = \mathbf{X}w$
is _as close as possible to_ $y$.

The most common way to define and get the closeness of the predicted
response $\hat{y}$ and the true response $y$ is using the
**residual sum of squares (RSS)**.

{{< tex display="RSS = \sum_{i=1}^N \big ( y_i - \hat{y}_i \big)^2 = (y - \mathbf{X}w)^T (y - \mathbf{X}w)" >}}

where $N$ is the total number of samples.
Using some linear algebra and calculus, we can show that, in the matrix form,
the solution to the weights vector $w$ can be given by,

{{< tex display="w = \big(\mathbf{X}^T\mathbf{X}\big)^{-1} \mathbf{X}^T y" >}}

This approach of estimating weights for linear regression is called **Ordinary Least Squares** ([OLS]).

[OLS]: https://en.wikipedia.org/wiki/Ordinary_least_squares

# Key Metrics

# Key Assumptions

# Regularization: Ridge and Lasso Regression

## A Bayesian Perspective

# Generalization of Linear Regression

# Preparing data for linear regression
