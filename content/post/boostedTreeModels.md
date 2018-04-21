---
title: "Understanding Boosted Trees Models"
date: 2017-08-31T21:30:00-07:00
tags:
    - "Machine Learning"
    - "Algorithms"
    - "Python"
categories:
    - "Machine Learning"
slug: "boostedtrees"
link:
authors:
    - "Sadanand Singh"
hasMath: true
notebook: true
draft: false
disqus_identifier: "boostedtrees.sadanand"
readingTime: 30
description:
---

In the [previous post]({{< relref "treemodels.md">}}), we learned about tree based learning methods - basics of tree based models and the use of [bagging]({{< relref "treemodels.md#bootstrap-aggregating-bagging">}}) to reduce variance. We also looked at one of the most famous learning algorithms based on the idea of bagging- [random forests]({{< relref "treemodels.md#random-forest-models">}}). In this post, we will look into the details of yet another type of tree-based learning algorithms: [boosted trees](http://machinelearningmastery.com/gentle-introduction-gradient-boosting-algorithm-machine-learning/).
<!--more-->

<!--TOC-->

# Boosting

Boosting, similar to [Bagging]({{< relref "treemodels.md#bootstrap-aggregating-bagging">}}), is a general class of learning algorithm where a set of weak learners are combined to get strong learners.
{{< marker "warning" >}}
For classification problems, a __weak learner__ is defined to be a classifier which is only slightly correlated with the true classification (it can label examples better than random guessing). In contrast, a __strong learner__ is a classifier that is arbitrarily well-correlated with the true classification.
{{< /marker >}}

Recall that bagging involves creating multiple copies of the original training data set via bootstrapping, fitting a separate decision tree to each copy, and then combining all of the trees in order to create a single predictive model. Notably, each tree is built on a bootstrap data set, independent of the other trees.

In contrast, in Boosting, the trees are grown sequentially: __each tree is grown using information from previously grown trees.__ Boosting does not involve bootstrap sampling; instead each tree is fit on a modified version of the original data set.

Unlike fitting a single large decision
tree to the data, which amounts to _fitting the data hard_ and potentially __overfitting__, the boosting approach instead learns slowly. Given the current model, a decision tree is fit to the residuals from the model. That is, a tree is fit using the current residuals, rather than the outcome as the response.

The above concept of additively fitting weak learners to get a strong learner is not limited to tree based methods. In fact, we can choose these weak learners to be any model of our choice. In practice, however, decision trees or sometimes linear models are the most common choices.
In this post, we will be focusing mainly on boosted trees - i.e. our choice of weak learners would be decision trees. Boosted trees are one of the [most used models](https://www.kaggle.com/wiki/Algorithms) in on-line machine learning competitions like
[Kaggle](https://www.kaggle.com).

Let us consider the case of boosted trees more rigorously. In particular, we will look at the case of boosted decision trees for regression problems. To begin, set the resultant model $\hat{F}(x) = 0$ and residual of the training response as the training target $y$.
Now __Sequentially__, for steps $b=1,2\ldots,B$ update $\hat{F}(x)$ as follows: $\hat{F}(x)\leftarrow \hat{F}(x) + \lambda\_b \hat{f}^{b}(x)$, where $\hat{f}^{b}(x)$ is a decision tree learner fit on $(X, r)$ with $d$ splits (or $d+1$ terminal nodes) and $\lambda\_b$ is a weighting parameter. Also update residuals, $r$ as,
$r \leftarrow r - \lambda\_b \hat{f}^{b}(x)$. At the end of $B$ steps, we will get the final model as $\hat{F}(x) = \sum\_{b=1}^{B}\lambda\_b\hat{f}^{b}(x)$.

The above algorithm of boosted is quite generic. One can come with several strategies for how the decision trees are grown and fit on residuals, and for the choice of the weighting parameter $\lambda$. Therefore, there are various boosting methods. Some common examples are:

- [**Ada**ptive **Boost**ing (AdaBoost)](https://en.wikipedia.org/wiki/AdaBoost)
- [BrownBoost](https://en.wikipedia.org/wiki/BrownBoost)
- [Gentle Boost](https://en.wikipedia.org/wiki/AdaBoost#Gentle_AdaBoost)
- [LP Boost](https://en.wikipedia.org/wiki/LPBoost)
- [Gradient Boosting](https://en.wikipedia.org/wiki/Gradient_boosting)

In this post, we will focus specifically on two of the most common boosting algorithms, AdaBoost and Gradient Boosting.

# Adaptive Boosting (AdaBoost)

**Ada**ptive **Boost**ing or AdaBoost refers to a particular formulation of boosting where the idea of residual learning is implemented through the concept of sample weights. In particular, at any iteration, $b$, all training samples have a weight $w\_i^b$ $\forall i = 1, \ldots N$, which is equal to the current error $E(\hat{f}(x\_i))$. The decision tree $\hat{f}^{b}(x)$ is fit to minimize the error $E\_b = \sum\_{i=1}^{N}{E\big(\hat{F}(x) + \lambda\_b \hat{f}^{b}(x)\big)}$. AdaBoost uses an exponential error/loss function: $E(\hat{F}(x\_i)) = e^{-y\_i \hat{F}(x\_i)}$. The choice of the error function, $E()$, also determines the way weights $w\_i^b$ and the weighting parameter $\lambda\_b$ are updated at different steps.
A neat mathematical derivation of these quantities for the case of binary classification can be found at the [Wiki article](https://en.wikipedia.org/wiki/AdaBoost#Example_algorithm_.28Discrete_AdaBoost.29).

In particular case of the classification problems, we can also think of AdaBoost to be an algorithm where at any step, the misclassified samples get a higher weight than the correctly classified samples. The weights attached to samples are used to inform the training of the weak learner, in this case, decision trees to be grown in a way that favor splitting the sets of samples with high weights.

In practice, the above definition of the AdaBoost model is modified to include a learning rate term, $\gamma$, as a regularization term that shrinks the contribution of all of the models. In particular, the model is updated as, $\hat{F}(x) \leftarrow \hat{F}(x) + \gamma \lambda\_b \hat{f}^{b}(x)$. The main tuning parameters of AdaBosst are, the **learning rate $\gamma$**, **number of estimators $B$**, and decision tree related parameters like **depth of trees $d$**, and **number of samples per split** etc.

<br>
{{< panel primary "AdaBoost in Python" >}}
The python scikit-learn library implementations of AdaBoost ([AdaBoostClassifier](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html) and [AdaBoostRegressor](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostRegressor.html)) are based on a modified version of the AdaBoost algorithms, [AdaBoost SAMME and SAMME.R](https://web.stanford.edu/~hastie/Papers/samme.pdf). Stage-wise Additive Modeling using a Multi-class Exponential loss function (SAMME) algorithm provides an extension of AdaBoost for the case of multi-class classification. The SAMME.R (R for _real_) variation of the algorithm is for prediction of weighted probabilities rather than the class itself.
{{< /panel >}}

## AdaBoost Classifier in Python

Recall the [US income data](https://www.kaggle.com/johnolafenwa/us-census-data) that we used in the [previous based post on tree based methods]({{< relref "treemodels.md">}}). In summary, in this dataset, we are required to predict the income range of adults (<=50K or >50K) based on following features: `Race`, `Sex`, `Education`, `Work Class`, `Capital Loss`, `Capital Gain`, `Relationship`, `Marital Status`, `Age Group`, `Occupation` and `Hours of Work per Week`. We have already seen that, with the best decision tree model, we were able to achieve a prediction accuracy of 85.9%. With the use of random forest models, we were able to increase the accuracy to 86.6%.

Let us try to solve the same problem using [AdaBoost classifier from scikit-learn module](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html). Please have a look at the [previous post on tree-based methods]({{< relref "treemodels.md">}}) to understand the EDA and preparation of the data.

{{< highlight python "linenos=table" >}}
from sklearn.ensemble import AdaBoostClassifier
aclf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=5), n_estimators=100)
aclf.fit(x_train, y_train)
aclf.score(x_test, y_test)
{{< /highlight >}}
Without any parameter tuning, we see an accuracy of 85.54%!

<br>
{{< card success "Genetic Algorithm for Parameter Search" >}}
Once the number of hyper-parameters and the range of those parameter in models becomes large, the time required to find the best parameters becomes exponentially large using simple grid search.
Instead of trying out every possible combination of parameters, we can evolve only the combinations that give the best results using [Genetic Algorithms](https://www.analyticsvidhya.com/blog/2017/07/introduction-to-genetic-algorithm/). A scikit-learn friendly implementation of this can be found in the [sklearn-deap](https://github.com/rsteca/sklearn-deap) library. In many of the examples below we will be using this library to search for best model parameters.

The genetic algorithm itself has three main parameters: `population size`, `tournament size` and `no. of generations`. Typically, for the problem of parameter search, we can use a population of 10-15 per hyper-parameter. The tournament size parameter affects the diversity of population being considered in future generation. This roughly translates into global vs local optimization for parameter search. In other words, if the tournament size is too large, we will have higher chance of getting a solution that is from local minima. A typical value of 0.1 times the population works well for the exercise of finding optimal model parameters. The number of generation decides the convergence of genetic algorithms. A larger value leads to better convergence but requires larger computation time.
{{< /card >}}

Let us try using genetic algorithm to find optimal model parameters for AdaBoost classifier.

{{< highlight python "linenos=table" >}}
from evolutionary_search import EvolutionaryAlgorithmSearchCV

parameters = {
     'base_estimator__max_features':(11, 9, 6),
     'base_estimator__max_depth':(1, 2, 4, 8),
     'base_estimator__min_samples_split': (2, 4, 8),
     'base_estimator__min_samples_leaf': (16, 12, 8, 4),
     'n_estimators': (50, 100, 200, 500),
     'learning_rate': (1, 0.1, 0.01, 10)
}

clf2 = EvolutionaryAlgorithmSearchCV(estimator=aclf,
                                   params=parameters,
                                   scoring="accuracy",
                                   cv=5,
                                   verbose=1,
                                   population_size=200,
                                   gene_mutation_prob=0.10,
                                   gene_crossover_prob=0.5,
                                   tournament_size=10,
                                   generations_number=100,
                                   n_jobs=8)
clf2.fit(x_train, y_train)
{{< /highlight >}}

This should take about **50 minutes** on a reasonable desktop machine!
We can now use the best parameters from this and create a new AdaBoost classifier.

{{< highlight python "linenos=table" >}}
aclf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=4, max_features=11, min_samples_leaf=4, min_samples_split=2),
                         n_estimators=100, learning_rate=0.1)
aclf.fit(x_train, y_train)
aclf.score(x_test, y_test)
{{< /highlight >}}

We see a significant improvement in our results with an accuracy of 87.06% on the testing data!

Given our data is highly imbalanced, let us look at the confusion matrix of our model on the test data. Note that we are using the `confusion_matrix()` method from the [previous post on tree based methods]({{< relref "treemodels.md">}}).

{{< highlight python "linenos=table" >}}
y_pred = aclf.predict(x_test)
cfm = confusion_matrix(y_test, y_pred, labels=[0, 1])
plt.figure(figsize=(10,6))
plot_confusion_matrix(cfm, classes=["<=50K", ">50K"], normalize=True)
{{< /highlight >}}

{{< png >}}
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
4v8DUHbqmZEIpC4AAAAASUVORK5CYII=
{{< /png >}}

We find that our model has a much better predictive power (94.1%) for the dominant class (<=50K), while it has prediction rate of only 64.2% for the other class.

# Gradient Boosting

The approach used in the case of AdaBoost can be also viewed as an [exponential loss minimization approach](https://en.wikipedia.org/wiki/AdaBoost#Boosting_as_gradient_descent). Let us look at this mathematically for the case of a generic loss function, $L\big(y,\hat{F}(x)\big)$. The goal of the method is to find an $\hat{F}(x)$ that minimizes the average value of the loss function $L\big(y,\hat{F}(x)\big)$ on the training set. This can be achieved by starting with a constant function $\hat{F\_0}(x)$, and incrementally expanding it in a greedy fashion as follows:
{{< tex display="\begin{aligned} & \hat{F_0}(x) = \mathop{\arg\min}\limits_{\gamma} \sum_{i=1}^{N} L\big(y,\gamma \big) \\ & \hat{F_b}(x) = \hat{F}_{b-1}(x) + \mathop{\arg\min}\limits_{f \in \mathcal{H}} \sum_{i=1}^{N} L\big(y,\hat{F}_{b-1}(x) + f(x) \big) \text{, for } b=1,2,\ldots, B \end{aligned}" >}}

where $f(x) \in \mathcal{H}$ refers to base learners, in this case tree models. The problem with this set up is that, it is computationally infeasible to choose optimal $f(x)$ at every step for an arbitrary loss function $L\big(y,\hat{F}(x)\big)$.

However, this can be simplified using a [steepest descent](https://en.wikipedia.org/wiki/Steepest_descent) approach. In this approach, at any step the decision tree model is trained on the pseudo-residuals, rather than residuals. The approach can be described in the following algorithm:

- Initialize model as,
{{< tex display="\hat{F_0}(x) = \mathop{\arg\min}\limits_{\gamma} \sum_{i=1}^{N} L\big(y,\gamma \big)" >}}
- for steps $b=1,2,\ldots, B$:
    - compute pseudo-residuals as:
    {{< tex display="r_{ib} = -\Bigg[ \frac{\partial{L\big(y_i, \hat{F}_{b-1}(x_i)\big)}}{\partial{\hat{F}_{b-1}(x_i)}} \Bigg]" >}}
    - Fit a decision tree $\hat{f^b}(x)$ to pseudo-residuals, i.e. train it using the training set $(x\_i, r\_{ib})\_{i=1}^N$
    - Compute multiplier $\gamma\_b$ using [line search](https://en.wikipedia.org/wiki/Line_search), where $0<\nu<1$ is the learning rate parameter
    {{< tex display="\gamma_b = \mathop{\arg\min}\limits_{\gamma} \sum_{i=1}^N L\big(y_i, \hat{F}_{b-1}(x) + \nu \gamma \hat{f^b}(x)\big)" >}}
    - update the model
    {{< tex display="\hat{F_b}(x) = \hat{F}_{b-1}(x) + \nu \gamma_b \hat{f^b}(x)" >}}

In  most real implementations of gradient boosted trees, rather than an individual tree weighing parameter $\gamma\_b$, different parameters are used at different splits, $\gamma\_{jb}$. If you recall from the [last post]({{< relref "treemodels.md" >}}), a decision tree model corresponds to diving the feature space in multiple rectangular regions and hence it can be represented as,

{{< tex display="\hat{f^b}(x) = \sum_{j=1}^{J} k_{jb} I\big(x\in R_{jb}\big)" >}}

where, $J$ is the number of terminal nodes (leaves), $I\big(x\in R\_{jb}\big)$ is an indicator function which is 1 if $x\in R\_{jb}$ and $k\_{jb}$ is the prediction in $j^{th}$ leaf.
Now, we can replace $\hat{f^b}(x)$ in above algorithm and replace $\gamma\_b$ for the whole tree by $\gamma\_{jb}$ per terminal node (leaf).

{{< tex display="\hat{F_b}(x) = \hat{F}_{b-1}(x) + \nu \sum_{j=1}^{J_b} \gamma_{jb} I\big(x\in R_{jb}\big)" >}}

where $\gamma\_{jb}$ is given by the following line search,
{{< tex display="\gamma_{jb} = \mathop{\arg\min}\limits_{\gamma} \sum_{x_i \in R_{jb}} L\big(y_i, \hat{F}_{b-1}(x) + \gamma \big)" >}}

Here $J$ refers to the number of terminal nodes (leaves) in any of constituent decision trees. A value of $J\_b =2$, i.e. **decision stumps** means no interactions among feature variables are considered. With a value of $J\_b=3$ the model may include effects of the interaction between up to two variables, and so on. Typically 
a value of $4 \le J\_b \le 8$ [work well for boosting](https://web.stanford.edu/~hastie/Papers/ESLII.pdf).

<br>
{{< panel "primary" "Regularization of Gradient Boosted Trees" >}}
Gradient Boosted Trees can be regularized by multiple approaches. Some common approaches are:

- **Shrinkage / Learning Rate:** For each gradient step, the step magnitude is multiplied by a factor between 0 and 1 called a learning rate ($0 <\nu < 1$). In other words, each gradient step is shrunken by some factor $\nu$. The rational for this to work as a regularization parameter has never been clear to me. My personal take is the shrinkage enables us to use a different prior. [Telgarsky et al.](https://arxiv.org/pdf/1303.4172.pdf) provide a mathematical proof that shrinkage makes gradient boosting to produce an approximate maximum margin classifier, i.e. a classifier which is able to maximize the associated distance from the decision boundary for each example.
- **Sub-Sampling:** Motivated by the bagging method, at each iteration of the algorithm, a decision tree is fit on a subsample of the training set drawn at random without replacement. Also, like in bagging, sub-sampling allows one to define an [out-of-bag error](https://en.wikipedia.org/wiki/Out-of-bag_error) of the prediction performance improvement by evaluating predictions on those observations which were not used in the building of the next base learner. Out-of-bag estimates help avoid the need for an independent validation dataset, but often underestimate actual performance improvement and the optimal number of iterations.
- **Minimum sample size for splitting trees**, and **Minimum sample size for tree leaves:** It is used in the tree building process by ignoring any splits that lead to nodes containing fewer than this number of training set instances. Imposing this limit helps to reduce variance in predictions at leaves.
- **The number of trees or Boosting Iterations, $B$** Increasing $B$ reduces the error on training set, but setting it too high may lead to over-fitting. An optimal value of $B$ is often selected by monitoring prediction error on a separate validation data set.
- **Sampling Features:** We can apply the idea of randomly choosing small subsets of features for different trees, as in the case of Random Forest models.

{{< /card >}}

## scikit-learn Implementation

[scikit-learn](http://scikit-learn.org/stable/modules/generated/sklearn.ensemble.GradientBoostingClassifier.html) provides a simple and generic implementation of the above described algorithm that is valid of different types of loss functions. Below is a simple implementation for the case of income data.

{{< highlight python "linenos=table" >}}
from sklearn.ensemble import GradientBoostingClassifier

params = {'n_estimators': 200, 'max_depth': 4, 'subsample': 0.75,
          'learning_rate': 0.1, 'min_samples_leaf': 4, 'random_state': 3}
gclf = GradientBoostingClassifier(**params)

gclf.fit(x_train, y_train)
gclf.score(x_test, y_test)
{{< /highlight >}}

Turns out we have got a quite good model just by chance! This has an accuracy of 87.11% on our test data!

We could try finding optimal parameters for this as before. However, in my experience this is a very academic implementation of boosted trees. Other implementation like [XGBoost](https://github.com/dmlc/xgboost), [LightGBM](http://lightgbm.readthedocs.io/en/latest/) and [CatBoost](https://github.com/catboost/catboost) are more optimized implementations and hence we will focus our tuning for some of these libraries only.

## XGBoost

The biggest drawback of the gradient boosting trees is that the algorithm is quite sequential in nature and hence are very slow and they can not take advantage of advanced computing features for parallelization like multiple threads and cores, GPU etc.

[XGBoost](https://github.com/dmlc/xgboost) is a python (C++ and R as well) library that provides an optimized implementation of gradient boosted trees. It uses various tricks like regularization of number of leaves and leaf weights, sparsity aware split finding, column block for parallel learning and cache-aware access. Using these tricks the implementation provides a parallelized efficient version of the algorithm. The details of these can be found [here](https://arxiv.org/pdf/1603.02754.pdf). XGBoost is one of the most famous machine learning libraries used in on-line machine learning competitions like Kaggle.

<br>
{{< panel primary "**XGBoost**: Additional Remarks">}}
**Regularization**: Apart from regular gradient boosted trees, XGBoost provides two additional types of regularization, by adding $L\_1$ constraints on number of leaves ($J\_b$) and $L\_2$ constraints on the leaf weights ($\gamma\_{jb}$) to the loss function. Mathematically, The loss function is modified as follows:
{{< tex display="\text{Loss Term at step b}= \sum_{i=1}^{N} L\big( y_i, \hat{F_b}(x_i) \big) + \sum\_{k=1}^b \Big (\eta J_k + \frac{1}{2} \lambda \left\lVert \gamma\_{jk} \right\rVert^2 \Big )" >}}
Here, the second term in the loss function, penalizes the complexity of the model, i.e. decision tree functions.

**Additional Weak Learners**: Apart from decision trees, XGBoost also supports [linear models](https://en.wikipedia.org/wiki/Linear_model) and [DART (decision trees with dropout)](http://proceedings.mlr.press/v38/korlakaivinayak15.pdf) as weak learners. In the DART algorithm, only a subset of available trees are considered in calculating the pseudo-residuals on which the new trees are fit.
{{< /panel >}}

XGBoost has many parameters that control the fitting of the model. Below are some of the relevant parameters and tuning them would be helpful in the most common cases. _Please note that original XGBoost library parameters might have a different name than before, since I am using the scikit-learn API parameter names below._

1. **max_depth (default=3)** : Maximum depth of a tree, increase this value will make the model more complex / likely to be over-fitting. A  value of 0 indicates no limit. _A Typical Value in the range of 2-10 can be used for model optimization_.
> 2. **n_estimators (default=100)** : The number of boosting steps to perform. This can also be seen as number of trees to be used in the boosted model. This number is inversely proportional to the learning_rate (eta) parameter, i.e. if we use a smaller value of learning_rate, n_estimators has be made larger. _A Typical Value in the range of $\ge 100$ can be used for model optimization. However, it is best to used XGBoost built-in `cv()` method to find this parameter (See the example ahead)_.
3. **min_child_weight (default=1)** : The minimum sum of instance weight needed in a child node. If the tree partition step results in a leaf node with the sum of instance weight less than the min_child_weight, then any further partitioning will be stopped. The larger the value of this parameter, the more conservative the algorithm will be. _A Typical Value in the range of 1-10 can be used for model optimization_.
4. **learning_rate (default=0.1)** : The step size shrinkage used  to prevent over-fitting. After each boosting step, we can directly get the weights of new features. and the learning_rate parameter (also referred as **eta** in regular XGBoost API) shrinks the feature weights to make the boosting process more conservative (See above formulation of Gradient Boosted Trees for mathematical details). _A Typical Value in the range of 0.001-0.3 can be used for model optimization_.
5. **gamma (default=0)** : (Also referred as **min_split_loss** in regular XGBoost API) The minimum loss reduction required to make a further partition on a leaf node of the tree. The larger, the more conservative the algorithm will be. _The value of this parameter depends on the type of loss function being used. A Typical Value in the range of 0.0-0.7 can be used for model optimization_.
6. **reg_alpha (default=0)** : (Also referred as **alpha** in regular XGBoost API) L1 regularization term on weights, increasing this value will make model more conservative (see [XGBoost paper](https://arxiv.org/pdf/1603.02754.pdf) for mathematical details). _A Typical Value in the range of 0-1 can be used for model optimization_.
7. **reg_lambda (default=1)** : (Also referred as **lambda** in regular XGBoost API) L2 regularization term on weights, increasing this value will make model more conservative (see [XGBoost paper](https://arxiv.org/pdf/1603.02754.pdf) for mathematical details). _A Typical Value in the range of 0-1 can be used for model optimization_.
8. **subsample (default=1)** : Subsample ratio of the training instance. Setting it to 0.5 means that XGBoost randomly collected half of the data instances to grow trees. This parameter is used to prevent over-fitting. _A Typical Value in the range of 0.5-1.0 can be used for model optimization_.
9. **colsample_bytree (default=1)** : Subsample ratio of columns when constructing each tree. Similar to Random Forest models, models tend to be more generalizable, if a number between 0 and 1 is used. _A Typical Value in the range of 0.5-1.0 can be used for model optimization_.
10. **scale_pos_weight (default=1)** : Controls the balance of positive and negative class weights, useful for unbalanced class problems. _A typical value to consider: sum(negative cases) / sum(positive cases)_.

Apart from above set of parameters, there are several parameters that should also be considered while tuning. Some examples of such parameters are: **objective** (objective function/ loss function to use, depends on problem, for eg. binary vs. multi-class classification), **tree_method** (The tree construction algorithm used in XGBoost(see description in the [paper](https://arxiv.org/pdf/1603.02754.pdf)), **random_state** (seed for random number generator), **n_jobs** (number of threads to use to train the model) and many other parameters related to different types of tree methods used. [This article](https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/) can be used as a good general reference for tuning XGBoost models.

Let us tune XGBoost model for our problem of income prediction. A simple sklearn API implementation can be used as below.

{{< highlight python "linenos=table" >}}
import xgboost as xgb

params = {'n_estimators': 100,
          'max_depth': 6,
          'subsample': 0.75,
          'learning_rate': 0.1,
          'min_samples_split': 2,
          'min_samples_leaf': 8,
          'random_state': 32,
          'objective': 'binary:logistic',
          'n_jobs': 8
         }
xclf = xgb.XGBClassifier(**params)

xclf.fit(x_train, y_train)
xclf.score(x_test, y_test)
{{< /highlight >}}

With this reasonable guess of parameters based on previous models, we already see an accuracy of 86.75%.

Let us try to find the optimal parameters for the XGBoost model. If we simply try to do a brute force grid search, it can be computationally very expensive and unreasonable on a desktop. Here is a sample parameters list that can give us an idea of what such a grid search could look like.

{{< highlight python "linenos=table" >}}
independent_params = {
    'random_state': 32,
    'objective': 'binary:logistic',
    'n_jobs': 8,
}
params = {'n_estimators': (100, 200, 400, 800, 1000),
          'max_depth': (4, 6, 8),
          'subsample': (0.75, 0.8, 0.9, 1.0),
          'learning_rate': (0.1, 0.01, 0.05),
          'colsample_bytree': (0.75, 0.8, 0.9, 1.0),
          'min_child_weight': range(1,6,2),
          'reg_alpha': [i/10.0 for i in range(0,5)],
          'gamma':[i/10.0 for i in range(0,5)],
          'reg_lambda': (1, 0.1, 10)
         }
{{< /highlight >}}

If we try to do a grid search of this with 5-fold cross validation, it will involve a whopping 0.81 million model training calls! And, even this will not be enough, as we will need additional model training steps to fine-tune our parameter search for finer and/or different range of parameters. Clearly, we need a different approach to solve this.

I will take an approach of optimizing different set of parameters in batches. To begin, we will choose a fixed learning rate of 0.1, and n_estimators=200. We will try to find only tree related parameters (i.e. **max_depth**, **gamma**, **subsample** and **colsample_bytree**) using grid search or genetic algorithm.

{{< highlight python "linenos=table" >}}
ind_params = {
    'random_state': 32,
    'objective': 'binary:logistic',
    'n_estimators': 200,
    'learning_rate': 0.1,
}
params = {'max_depth': (4, 6, 8),
          'subsample': (0.75, 0.8, 0.9, 1.0),
          'colsample_bytree': (0.75, 0.8, 0.9, 1.0),
          'gamma': [i/10 for i in range(0,5)]
         }

clf2 = EvolutionaryAlgorithmSearchCV(estimator=xgb.XGBClassifier(**ind_params),
                                   params=params,
                                   scoring="accuracy",
                                   cv=5,
                                   verbose=1,
                                   population_size=60,
                                   gene_mutation_prob=0.10,
                                   gene_crossover_prob=0.5,
                                   tournament_size=5,
                                   generations_number=100,
                                   n_jobs=8)
clf2.fit(x_train, y_train)
{{< /highlight >}}

This gives us the following optimal values for different parameters:

    Best individual is: {'max_depth': 6, 'subsample': 1.0, 'colsample_bytree': 0.8, 'gamma': 0.2}
    with fitness: 0.8710727557507447

We can do a finer grid search to get more precise values. For this exercise, let us move on to the next stage of parameter tuning of XGBoost.

XGBoost provides an optimized version of cross validation using `cv()` method which supports early stopping to give us optimal value of **n_estimators**.

{{< highlight python "linenos=table" >}}
xgb1 = xgb.XGBClassifier(
 learning_rate =0.1,
 n_estimators=10000,
 max_depth=6,
 min_child_weight=1,
 gamma=0.2,
 subsample=1.0,
 colsample_bytree=0.8,
 objective= 'binary:logistic',
 n_jobs=8,
 scale_pos_weight=1,
 random_state=32)
xgb_param = xgb1.get_xgb_params()
xgtrain = xgb.DMatrix(x_train, label=y_train)
cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=xgb1.get_params()['n_estimators'], nfold=5, metrics='auc', early_stopping_rounds=50)

print("Number of Predicted n_estimators = ", cvresult.shape[0])
{{< /highlight >}}

This gives us a value of **n_estimators = 206**. We will now use these parameters to search for the next set of tree building parameters: **max_depth** and **min_child_weight**.

{{< highlight python "linenos=table" >}}
params = {
 'max_depth':range(3,10,2),
 'min_child_weight':range(1,6,2)
}

ind_params = {'learning_rate': 0.1,
 'n_estimators': 206,
 'gamma': 0.2,
 'subsample': 1.0,
 'colsample_bytree': 0.8,
 'objective': 'binary:logistic',
 'random_state': 32}

clf2 = EvolutionaryAlgorithmSearchCV(estimator=xgb.XGBClassifier(**ind_params),
                                   params=params,
                                   scoring="accuracy",
                                   cv=5,
                                   verbose=1,
                                   population_size=30,
                                   gene_mutation_prob=0.10,
                                   gene_crossover_prob=0.5,
                                   tournament_size=5,
                                   generations_number=100,
                                   n_jobs=8)
clf2.fit(x_train, y_train)
{{< /highlight >}}

The optimal set of parameters found by this are:

    Best individual is: {'max_depth': 7, 'min_child_weight': 1}
    with fitness: 0.8712877368631184

We can now use these parameters as fixed values and optimize regularization parameters: **reg_alpha** and **reg_lambda**.

{{< highlight python "linenos=table" >}}
ind_params = {'learning_rate': 0.1,
 'n_estimators': 206,
 'gamma': 0.2,
 'subsample': 1.0,
 'colsample_bytree': 0.8,
 'objective': 'binary:logistic',
 'random_state': 32,
 'max_depth': 7,
 'min_child_weight': 1}

params = {'reg_alpha':[0, 0.001, 0.005, 0.01, 0.05], 'reg_lambda':[0.01, 0.1, 1, 10, 100]}

clf2 = EvolutionaryAlgorithmSearchCV(estimator=xgb.XGBClassifier(**ind_params),
                                   params=params,
                                   scoring="accuracy",
                                   cv=5,
                                   verbose=1,
                                   population_size=30,
                                   gene_mutation_prob=0.10,
                                   gene_crossover_prob=0.5,
                                   tournament_size=3,
                                   generations_number=100,
                                   n_jobs=8)
clf2.fit(x_train, y_train)
{{< /highlight >}}

The optimal set of parameters found by this search are:

    Best individual is: {'reg_alpha': 0.001, 'reg_lambda': 1}
    with fitness: 0.8714720063880101

We can now decrease the learning rate by an order to magnitude to get a more stable model. However, we will also need to find the optimal value of number of estimators again using the `cv()` method.

{{< highlight python "linenos=table" >}}
ind_params = {'learning_rate': 0.01,
 'n_estimators': 5000,
 'gamma': 0.2,
 'reg_alpha': 0.001,
 'reg_lambda': 1,
 'subsample': 1.0,
 'colsample_bytree': 0.8,
 'objective': 'binary:logistic',
 'random_state': 32,
 'max_depth': 7,
 'n_jobs': 8,
 'min_child_weight': 1}

xgb2 = xgb.XGBClassifier(**ind_params)
xgb_param = xgb2.get_xgb_params()
xgtrain = xgb.DMatrix(x_train, label=y_train)
cvresult = xgb.cv(xgb_param, xgtrain, num_boost_round=xgb1.get_params()['n_estimators'], nfold=5, metrics='auc', early_stopping_rounds=50)

print("Number of Predicted n_estimators = ", cvresult.shape[0])
{{< /highlight >}}

We get an optimal value of **n_estimators = 1559**. Let us use now all of these optimized values to make a final XGBoost model.

{{< highlight python "linenos=table" >}}
ind_params = {'learning_rate': 0.01,
 'n_estimators': 1559,
 'gamma': 0.2,
 'reg_alpha': 0.001,
 'reg_lambda': 1.0,
 'subsample': 1.0,
 'colsample_bytree': 0.8,
 'objective': 'binary:logistic',
 'random_state': 32,
 'max_depth': 7,
 'n_jobs': 8,
 'min_child_weight': 1}

xclf = xgb.XGBClassifier(**ind_params)

xclf.fit(x_train, y_train)
xclf.score(x_test, y_test)
{{< /highlight >}}

We get test accuracy of 86.99%. Now, this seems odd. After we did all this computation and we still have got a test accuracy that is smaller than an optimized version of scikit-learn's Gradient Boosting Tree implementation. However, if you have paid attention to the metric, you can notice - for cross validation, I started using 'auc' as metric, instead of 'accuracy'. This will give us better accuracy for the less abundant class (> 50K salary) but at the cost of slight decrease in the accuracy of the more abundant class (<= 50K salary). We can verify this by the following confusion matrix plot.

{{< highlight python "linenos=table" >}}
y_pred = xclf.predict(x_test)
cfm = confusion_matrix(y_test, y_pred, labels=[0, 1])
plt.figure(figsize=(10,6))
plot_confusion_matrix(cfm, classes=["<=50K", ">50K"], normalize=True)
{{< /highlight >}}

{{< png >}}
iVBORw0KGgoAAAANSUhEUgAAAfUAAAG2CAYAAABmhB/TAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAIABJREFUeJzt3Xm8VXW5+PHPw+SIiOIIqKg4oDmiZpaapWKaw80BLXMqs9QGs9/FNDPLTG2yK90uNpgN4nAzMTEsy66aJjgmmog4MCWCiiaKHnh+f+wFrbOBcw6cYbM3n7ev/XKvtb77u74bjzznedZ3fVdkJpIkqf51q/UAJElSxzCoS5LUIAzqkiQ1CIO6JEkNwqAuSVKDMKhLktQgDOpSJ4mINSLi1oiYGxE3tqOfj0bEHR05tlqIiNsj4qRaj0NqZAZ1rfIi4oSImBAR/4qImUXweW8HdH00sBGwfmYes6KdZOavMvOgDhhPMxGxf0RkRNxctX/nYv9dbeznooj4ZWvtMvOQzPz5Cg5XUhsY1LVKi4hzgO8D36QSgDcDfggc0QHdbw5MysymDuirs7wE7B0R65f2nQRM6qgTRIV/10hdwP/RtMqKiD7AxcCZmfmbzHwjM9/JzFsz80tFm9Ui4vsRMaN4fT8iViuO7R8R0yLiixExq8jyTymOfQ24EDiuqACcVp3RRsQWRUbco9g+OSKmRMTrEfFsRHy0tP+e0ufeExHji7L++Ih4T+nYXRHx9Yi4t+jnjojo18Ifw9vAb4Hhxee7A8cBv6r6s7oyIqZGxGsR8WBEvK/YPwz4cul7PloaxyURcS8wD9iy2PeJ4vh/R8T/lvq/LCLujIho839ASUswqGtVtjewOnBzC23OB94N7ALsDOwJXFA6vjHQB+gPnAaMjIi+mflVKtn/9Zm5dmb+pKWBRMRawA+AQzKzN/Ae4JGltFsPuK1ouz7wXeC2qkz7BOAUYEOgF3BuS+cGrgU+Xrw/GHgcmFHVZjyVP4P1gF8DN0bE6pn5+6rvuXPpMycCpwO9geer+vsi8K7iF5b3UfmzOyldt1pqF4O6VmXrA7NbKY9/FLg4M2dl5kvA16gEq0XeKY6/k5ljgX8B267geBYCO0bEGpk5MzMnLqXNocDTmfmLzGzKzOuAfwAfLrX5WWZOysw3gRuoBONlysy/AutFxLZUgvu1S2nzy8ycU5zzO8BqtP49r8nMicVn3qnqbx6VP8fvAr8Ezs7Maa30J6kVBnWtyuYA/RaVv5dhU5pnmc8X+xb3UfVLwTxg7eUdSGa+QaXsfQYwMyJui4jt2jCeRWPqX9r+5wqM5xfAWcD7WUrlIiLOjYgni5L/q1SqEy2V9QGmtnQwM/8GTAGCyi8fktrJoK5V2X3AfODIFtrMoDLhbZHNWLI03VZvAGuWtjcuH8zMcZl5ILAJlez76jaMZ9GYpq/gmBb5BfAZYGyRRS9WlMf/H3As0Dcz1wXmUgnGAMsqmbdYSo+IM6lk/DOK/iW1k0Fdq6zMnEtlMtvIiDgyItaMiJ4RcUhEXF40uw64ICI2KCacXUilXLwiHgH2jYjNikl65y06EBEbRcQRxbX1+VTK+AuX0sdYYJviNrweEXEcMAT43QqOCYDMfBbYj8ocgmq9gSYqM+V7RMSFwDql4y8CWyzPDPeI2Ab4BvAxKmX4/xcRLV4mkNQ6g7pWacX14XOoTH57iUrJ+CwqM8KhEngmAI8BfwceKvatyLn+AFxf9PUgzQNxt2IcM4CXqQTYTy+ljznAYVQmms2hkuEelpmzV2RMVX3fk5lLq0KMA35P5Ta354G3aF5aX7SwzpyIeKi18xSXO34JXJaZj2bm01Rm0P9i0Z0FklZMONlUkqTGYKYuSVKDMKhLktQgDOqSJDUIg7okSQ2ipUU3VgnRY42MXr1rPQypXXbdfrNaD0Fql+eff47Zs2evFGv/d19n88ymN9vdT7750rjMHNYBQ2ozg3qv3qy27bG1HobULvf+7apaD0Fql332GlrrISyWTW92SFx465GRra262OFW+aAuSVJzAXX6tOD6HLUkSVqCmbokSWUBxEpxeX+5GdQlSapWp+V3g7okSdXqNFOvz19FJEnSEszUJUlqpn5nvxvUJUmqZvldkiTVkpm6JEllgeV3SZIaQ1h+lySpYUS39r9aO0XEsIh4KiImR8SIpRzfPCLujIjHIuKuiBjQWp8GdUmSulhEdAdGAocAQ4DjI2JIVbNvA9dm5k7AxcClrfVrUJckqVpE+18t2xOYnJlTMvNtYDRwRFWbIcCfivd/XsrxJRjUJUlqJjqq/N4vIiaUXqeXTtIfmFranlbsK3sU+I/i/VFA74hYv6WRO1FOkqTOMTsz2/Og+HOBqyLiZOD/gOnAgpY+YFCXJKmsa57SNh0YWNoeUOxbLDNnUGTqEbE28JHMfLWlTi2/S5JUrfNnv48HBkfEoIjoBQwHxjQbQkS/iMUdnQf8tLVODeqSJDXTYdfUlykzm4CzgHHAk8ANmTkxIi6OiMOLZvsDT0XEJGAj4JLWRm75XZKkGsjMscDYqn0Xlt7fBNy0PH0a1CVJqtatPleUM6hLklTm2u+SJDUQ136XJEm1ZKYuSVIzYfldkqSGYfldkiTVkpm6JEnVLL9LktQA2vbo1JWSQV2SpGp1mqnX56glSdISzNQlSapm+V2SpEZQv/ep1+eoJUnSEszUJUmqZvldkqQG4FPaJElqFF5TlyRJNWamLklSNa+pS5LUICy/S5KkWjJTlySpmuV3SZIaQNTv7HeDuiRJ1eo0U6/PX0UkSdISzNQlSaoSdZqpG9QlSSoJDOqSJDWGKF51yGvqkiQ1CDN1SZKaCcvvkiQ1inoN6pbfJUmqgYgYFhFPRcTkiBixlOObRcSfI+LhiHgsIj7UWp9m6pIkVensTD0iugMjgQOBacD4iBiTmU+Uml0A3JCZ/x0RQ4CxwBYt9WtQlySpSheU3/cEJmfmlOJ8o4EjgHJQT2Cd4n0fYEZrnRrUJUkq67hb2vpFxITS9qjMHFW87w9MLR2bBuxV9fmLgDsi4mxgLeCDrZ3QoC5JUueYnZlD2/H544FrMvM7EbE38IuI2DEzFy7rAwZ1SZJKomtuaZsODCxtDyj2lZ0GDAPIzPsiYnWgHzBrWZ06+12SpCoR0e5XK8YDgyNiUET0AoYDY6ravAB8oBjP9sDqwEstdWpQlySpi2VmE3AWMA54ksos94kRcXFEHF40+yLwyYh4FLgOODkzs6V+Lb9LklSlKxafycyxVG5TK++7sPT+CWCf5enToC5JUpV6XVHOoC5JUplPaZMkSbVmpi5JUhXL75IkNYAuuk+9UxjUJUmqUq9B3WvqkiQ1CDN1SZKq1WeiblCXJKmZsPwuSZJqzExdkqQq9ZqpG9QlSapiUJckqQHU833qXlOXJKlBmKlLklStPhN1g7okSc14S5skSao1M3VJkqrUa6ZuUJckqYpBXZKkRlGfMd1r6lo+B75nex69+Ss8fstXOfeUA5c4vtkmfRn7o7N54PrzGHf15+i/4bqL9//11//J/aNH8OBN5/OJo9+7+DPHDtud8Td8mQeuP49brvoM66+7Vpd9H62a7hj3e3baYVt22G5rrrj8W0scnz9/Ph874Th22G5r3veevXj+uecWH/v7Y4+x33v3Zredd2DoLu/irbfeYt68eRx1+KHsvON27LbzDlzw5RFd+G2kfzOoq826dQu+P+JYjjjrh+z6kW9wzLDd2W7LjZu1ufQLR/Gr2x5gz+Mu5Zujbufisw8HYOZLr7H/Sd/h3cO/xb4nXsG5pxzIJhv0oXv3blzxpaMZdvqV7HncpTz+9HTOOG6/Wnw9rSIWLFjA5z97JrfcejsPP/YEN46+jiefeKJZm2t++hP6rtuXif+YzNmf+wLnf/k/AWhqauLUkz7Gf438EQ89OpFxd95Fz549Afj8Oefy6OP/4P7xD3PfX+9l3O9v7/Lvpo4TEe1+1YJBXW22x45b8MzU2Tw3fQ7vNC3gxnEPcdj+OzVrs92Wm/CXB54C4C/jJ3HY/u8C4J2mBbz9ThMAq/XqSbfiBz6i8lprjV4A9F57DWa+NLervpJWQeMfeICtttqaQVtuSa9evTjmuOH87tZbmrX53a238NETTwLgPz5yNHf96U4ykz/+4Q52fNdO7LTzzgCsv/76dO/enTXXXJP99n8/AL169WKXXXdj+rRpXfvF1GE6IqAb1LXS23TDPkx78ZXF29NffIX+G/Rp1ubvk6ZzxAG7AHDEATuzztprsF6fSjl9wEbr8sD15/H07V/nO9f8kZkvzaWpaSGf++b1jL/hy0y54xK233JjrvntX7vuS2mVM2PGdAYMGLh4u3//AUyfPn3JNgMrbXr06ME6ffowZ84cnp40iYjgwx86mL332I3vfPvyJfp/9dVXGXvbrbz/gA907hdRpzKod7CI2D8i5kbEI8XrwtKxYRHxVERMjogRpf13RcTQ4v2giHg6Ig6uxfhXVed972bet/vW3Hfdf/K+3bdm+ouvsGDBQgCmvfgqex53KTse8TU+9uE92XC93vTo0Y1PHv0+3n38ZWx50Pk8Pmk6Xzr1oBp/C2npmhY08de/3sPPrv0Vd/7lHsb89mb+/Kc7/328qYmTPnY8nznzswzacssajlSrqi6d/R4RvYCemflGGz9yd2YeVtVHd2AkcCAwDRgfEWMy84lSmwHA74EvZua4jhm9Zsyay4CN+i7e7r9RX6ZXlcpnvjSX4ef+GKiU1I/8wC7M/debS7SZOHkm++y2FS/MeBmAZ6fNBuCmPzzEuacY1NV5Nt20P9OmTV28PX36NPr3779km6lTGTBgAE1NTbw2dy7rr78+/fsP4L3v3Zd+/foBMOyQD/Hwww8tzsrPPON0ttp6MGd/7vNd94XUKer1lrYuydQjYvuI+A7wFLBNO7vbE5icmVMy821gNHBE6fgmwB3A+Zk5pp3nUsmEic+z9WYbsPmm69OzR3eOOXg3brvrsWZt1l93rcX/M3zp1IP5+S33A9B/w3VZfbXKhKJ1e6/Be3bdiknPzWLGS3PZbsuN6dd3bQA+8O7teOrZf3bht9KqZugeezB58tM89+yzvP3229x4/WgOPezwZm0OPexwfvWLnwPwm/+9if3efwARwYEHHczEx//OvHnzaGpq4u7/+wvbbz8EgIsuvIC5r83l29/9fpd/J3WC6IBXDXRaph4RawHHAqcVu34GXJSZrxfHvwe8fykfHZ2Zi+4x2TsiHgVmAOdm5kSgPzC11H4asFdp++fABZl5UwtjOx04HYCeay/nN1t1LViwkC9cdgO3/vBMuncLfn7L/Tw55Z985dOH8tATL3DbX/7OvkMHc/HZh5MJ9zw0mc9fegMA2w7amG+dcxRJEgTfv/ZOJk6eAcA3R93OH378ed5pWsALM1/m9K/+spZfUw2uR48efO/Kq/jwoQezYMECTjr5VIbssAMXX3Qhu+0+lMM+fDgnn3oap558IjtstzV9+67HL341GoC+ffvy2c+fw3v33oOI4OBhH+KQDx3KtGnTuOzSS9h2u+3Ye4/dADjjM2dxymmfqOVX1SooMrNzOo54DXgM+ERm/mMFPr8OsDAz/xURHwKuzMzBEXE0MCwzP1G0OxHYKzPPioi7gFnAAOCDmTmvtfN0W3PDXG3bY5d3eNJK5ZXxV9V6CFK77LPXUB58cMJKUfNebaPB2f+jV7a7n2e/d+iDmTm0A4bUZp1Zfj8amA78JiIujIjNywcj4nulSXDl1wiAzHwtM/9VvB8L9IyIfkWfA0tdDSj2LXI5MB64MSJcMU+StHyifme/d1rQy8w7gDsiYn3gY8AtETGbSub+XGZ+oaXPR8TGwIuZmRGxJ5VfQOYArwKDI2IQlWA+HDih6uOfB34N/CQiTs7OKkdIkhpOUFk/ox51+kS5zJyTmVdm5i7Al4EFbfzo0cDjxTX1HwDDs6IJOAsYBzwJ3FBcay+fM4GTqEyaW/JGUkmSGlCXlqcz84HlaHsVsNQLhUU5fuxS9u9fev824L1RkqTl1DXl84gYBlwJdAd+XJokvuh4eUL5msCGmbluS316zVmSpCqdHdPbsuZK+TJ1RJwN7NpavyvtinKSJDWw1tZcqXY8cF1rnZqpS5JUpYPK7/0iYkJpe1Rmjiret7bmSnksmwODgD+1dkKDuiRJZdFh5ffZHXSf+nDgpsxsdaK5QV2SpJIAunXr9Ilyra25UjYcOLMtnXpNXZKkrjeeYs2V4mFnw4ElnlcSEdsBfYH72tKpmbokSVU6e/Z7ZjZFxKI1V7oDP83MiRFxMTCh9ECy4VSeidKmRdQM6pIkVemK+9SXtuZKZl5YtX3R8vRp+V2SpAZhpi5JUlnHzX7vcgZ1SZJKKg90qc+oblCXJKmZ2j06tb28pi5JUoMwU5ckqUqdJuoGdUmSqtVr+d2gLklSWR3PfveauiRJDcJMXZKkEm9pkySpgdRpTLf8LklSozBTlySpiuV3SZIaRJ3GdIO6JEnNRP1m6l5TlySpQZipS5JUUrmlrdajWDEGdUmSmvEpbZIkqcbM1CVJqlKnibpBXZKkavVafjeoS5JU5lPaJElSrZmpS5JU4lPaJElqIAZ1SZIaRJ3GdK+pS5LUKMzUJUmqYvldkqRG4C1tkiSp1szUJUkqCR/oIklS44ho/6v1c8SwiHgqIiZHxIhltDk2Ip6IiIkR8evW+jRTlySpSrdOztQjojswEjgQmAaMj4gxmflEqc1g4Dxgn8x8JSI2bK1fM3VJkrrensDkzJySmW8Do4Ejqtp8EhiZma8AZOas1jo1qEuSVKWDyu/9ImJC6XV66RT9gaml7WnFvrJtgG0i4t6IuD8ihrU2bsvvkiSVVIJyh5TfZ2fm0HZ8vgcwGNgfGAD8X0S8KzNfXdYHzNQlSep604GBpe0Bxb6yacCYzHwnM58FJlEJ8stkUJckqUq3aP+rFeOBwRExKCJ6AcOBMVVtfkslSyci+lEpx09pqVPL75IkVens+9QzsykizgLGAd2Bn2bmxIi4GJiQmWOKYwdFxBPAAuBLmTmnpX4N6pIkVemKtWcycywwtmrfhaX3CZxTvNrE8rskSQ3CTF2SpJKgslRsPTKoS5JUpQ0T3VZKlt8lSWoQZuqSJJVF/T6lzaAuSVKVOo3pBnVJksqCzn9KW2fxmrokSQ3CTF2SpCp1mqgb1CVJquZEOUmSGkDpeeh1x2vqkiQ1iGVm6hGxTksfzMzXOn44kiTVXr3Ofm+p/D4RSGi2AO6i7QQ268RxSZJUM/UZ0lsI6pk5sCsHIkmS2qdN19QjYnhEfLl4PyAidu/cYUmSVDtRLBXbnlcttBrUI+Iq4P3AicWuecCPOnNQkiTVSmVFufa/aqEtt7S9JzN3i4iHATLz5Yjo1cnjkiSpNur4gS5tKb+/ExHdqEyOIyLWBxZ26qgkSdJya0tQHwn8L7BBRHwNuAe4rFNHJUlSDS1agKY9r1potfyemddGxIPAB4tdx2Tm4507LEmSaqdey+9tXSa2O/AOlRK8q9BJkrQSasvs9/OB64BNgQHAryPivM4emCRJtdDos98/DuyamfMAIuIS4GHg0s4cmCRJtdLI5feZVe16FPskSWpI9RnSW36gy/eoXEN/GZgYEeOK7YOA8V0zPEmS1FYtZeqLZrhPBG4r7b+/84YjSVJtRTTgU9oy8yddORBJklYWdRrTW7+mHhFbAZcAQ4DVF+3PzG06cVySJNVMvU6Ua8s959cAP6Myb+AQ4Abg+k4ckyRJWgFtCeprZuY4gMx8JjMvoBLcJUlqSA27TCwwv3igyzMRcQYwHejducOSJKk2gqjbiXJtydS/AKwFfBbYB/gkcGpnDkqSpEYXEcMi4qmImBwRI5Zy/OSIeCkiHilen2itz7Y80OVvxdvXgROXf9iSJNWRLiifR0R3Kk9BPRCYBoyPiDGZ+URV0+sz86y29tvS4jM3UzxDfWky8z/aepKV2aBBm3D5NefXehhSu+x7+V21HoLULv/45+u1HkIzXTD7fU9gcmZOKc43GjgCqA7qy6WlTP2q9nQsSVK96qDHkfaLiAml7VGZOap43x+YWjo2DdhrKX18JCL2BSYBX8jMqUtps1hLi8/c2bYxS5KkpZidmUPb8flbgesyc35EfAr4OXBASx/w2eiSJJUElfJ7e1+tmA4MLG0PKPYtlplzMnN+sfljYPfWOjWoS5JUpQuepz4eGBwRgyKiFzAcGFNuEBGblDYPB55srdO23Ke+qPPVSr8xSJKkFZSZTRFxFjAO6A78NDMnRsTFwITMHAN8NiIOB5qoPDH15Nb6bcva73sCPwH6AJtFxM7AJzLz7BX+NpIkrcTakGm3W2aOBcZW7buw9P484Lzl6bMt5fcfAIcBc4qTPAq8f3lOIklSvags89rp19Q7RVvK790y8/mqAS7opPFIklRzXZGpd4a2BPWpRQk+ixVwzqZyv5wkSVqJtCWof5pKCX4z4EXgj8U+SZIaUp0+z6VNa7/PojLVXpKkhhdQt09pa8vs96tZyhrwmXl6p4xIkiStkLaU3/9Yer86cBTN16uVJKmh1OvKbG0pv19f3o6IXwD3dNqIJEmqsTqtvrd9RbmSQcBGHT0QSZJWBhHR0NfUX+Hf19S7UVmqbkRnDkqSJC2/FoN6VFac2Zl/PzlmYWYuMWlOkqRGUqeJestBPTMzIsZm5o5dNSBJkmqtkVeUeyQids3Mhzt9NJIk1VhD3qceET0yswnYFRgfEc8Ab1D5vpmZu3XRGCVJUhu0lKk/AOxG5cHskiStMuo0UW8xqAdAZj7TRWORJKn2ojGvqW8QEecs62BmfrcTxiNJklZQS0G9O7A2RcYuSdKqIuo09LUU1Gdm5sVdNhJJklYCldnvtR7Fimn1mrokSauaeg3qLT2I5gNdNgpJktRuy8zUM/PlrhyIJEkri6jTe9pW5CltkiQ1rHq+pl6vz4GXJElVzNQlSSqLxlxRTpKkVVLDPdBFkqRVkdfUJUlSzZmpS5JUpU6r7wZ1SZKaC7rV6aKqBnVJkkqC+s3UvaYuSVINRMSwiHgqIiZHxIgW2n0kIjIihrbWp5m6JEll0fmz3yOiOzASOBCYBoyPiDGZ+URVu97A54C/taVfM3VJkqp0i2j3qxV7ApMzc0pmvg2MBo5YSruvA5cBb7Vp3MvzJSVJUpv1i4gJpdfppWP9gaml7WnFvsUiYjdgYGbe1tYTWn6XJKmkAyfKzc7MVq+DL3UMEd2A7wInL8/nDOqSJFXpgmVipwMDS9sDin2L9AZ2BO4qHgO7MTAmIg7PzAnL6tSgLklSlS64pW08MDgiBlEJ5sOBExYdzMy5QL9/jyfuAs5tKaCD19QlSepymdkEnAWMA54EbsjMiRFxcUQcvqL9mqlLklQSdE3Gm5ljgbFV+y5cRtv929KnQV2SpLKAqNMl5Sy/S5LUIMzUJUmqUp95ukFdkqRmgi65pa1TGNQlSapSnyHda+qSJDUMM3VJkqrUafXdoC5JUnPhLW2SJKm2zNQlSSrpqhXlOoNBXZKkKvVafjeoS5JUpT5Dev1WGCRJUhUzdUmSyur4gS4GdUmSSpwoJ0lSA6nXTL1efxmRJElVzNQlSapSn3m6QV2SpCXUafXd8rskSY3CTF2SpJLK7Pf6TNUN6pIkVanX8rtBXZKkZoKo00zda+qSJDUIM3VJkqpYfpckqQHU80Q5y++SJDUIM3VJksrC8rskSQ3DoC5JUoPwljZJklRTZuqSJJUE0K0+E3UzdUmSqkUH/NPqOSKGRcRTETE5IkYs5fgZEfH3iHgkIu6JiCGt9WlQlySpSkT7Xy33H92BkcAhwBDg+KUE7V9n5rsycxfgcuC7rY3boC5JUtfbE5icmVMy821gNHBEuUFmvlbaXAvI1jr1mrqWy8P3/pmfXf4VFi5cyAeOOp6jTj272fFxN17LuOuvoVu3bqy+5lp86itXMHCrbZg1fSqf/4/92HTzLQEYvNPufOqCywD49X99i7/87kbeeG0uv7xvcpd/J6163r3lenzxwK3pFsEtj87k2vteWKLNB7ffgE+8bwtIeHrWv/jKLU8uPrZWr+6MPn1P/jJpNt++4+nF7U/ZZ3O6R3DP5Dlc9ecpXfV11Ak6aPZ7v4iYUNoelZmjivf9gamlY9OAvZYYR8SZwDlAL+CA1k5oUFebLViwgB9f+mUu/NFo1ttoE0Z89EMM3e9gBm61zeI27zvkKA4+5uMAjL9rHD//zkVc8MNfA7DRgM359g1/XKLfofsdyCHDT+Hsw/fpmi+iVVq3gP938GDOuu5RZr02n5+fsjt3Pz2bZ2fPW9xmYN81OGnvzfjktQ/z+ltN9F2zZ7M+PrXfIB6Z+uri7T5r9OCzB2zFx3/2IK/Oe4evHrYde2yxLuOfexXVnw6cKDc7M4e2p4PMHAmMjIgTgAuAk1pqb/ldbTb58YfZeOAWbDRgc3r27MU+Bx/B+LvGNWuz5tq9F7+f/+a8Nq3gsM1Ou9N3g406fLzS0uyw6TpMe+VNZrz6Fk0LkzuemMW+g/s1a3PkLptw04MzeP2tJgBemffO4mPbbbw2663Vi/unvLJ436brrsHUV97k1aLdA8+9wvu33aALvo3q2HRgYGl7QLFvWUYDR7bWqZm62uzlWf+k38abLt5ef6NNePrvDy3R7vbRP+N3vxxF0ztvc9GoGxfvnzX9Bc497kDWXLs3w8/8T4bstkSlSep0G/RejRdfm794e9br89lh03WatdlsvTUBuPrEXenWLbj67ue4f8rLBPC5D2zNV8c8yR5b9F3cftorb7LZemuySZ/VmfXafPbbph89u9fpPVGii56nPh4YHBGDqATz4cAJzUYRMTgzny42DwWephUrdaYeEddExLPFdP5HImKXYn9ExA+K2wAei4jdiv1bRMTjpc9/MiIejIi+yzqHOt4hw09h5O/u42OfO5+brr4SgL4bbMiPfj+eb1//B0764kVced5nmPev12s8UmnpuncLBq63Bmf86hG+8tsnOP9D27D2aj04evf+/PWZOcx6fX6z9q+/1cRlv5/EJUcOYdSJuzCIMXQqAAARrUlEQVRz7lssXFijwav9OmDme2tFysxsAs4CxgFPAjdk5sSIuDgiDi+anRUREyPiESrX1VssvUONM/WI6JuZr7TS7EuZeVPVvkOAwcVrL+C/qZpgEBEnAmcDB7ThHGqD9TbcmNn/nLF4e86LM1lvw02W2X6fYUdy9TfPA6Bnr9Xo2Ws1ALYashMbDdiCGc9PYesddu7cQUtVXnp9Phuts9ri7Q17r8ZLVUF61uvzeXzGayxYmMyY+xYvvPwmA9dbg3f1X4ddBvbhI7v1Z81e3enRPXjz7QWMvGsK90yewz2T5wCV8v3Cha1OVNZKrCvqLJk5Fhhbte/C0vvPLW+ftc7UJ0TEryLigIjlWj7/CODarLgfWDciFkeXiDgWGAEclJmzO3jMq6ytd9iFmS88y4vTX+Cdd97m3nG3sMd+BzVrM/P5f8/4fejuP7LxZoMAmPvyHBYsWADAi9Oe558vPMtGAzbrusFLhSdmvM7AvmuwaZ/V6dEtOGjIhtz9dPO/Ju6aNJvdN1sXgD5r9GSz9dZgxqtvcuGYJzl85P0c+cP7ufLOZxj79xcZeVflZ37RZLreq1cy+lsendm1X0yi9tfUt6GSdZ9FZXbfL4BrMnNGqc0lEXEhcCcwIjPns/RbAfoDs4HNgauAXTPzn13wHVYZ3Xv04BMjLuEbnz6BhQsXcMARwxm49baM/uHlbDVkZ/bY/2BuH/0zHvvb3fTo0YO11lmXsy+ulN+ffOh+Rv/wCnr06EF068bpF3yL3n0qV0V+8b2vc/ftv2X+W29y+kG784Gjjue4T59by6+qBrYgkyvueJofDN+Jbt2CWx+dyZTZ8zh93y14cubr3P30HO6f8jLvHtSX0afvwcKFyQ/+NIW5bza12O85B27N4I3WBuAn9zzPCy+/2RVfR52gMvu9PudERObKUSKKiA2AS4GTgfdk5gNF9v1PKvfnjQKeycyLI+J3wLcy857is3cC/0klqP8JeBn4VWZ+bxnnOh04HaDfJv13/9Ht4zv1u0md7bLbnqr1EKR2mTjyU7wx/amVIpJu/65d82c3/7nd/ew9uO+D7b2lbXnVuvxORPSJiE8BY6hcIz8VeAwgM2cWJfb5wM+orMADLd8KMA/4EHBGRHx0aefMzFGZOTQzh67Td/0O/06SJNVCTYN6RPwSeAgYBHw8M/fLzGsz863i+CbFv4PK/XmLZraPAT5ezIJ/NzA3MxdfwMrMWcAw4JsRcXDXfSNJUkOIDnjVQK2vqd8AnFxM7V+aXxVl+QAeAc4o9o+lko1PppKZn1L9wcx8trgtYGxEHJWZD3T46CVJDakL7lPvFDUN6pk5ppXjS13nNisTAc5cyv7ngB1L249SmUAnSVKb1ek8udpfU5ckSR2j1uV3SZJWOnWaqBvUJUlaQp1GdcvvkiQ1CDN1SZJKKnek1WeqblCXJKmsDU9ZW1kZ1CVJqlKnMd1r6pIkNQozdUmSqtVpqm5QlySpmXCinCRJjaJeJ8p5TV2SpAZhpi5JUkkNn5zabgZ1SZKq1WlUt/wuSVKDMFOXJKmKs98lSWoQ9Tr73aAuSVKVOo3pXlOXJKlRmKlLklRWx/e0GdQlSapSrxPlLL9LktQgzNQlSSoJnP0uSVLDqNOYbvldkqQlRAe8WjtFxLCIeCoiJkfEiKUcPycinoiIxyLizojYvLU+DeqSJHWxiOgOjAQOAYYAx0fEkKpmDwNDM3Mn4Cbg8tb6NahLklQlOuCfVuwJTM7MKZn5NjAaOKLcIDP/nJnzis37gQGtdeo1dUmSqnTBRLn+wNTS9jRgrxbanwbc3lqnBnVJkqp0UEzvFxETStujMnPUco8l4mPAUGC/1toa1CVJ6hyzM3PoMo5NBwaWtgcU+5qJiA8C5wP7Zeb81k7oNXVJkqp1/uz38cDgiBgUEb2A4cCYZkOI2BX4H+DwzJzVlmGbqUuSVFKJyZ17UT0zmyLiLGAc0B34aWZOjIiLgQmZOQa4AlgbuDEqF/lfyMzDW+rXoC5JUg1k5lhgbNW+C0vvP7i8fRrUJUkqC5eJlSSpYdRpTDeoS5K0hDqN6s5+lySpQZipS5LUTJuWeV0pGdQlSapSrxPlLL9LktQgzNQlSSpp4+PQV0oGdUmSqtVpVDeoS5JUpV4nynlNXZKkBmGmLklSlXqd/W5QlySpSp3GdMvvkiQ1CjN1SZLKfEqbJEmNpD6jukFdkqSSoH4zda+pS5LUIMzUJUmqUqeJukFdkqRq9Vp+N6hLklTFZWIlSVJNmalLklStPhN1g7okSdXqNKZbfpckqVGYqUuSVBIuEytJUuOo19nvBnVJkqrVZ0z3mrokSY3CTF2SpCp1mqgb1CVJqlavE+Usv0uS1CAM6pIkNRMd8k+rZ4kYFhFPRcTkiBixlOP7RsRDEdEUEUe3ZeQGdUmSSoJ/36venleL54joDowEDgGGAMdHxJCqZi8AJwO/buvYvaYuSVLX2xOYnJlTACJiNHAE8MSiBpn5XHFsYVs7NVOXJKlz9IuICaXX6aVj/YGppe1pxb52MVOXJKlKB81+n52ZQzukpzYyqEuSVKULlomdDgwsbQ8o9rWLQV2SpLKueaDLeGBwRAyiEsyHAye0t1OvqUuS1MUyswk4CxgHPAnckJkTI+LiiDgcICL2iIhpwDHA/0TExNb6NVOXJKkk6JplYjNzLDC2at+FpffjqZTl28ygLklSNZeJlSRJtWSmLklSlS6Y/d4pDOqSJFWp16e0GdQlSapSpzHda+qSJDUKM3VJkqrVaapuUJckqUq9TpSz/C5JUoOIzKz1GGoqIl4Cnq/1OBpcP2B2rQchtYM/w51v88zcoNaDAIiI31P5b95eszNzWAf002arfFBX54uICV39+EGpI/kzrHph+V2SpAZhUJckqUEY1NUVRtV6AFI7+TOsuuA1dUmSGoSZuiRJDcKgLklSgzCoS5LUIAzqqqmI2Ccidqn1OKTlFREHRsSRtR6HVGZQV01ELH5a8SVA/1qORVoeUQAOA7rXejxSmUFdtbIoqDcB82s5EGl5ZAHoA6xX6/FIZQZ1dbmI2B14f7E5DZhX7F9tUQYfEf5saqUTEUMj4spi81WqHtBZqkBJNeGjV1UL+wDHR8TrwNrAOgCZWc7YXUBBK6M5wD4R8Q3gWeC58sHMzIiIdAEQ1YiLz6jLRMRamflG8f6TwLHAdsAzwEtUsp4Xqfyy+Q/g+/7lqJVBRKwOLMzMtyNiC+BHwEHAC8A9wJpAT2AWMBn4lj+7qgUzdXWJiDgMODYimoBrgJ9QKb1/H7gPmFg0XRfYBBjjX4paGUTEUcCngbkRcXdm/iAizgCuBLYALgA2B7YGXgMm+rOrWjFTV6eLiB2AO4Hjgf2olNzfAb4OHAqcAnw9M++r2SClpYiIbYEbgLOpTOgcCYwp/t0b+ClwT2ZeWLNBSiVORlJXWAu4PTP/nJkXAb8p9p+fmTcCNwM/iIj3lW4XklYGPYHZwN8y82/A0cDOwGcy8zkqv5AeGhHfrN0QpX+z/K5OExGrZ+ZbVK6Z7xkRx2fmdZn51yJwHxMRe2Tm1cX285YttTKIiNWKiZvPA08C+0fEXzLzuYj4IvDbiJiTmT8syvPSSsFMXZ0iIg4AvlhMjpsDfAUYFhGHAGTmvcDbwEnF9qjMfKFmA5YKEXEoMCIiembm61R+Kf0osH1ErFFk6J8Fdo+Ibpn5gj+7WlkY1NXhImIY8G3g7kWz3YF7qUyI+2hEnFjs+wfQPSJ61WCY0hKKn91LgP/LzHcAMvN7VG5f+yJwUESsCWwFbIB/h2ol40Q5daiI2BF4EDg2M2+JiA2oLKUZmTkzIo4ALi/a7AcckpmP1W7EUkUxofNmKrej/TQi+lKZ0f5SUXb/GLA3MITK2gqnZeYjtRuxtCSDujpURAwCRgAvA9cB3wGmA4cAn87M3xR/WW4MvJqZM2s2WKkkIrYCvgHcQeX+869SWWwmi+0vFk0HAa9n5ou1GKfUEktH6lCZ+SxwBZUZ7w9Sud/8ZOBk4McRsVNmvpKZTxrQtbIoVoF7hsptlvsD/wX8MjOPAs4HNgL2yswFmTnZgK6VlbPf1WEiovuiv/Qi4tvAnZl5C0Bm3h4RNwELaztKaUnF8q7dMvOJiLgE2Lm43ZLMfLK4y3Ktmg5SagODujrEooAeERsBQzLzzxExfdE62BFxArAXlYdgSCuNIpgvzMyFAJk5KSKeLh0/CtgGmFSrMUptZfld7VYK6AOBW4GMiDUzcwGV2e3HUilhnpCZ02o6WInmT1PLzIUR0Scido2IqyNi2KL1EopnFHwNOCkzn6/VeKW2MqirXUoBfQBwPXAZlUlFIyNiE2AB8DpwWGZObKErqcuUgvaWEbEv8EfgKOBwYPVS078CH8nMx7t+lNLyc/a7VliptD6QyvrYVwAPU7kt6MLMHFPTAUotiIiLgF2o/BL6F2AKlQcNHZOZz/gIVdUjg7qWSymQdyvKlusDN1F5wMWDwI3A1zLzVv9S1MosIvYE3gSmZ+bLEXEpMCUzr67x0KQV5kQ5LZdSkN6eyuNS16RyX/qLwG+Br2TmrVVtpZVOZj6w6H1E9KBy//nNtRuR1H5eU9dyi4hTgVHFZLipVDL0M4EvLwroUp35NpXfQx9otaW0ErP8rjYrldy/DDxevmZePLjlDUvuqkcRsQ3Qr3iCYLdFt7dJ9cZMXW1WBPQtgQOpLP0KVGYQA/OLNgZ01Z3MnATcX7w3oKtuGdTVJlHRE/gS8FPgkYjYISLGAF8ANq3pAKV2MpirEThRTm1SZODvRERvKgH8TmA88CjwLSqziCVJNWRQV5tFxLbAMUBQeXzqHxY9c1qSVHtOlNNyiYh1gKbMnFfa5+Q4SVoJGNQlSWoQTpSTJKlBGNQlSWoQBnVJkhqEQV2SpAZhUJckqUEY1CVJahAGdWk5RcSCiHgkIh6PiBsjYs129LV/RPyueH94RIxooe26EfGZFTjHRRFxblv3V7W5JiKOXo5zbRERjy/vGCV1DIO6tPzezMxdMnNH4G3gjPLBYp385f5/KzPHZOa3WmiyLrDcQV3SqsOgLrXP3cDWRYb6VERcCzwODIyIgyLivoh4qMjo1waIiGER8Y+IeAj4j0UdRcTJEXFV8X6jiLg5Ih4tXu+hssb+VkWV4Iqi3ZciYnxEPBYRXyv1dX5ETIqIe4BtW/sSEfHJop9HI+J/q6oPH4yICUV/hxXtu0fEFaVzf6q9f5CS2s+gLq2giOgBHAL8vdg1GPhhZu4AvAFcAHwwM3cDJgDnRMTqwNXAh4HdgY2X0f0PgL9k5s7AbsBEYATwTFEl+FJEHFScc09gF2D3iNg3InYHhhf7PgTs0Yav85vM3KM435PAaaVjWxTnOBT4UfEdTgPmZuYeRf+fjIhBbTiPpE7kA12k5bdGRDxSvL8b+AmVJ9c9n5n3F/vfDQwB7o0IgF7AfcB2wLOZ+TRARPwSOH0p5zgA+DhAZi4A5kZE36o2BxWvh4vttakE+d7AzYvW5y8ej9uaHSPiG1RK/GsD40rHbigeS/p0REwpvsNBwE6l6+19inNPasO5JHUSg7q0/N7MzF3KO4rA/UZ5F5Wn2B1f1a7Z59opgEsz83+qzvH5FejrGuDIzHw0Ik4G9i8dq35ARBbnPjszy8GfiNhiBc4tqYNYfpc6x/3APhGxNUBErBUR2wD/ALaIiK2Kdscv4/N3Ap8uPts9IvoAr1PJwhcZB5xaulbfPyI2BP4PODIi1oiI3lRK/a3pDcyMiJ7AR6uOHRMR3Yoxbwk8VZz700V7ImKbiFirDeeR1InM1KVOkJkvFRnvdRGxWrH7gsycFBGnA7dFxDwq5fveS+nic8CoiDgNWAB8OjPvi4h7i1vGbi+uq28P3FdUCv4FfCwzH4qI64FHgVnA+DYM+SvA34CXin+Xx/QC8ACwDnBGZr4VET+mcq39oaic/CXgyLb96UjqLD56VZKkBmH5XZKkBmFQlySpQRjUJUlqEAZ1SZIahEFdkqQGYVCXJKlBGNQlSWoQ/x8cat1LmncYngAAAABJRU5ErkJggg==
{{< /png >}}

We see the largest accuracy of the less abundant class with an accuracy of 64.9%, compared to the previous best of 64.2%. We can also look the importance of different features for this XGBoost model.

{{< highlight python "linenos=table" >}}
importances = xclf.feature_importances_
indices = np.argsort(importances)
cols = [cols[x] for x in indices]
plt.figure(figsize=(10,6))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), cols)
plt.xlabel('Relative Importance')
{{< /highlight >}}

{{< png >}}
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
{{< /png >}}

## LightGBM

Similar to XGBoost, [LightGBM](http://lightgbm.readthedocs.io/en/latest/) is another optimized implementation of Gradient Boosting developed by [Microsoft](https://www.microsoft.com/en-us/defaultd.aspx) (similar to XGBoost available in Python, C++ and R). The main difference between LightGBM and other Gradient boosted trees (like XGBoost) implementations is in the way trees are grown. The details of this can be found on their [features page](https://github.com/Microsoft/LightGBM/wiki/Features). Briefly, LightGBM splits the tree leaf-wise with the best fit whereas other boosting algorithms split the tree depth-wise or level-wise. The two approaches can be best visualized in the following illustrations:

**Level-wise Splits:**

{{< figure src="https://raw.githubusercontent.com/wiki/Microsoft/LightGBM/image/level_wise.png" class="align-center img-responsive" >}}

**Leaf-wise Splits:**

{{< figure src="https://raw.githubusercontent.com/wiki/Microsoft/LightGBM/image/leaf_wise.png" class="align-center img-responsive" caption="Courtsey: LightGBM User Guide" >}}

Leaf-wise splits lead to increase in complexity and may lead to over-fitting, and hence extra caution needs to be taken in tuning. Some of the biggest advantages of LightGBM over XGBoost is in terms of extremely fast training speed, lower memory usage, compatibility with large datasets and highly parallel computational support using threads, MPI and GPUs. LightGBM also has inbuilt support for categorical variables, unlike XGBoost, where one has to pre-process the data to convert all of the categorical features to integer ones using _one-hot encoding_ or _label encoding_.

Since the trees are grown differently in LightGBM, its tuning procedure is quite different than XGBoost. Note that the latest version of XGBoost also provides a tree building strategy (depth-wise) which is quite similar to LightGBM.

All the parameters described above for XGBoost are also valid for LightGBM library. However, some parameters can have different names.
Given the strategy of growing trees is different in LightGBM, an additional parameter needs to be tuned as well.

**num_leaves**: Maximum tree leaves for base learners. Note that since trees are grown depth-first, this parameters is independent
of the **max_depth** parameter and has to be tuned independently. A typical value for starting should be much less than 2<sup>max
_depth</sup>.

When using the scikit-learn API of LightGBM, one should keep in mind that some of the parameter names are not standard ones (even though described in the API reference). In particular, I found that _seed_ and _nthreads_ as parameters, instead of *random_state* and *n_jpbs*, respectively.

Let us tune a LightGBM model for the problem of Income prediction.

{{< highlight python "linenos=table" >}}
import lightgbm as lgb

params = {'n_estimators': 100,
          'num_leaves': 48,
          'max_depth': 6,
          'subsample': 0.75,
          'learning_rate': 0.1,
          'min_child_samples': 8,
          'seed': 32,
          'nthread': 8
         }
lclf = lgb.LGBMClassifier(**params)

lclf.fit(x_train, y_train)
lclf.score(x_test, y_test)
{{< /highlight >}}

This results in test accuracy of 86.8%. 

Given this library also has many parameters, similar to XGBoost, we need to use a similar strategy of tuning in stages.

First we will fix learning rate to a reasonable value of 0.1 and number of estimators = 200, and tune only the major tree building parameters: `max_depth`, `subsample`, `colsample_bytree` and `num_leaves`. We will use the genetic algorithm to search for optimal values of these parameters.

{{< highlight python "linenos=table" >}}
ind_params = {
    'seed': 32,
    'n_estimators': 200,
    'learning_rate': 0.1,
    'nthread': 1
}
params = {'max_depth': (4, 6, 8),
          'subsample': (0.75, 0.8, 0.9, 1.0),
          'colsample_bytree': (0.75, 0.8, 0.9, 1.0),
          'num_leaves': (12, 16, 36, 48, 54, 60, 80, 100)
         }

clf2 = EvolutionaryAlgorithmSearchCV(estimator=lgb.LGBMClassifier(**ind_params),
                                   params=params,
                                   scoring="accuracy",
                                   cv=5,
                                   verbose=1,
                                   population_size=50,
                                   gene_mutation_prob=0.10,
                                   gene_crossover_prob=0.5,
                                   tournament_size=5,
                                   generations_number=100,
                                   n_jobs=8)
clf2.fit(x_train, y_train)
{{< /highlight >}}

This gives the following set of optimal parameters:

    Best individual is: {'max_depth': 6, 'subsample': 1.0, 'colsample_bytree': 0.75, 'num_leaves': 54}
    with fitness: 0.870888486225853

Now, we can use grid search to fine tune the search of number of leaves parameter.


{{< highlight python "linenos=table" >}}
ind_params = {
    'seed': 32,
    'n_estimators': 200,
    'learning_rate': 0.1,
    'nthread': 1,
    'max_depth': 6,
    'subsample': 1.0,
    'colsample_bytree': 0.75,
}
params = {
          'num_leaves': (48, 50, 52, 54, 56, 58, 60)
         }

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)
{{< /highlight >}}

Similar to XGBoost, LightGBM also provides a `cv()` method that can be used to find optimal value of number of estimators using early stopping strategy. Another strategy would be to search for this parameter as well. In the following, I want to use this grid search strategy to find best value of number of estimators, just to show how tedious this can be!

{{< highlight python "linenos=table" >}}
ind_params = {
    'seed': 32,
    'learning_rate': 0.1,
    'nthread': 1,
    'max_depth': 6,
    'subsample': 1.0,
    'colsample_bytree': 0.75,
    'num_leaves': 54
}
params = {'n_estimators': (200,300,400,800,1000)}

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

params = {'n_estimators': (250,275,300,320,340,360,380)}

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

params = {'n_estimators': (322,324,325,326,327,328,330,332,334,336,338)}

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

{{< /highlight >}}

We find that the optimal value of `n_estimators` to be 327.

Now, we can use the similar strategy to find and fine-tune the best regularization parameters.

{{< highlight python "linenos=table" >}}
ind_params = {
    'seed': 32,
    'learning_rate': 0.1,
    'n_estimators': 327,
    'nthread': 1,
    'max_depth': 6,
    'subsample': 1.0,
    'colsample_bytree': 0.75,
    'num_leaves': 54
}

params = {'reg_alpha' : [0,0.1,0.5,1],'reg_lambda' : [1,2,3,4,6],}

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

params = {'reg_alpha' : [0.2,0.3,0.4,0.5,0.6,0.7,0.9],'reg_lambda' : [1.5,2,2.5],}
clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

params = {'reg_alpha' : [0.55,0.58,0.6,0.62,0.65,0.68],'reg_lambda' : [1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9],}
clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

params = {'reg_alpha' : [0.61,0.62,0.63,0.64],'reg_lambda' : [1.85,1.88,1.9,1.95,1.98],}
clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)
{{< /highlight >}}

Finally, we can decrease the learning rate to 0.01 and find the optimal value of `n_estimators`.

{{< highlight python "linenos=table" >}}
ind_params = {
    'seed': 32,
    'learning_rate': 0.01,
    'nthread': 1,
    'max_depth': 6,
    'subsample': 1.0,
    'colsample_bytree': 0.75,
    'num_leaves': 54,
    'reg_alpha': 0.62,
    'reg_lambda': 1.9
}
params = {'n_estimators': (3270,3280,3300,3320,3340,3360,3380,3400)}

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

params = {'n_estimators': (3325,3330,3335,3340,3345,3350,3355)}

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)

params = {'n_estimators': (3326,3327,3328,3329,3330,3331,3332,3333,3334)}

clf2 = GridSearchCV(lgb.LGBMClassifier(**ind_params), params, cv=5, n_jobs=8, verbose=1)
clf2.fit(x_train, y_train)
print(clf2.best_params_)
{{< /highlight >}}

We find the optimal `n_estimators` to be equal to 3327 for a learning rate of 0.01. We can now built a final LightGBM model using these parameters and evaluate the test data.

{{< highlight python "linenos=table" >}}
ind_params = {
    'seed': 32,
    'learning_rate': 0.01,
    'n_estimators': 3327,
    'nthread': 8,
    'max_depth': 6,
    'subsample': 1.0,
    'colsample_bytree': 0.75,
    'num_leaves': 54,
    'reg_alpha': 0.62,
    'reg_lambda': 1.9
}
lclf = lgb.LGBMClassifier(**ind_params)
lclf.fit(x_train, y_train)
lclf.score(x_test, y_test)
{{< /highlight >}}

We get a test accuracy of 87.01%. Similar to previous cases, we can again look at the accuracy of individual classes using the following confusion matrix plot:

{{< highlight python "linenos=table" >}}
y_pred = lclf.predict(x_test)
cfm = confusion_matrix(y_test, y_pred, labels=[0, 1])
plt.figure(figsize=(10,6))
plot_confusion_matrix(cfm, classes=["<=50K", ">50K"], normalize=True)
{{< /highlight >}}

{{< png >}}
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
{{< /png >}}

We find the results to be slightly better than XGBoost with 65% accuracy of the less abundant >50K salary class. We can also look the importance of different features in this model:

{{< highlight python "linenos=table" >}}
importances = lclf.feature_importances_
indices = np.argsort(importances)
cols = [cols[x] for x in indices]
plt.figure(figsize=(10,6))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='b', align='center')
plt.yticks(range(len(indices)), cols)
plt.xlabel('Relative Importance')
{{< /highlight >}}

{{< png >}}
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
{{< /png >}}

Concluding Remarks
===================

XGBoost has been one of the most famous libraries used to win several machine learning competitions on Kaggle and similar sites. Slowly, LightGBM is also gaining traction due to its speed and parallelization capabilities. [CatBoost](https://github.com/catboost/catboost) is another boosting library from [Yandex](https://www.yandex.com) that has been [shown to be quite efficient](https://catboost.yandex). I have used it personally yet though. If I find it to be worth making a move to, I will write about it in a future post.