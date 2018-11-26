---
title: "A Practical guide to Autoencoders"
date: 2018-04-26T18:47:44-07:00
tags:
    - Deep Learning
    - Machine Learning
    - Python
    - Data Science
categories:
    - Machine Learning
slug: autoencoders
link:
authors:
    - "Sadanand Singh"
hasMath: true
notebook: false
draft: false
disqus_identifier: "autoencoders.sadanand"
description:
---

Usually in a conventional neural network, one tries to predict a target vector
$y$ from input vectors $x$. In an auto-encoder network, one tries to predict
$x$ from $x$. It is trivial to learn a mapping from $x$ to $x$ if the network
has no constraints, but if the network is constrained the learning process
becomes more interesting. In this article, we are going to take a detailed
look at the mathematics of different types of autoencoders (with different
constraints) along with a sample implementation of it using [Keras],
with a [tensorflow] back-end.

[Keras]: https://keras.io
[tensorflow]: https://tensorflow.org
<!--more-->

<!--TOC-->

# Basic Autoencoders

{{< figure src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSx1PGY44IVn6aV-zTjvOD8IK3xNnv6vMDLHpsA2ignlXE6SrfBrg" class="figure img-responsive align-right" width="320px" >}}

The simplest AutoEncoder (AE) has an MLP-like (Multi Layer Perceptron)
structure:

- Input Layer
- Hidden Layer, and
- Output Layer

However, unlike MLP, autoencoders do not require any target data.
As the network is trying to learn $x$ itself, the learning algorithm is a
special case of
[__unsupervised learning__](https://en.wikipedia.org/wiki/Unsupervised_learning).

Mathematically, lets define:

- Input vector: $x \in \Big[ 0, 1 \Big]^d$
- Activation function: $a(h)$ applied to very nuron of layer $h$
- {{< tex "W_i \in \mathbb{R}^{I_{di} \times O_{di}}" >}}, the parameter matrix
of $i$-th layer, projecting a{{< tex "I_{di}" >}} dimensional input in
a {{< tex "O_{di}" >}}dimensional space
- {{< tex "b_i \in \mathbb{R}^{O_{di}}" >}} bias vector

The simplest AE can then be summarized as:
{{< tex display="\begin{aligned} z &=  a(x W_1 + b_1) \\ x' &=  a(z W_2 + b_2) \end{aligned}" >}}

The AE model tries to minimize the __reconstruction error__ between the input
value $x$ and the reconstructed value {{< tex "x'" >}}.
A typical definition of the reconstruction error is the $L_p$ distance
(like $L_2$ norm) between the $x$ and {{< tex "x'" >}} vectors:
{{< tex display="\min \mathcal{L} = \min E(x, x') \stackrel{e.g.}{=} \min || x - x' ||_p" >}}

Another common variant of loss function (especially images) for AE is the
cross entropy function.
{{< tex display="\mathcal{L}(x, x') = -\sum_{c=1}^{M} x'_c \log (x_c)" >}}

where $M$ is the dimensionality of the input data $x$ (for eg. no. of
pixels in an image).

## Autoencoders in Practice

The above example of auto-encoder is too simplistic for any real use case.
It can be easily noticed that if the number of units in the hidden layer is
greater than or equal to the number of input units, the network will learn
the identity function easily.
Hence, the simplest constraint used in real-life autoencoders is the
__number of hidden units__ ($z$) should be less than the dimensions ($d$) of
the input ($z < d$).

By limiting the amount of information that can flow through the network, AE
model can learn the most important attributes of the input data and how to best
reconstruct the original input from an "encoded" state.
Ideally, this encoding will
__learn and describe latent attributes of the input data.__
Dimensionality reduction using
AEs leads to better results than classical dimensionality reduction techniques
such as [PCA] due to the non-linearities and the type of constraints applied.

{{< card "" "PCA and Autoencoders" >}}
If we were to construct a linear network (i.e. without the use of
nonlinear activation functions at each layer) we would observe a similar
dimensionality reduction as observed in [PCA].
See [Geoffrey Hinton's discussion][1].
[PCA]: https://en.wikipedia.org/wiki/Principal_component_analysis
[1]: https://www.coursera.org/learn/neural-networks/lecture/JiT1i/from-pca-to-autoencoders-5-mins
{{< /card >}}

[PCA]: https://en.wikipedia.org/wiki/Principal_component_analysis

A practical auto-encoder network consists of an encoding function (_encoder_),
and a decoding function (_decoder_). Following is an example architecture for
the reconstruction of images.

{{< figure src="https://cdn-images-1.medium.com/max/1600/1*op0VO_QK4vMtCnXtmigDhA.png" class="figure img-responsive align-center" width="540px" >}}

In this article we will build different types of autoencoders for the
[fashion MNIST] dataset. In stead of using more common [MNIST] dataset,
I prefer to use [fashion MNIST] dataset for the [reasons described here][2].

[fashion MNIST]: https://github.com/zalandoresearch/fashion-mnist
[MNIST]: http://yann.lecun.com/exdb/mnist/
[2]: https://github.com/zalandoresearch/fashion-mnist#to-serious-machine-learning-researchers

For example using [MNIST] data, please have a look at the [article] by
[Francois Chollet][3], the creator of [Keras]. The code below is heavily adapted
from his article.

[article]: https://blog.keras.io/building-autoencoders-in-keras.html
[3]: https://twitter.com/fchollet

We'll start simple, with a single fully-connected neural layer as encoder
and as decoder.
{{< highlight lang="python" linenos="yes" >}}
from keras.layers import Input, Dense
from keras.models import Model
import numpy as np

# size of bottleneck latent space
encoding_dim = 32
# input placeholder
input_img = Input(shape=(784,))
# encoded representation
encoded = Dense(encoding_dim, activation='relu')(input_img)
# lossy reconstruction
decoded = Dense(784, activation='sigmoid')(encoded)

# full AE model: map an input to its reconstruction
autoencoder = Model(input_img, decoded)
{{< /highlight >}}

We will also create separate encoding and decoding functions, that can be used
to extract latent features at test time.

{{< highlight lang="python" linenos="yes" start="16" >}}
# encoder: map an input to its encoded representation
encoder = Model(input_img, encoded)
# placeholder for an encoded input
encoded_input = Input(shape=(encoding_dim,))
# last layer of the autoencoder model
decoder_layer = autoencoder.layers[-1]
# decoder
decoder = Model(encoded_input, decoder_layer(encoded_input))
{{< /highlight >}}

We can now set the optimizer and the loss function before training the
auto-encoder model.
{{< highlight lang="python" linenos="yes" start="24" >}}
autoencoder.compile(optimizer='rmsprop', loss='binary_crossentropy')
{{< /highlight >}}

Next, we need to get the [fashion MNIST] data and normalize it for training.
Furthermore, we will flatten the $28\times28$ images to a vector of size 784.
Please note that running the code below for the first time will download the
full dataset and hence might take few minutes.

{{< highlight lang="python" linenos="yes" start="25" >}}
from keras.datasets import fashion_mnist

(x_train, _), (x_test, _) = fashion_mnist.load_data()
x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
print(x_train.shape, x_test.shape)
{{< /highlight >}}

**Output:**
    (60000, 784) (10000, 784)

We can now train our model for 100 epochs:
{{< highlight lang="python" linenos="yes" start="33" >}}
history = autoencoder.fit(x_train, x_train,
                epochs=100,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))
{{< /highlight >}}

This will print per epoch training and validation loss. But we can plot the loss
history during training using the history object.
{{< highlight lang="python" linenos="yes" hl="4-12" >}}
import matplotlib.pyplot as plt
%matplotlib inline

def plot_train_history_loss(history):
    # summarize history for loss
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.title('model loss')
    plt.ylabel('loss')
    plt.xlabel('epoch')
    plt.legend(['train', 'test'], loc='upper right')
    plt.show()

plot_train_history_loss(history)
{{< /highlight >}}
**Output:**
{{< png >}}
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
{{< /png >}}

After 100 epochs, the auto-encoder reaches a stable train/text loss value of
about 0.282. Let us look visually how good of reconstruction this
simple model does!
{{< highlight lang="python" linenos="yes" >}}
# encode and decode some images from test set
encoded_imgs = encoder.predict(x_test)
decoded_imgs = decoder.predict(encoded_imgs)

def display_reconstructed(x_test, decoded_imgs, n=10):
    plt.figure(figsize=(20, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(2, n, i + 1)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        if decoded_imgs is not None:
            # display reconstruction
            ax = plt.subplot(2, n, i + 1 + n)
            plt.imshow(decoded_imgs[i].reshape(28, 28))
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)
    plt.show()

display_reconstructed(x_test, decoded_imgs, 10)
{{< /highlight >}}

The top row is the original image, while bottom row is the reconstructed image.
We can see that we are loosing a lot of fine details.

{{< figure src="../../images/autoencoders/ae_basic_fm.png" alt="sample images" class="figure img-responsive align-center" >}}

## Sparsity Constraint

We can add an additional constraint to the above AE model, a sparsity
constraints on the latent variables. Mathematically, this is achieved by adding
a sparsity penalty $\Omega(\mathbf{h})$ on the bottleneck layer $\mathbf{h}$.
{{< tex display="\min \mathcal{L} = \min E(x, x') + \Omega(h)" >}}
where, $\mathbf{h}$ is the encoder output.

Sparsity is a desired characteristic for an auto-encoder, because it allows to
use a greater number of hidden units (even more than the input ones) and
therefore gives the network the ability of learning different connections
and extract different features (w.r.t. the features extracted with the only
constraint on the number of hidden units). Moreover, sparsity can be used
together with the constraint on the number of hidden units: an optimization
process of the combination of these hyper-parameters is required to achieve
better performance.

In Keras, sparsity constraint can be achieved by adding an **activity_regularizer**
to our Dense layer:
{{< highlight lang="python" linenos="yes" >}}
from keras import regularizers

encoding_dim = 32

input_img = Input(shape=(784,))
# add a Dense layer with a L1 activity regularizer
encoded = Dense(encoding_dim, activation='relu',
                activity_regularizer=regularizers.l1(1e-8))(input_img)
decoded = Dense(784, activation='sigmoid')(encoded)

autoencoder = Model(input_img, decoded)
{{< /highlight >}}

Similar to the previous model, we can train this as well for 150 epochs.
Using a regularizer is less likely to overfit and hence can be trained for
longer.
{{< highlight lang="python" linenos="yes" >}}
autoencoder.compile(optimizer='rmsprop', loss='binary_crossentropy')
history = autoencoder.fit(x_train, x_train,
                epochs=150,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))

plot_train_history_loss(history)
{{< /highlight >}}

We get a very similar loss as the previous example. Here is a plot of
loss values during training.
{{< png >}}
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
{{< /png >}}

As expected, the reconstructed images too look quite similar as before.
{{< highlight lang="python" linenos="true" >}}
decoded_imgs = autoencoder.predict(x_test)
display_reconstructed(x_test, decoded_imgs, 10)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/ae_sparsity_fm.png" alt="sample images" class="figure img-responsive align-center" >}}

## Deep Autoencoders

We have been using only single layers for encoders and decoders. Given we have large enough data, there is nothing that stops us from building deeper networks
for encoders and decoders.

{{< highlight lang="python" linenos="true" >}}
input_img = Input(shape=(784,))
encoded = Dense(128, activation='relu')(input_img)
encoded = Dense(64, activation='relu')(encoded)
encoded = Dense(32, activation='relu')(encoded)

decoded = Dense(64, activation='relu')(encoded)
decoded = Dense(128, activation='relu')(decoded)
decoded = Dense(784, activation='sigmoid')(decoded)

autoencoder = Model(input_img, decoded)
{{< /highlight >}}

We can train this model, same as before.
{{< highlight lang="python" linenos="yes" >}}
autoencoder.compile(optimizer='rmsprop', loss='binary_crossentropy')
history = autoencoder.fit(x_train, x_train,
                epochs=150,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test))

plot_train_history_loss(history)
{{< /highlight >}}

{{< png >}}
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
{{< /png >}}

The average loss is now  0.277, as compared to ~0.285 before! We can also see that visually all reconstructed images too look slightly better.

{{< highlight lang="python" linenos="yes" >}}
decoded_imgs = autoencoder.predict(x_test)
display_reconstructed(x_test, decoded_imgs, 10)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/ae_deep_fm.png" alt="sample images" class="figure img-responsive align-center" >}}

## Convolutional Autoencoders

Since our inputs are images, it makes sense to use convolution neural
networks (conv-nets) as encoders and decoders. In practical settings,
autoencoders applied to images are always convolution autoencoders --they
simply perform much better.

The encoder will consist of a stack of `Conv2D` and `MaxPooling2D` layers (max
pooling being used for spatial down-sampling), while the decoder will consist
of a stack of `Conv2D` and `UpSampling2D` layers. We will also be using
`BatchNormalization`. One major difference between this network and prior ones is that now we have 256 (4x4x16) elements in the bottleneck layer as opposed to
just 32 before!

You can read more about convolution-based auto-encoders in further details [here][cae].

[cae]: https://pgaleone.eu/neural-networks/2016/11/24/convolutional-autoencoders/

{{< highlight lang="python" linenos="yes" >}}
from keras.layers import Input, Dense, Conv2D, MaxPooling2D, UpSampling2D, BatchNormalization
from keras.models import Model
from keras import backend as K

input_img = Input(shape=(28, 28, 1))

x = Conv2D(32, (3, 3), activation='relu', padding='same', use_bias=False)(input_img)
x = BatchNormalization(axis=-1)(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(16, (3, 3), activation='relu', padding='same', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(16, (3, 3), activation='relu', padding='same', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)

x = Conv2D(16, (3, 3), activation='relu', padding='same', use_bias=False)(encoded)
x = BatchNormalization(axis=-1)(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(16, (3, 3), activation='relu', padding='same', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(32, (3, 3), activation='relu', padding='valid', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same', use_bias=False)(x)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='rmsprop', loss='binary_crossentropy')
{{< /highlight >}}

To train it, we will use the original fashion MNIST digits with shape (samples, 1, 28, 28), and we will just normalize pixel values between 0 and 1.
{{< highlight lang="python" linenos="yes" >}}
(x_train, _), (x_test, _) = fashion_mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = np.reshape(x_train, (len(x_train), 28, 28, 1))
x_test = np.reshape(x_test, (len(x_test), 28, 28, 1))
{{< /highlight >}}

Similar to before, we can train this model for 150 epochs. However, unlike 
before, we will checkpoint the model during training to save the best model,
based on the validation loss minima.

{{< highlight lang="python" linenos="yes" >}}
from keras.callbacks import ModelCheckpoint

fpath = "weights-ae-{epoch:02d}-{val_loss:.3f}.hdf5"
callbacks = [ModelCheckpoint(fpath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')]
history = autoencoder.fit(x_train, x_train,
                epochs=150,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test, x_test),
                callbacks=callbacks)

plot_train_history_loss(history)
{{< /highlight >}}

{{< png >}}
iVBORw0KGgoAAAANSUhEUgAAAYsAAAEWCAYAAACXGLsWAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADl0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uIDIuMi4yLCBodHRwOi8vbWF0cGxvdGxpYi5vcmcvhp/UCwAAIABJREFUeJzt3Xl8VPW5x/HPM0s2EsIW9lXAKoKiRhTRuiu4W1t3a7W96K1e7WbV1tpq671W77VW69pq61JFi0tpxYpYdwVZZF9kESHssoUAWWbmuX88J2QSJiQBJhPN8369eGXONvObEzLf+S3nd0RVcc4553YnlOkCOOeca/k8LJxzzjXIw8I551yDPCycc841yMPCOedcgzwsnHPONcjDwrl9QET+IiK/aeS+y0Tk5L19Hueak4eFc865BnlYOOeca5CHhWs1guafG0VklohsE5HHRaSLiLwmIltFZKKItE/a/2wRmSsim0XkbRE5MGnboSIyPTjueSCnzmudKSIzgmM/FJGD97DM/yEii0Vko4iME5HuwXoRkd+JyDoRKRWR2SIyONh2uojMC8q2UkR+skcnzLkkHhautTkfOAXYHzgLeA34GVCE/T1cDyAi+wPPAT8Ito0H/iEiWSKSBbwCPA10AP4WPC/BsYcCTwBXAx2BR4FxIpLdlIKKyInA/wAXAN2Az4ExweZTga8H76Mw2GdDsO1x4GpVLQAGA/9uyus6l4qHhWttHlDVtaq6EngPmKyqn6hqOfAycGiw34XAq6r6hqpWAf8L5AJHA0cBUeA+Va1S1bHAlKTXGA08qqqTVTWuqk8CFcFxTXEp8ISqTlfVCuAWYLiI9AWqgALgAEBUdb6qrg6OqwIGiUhbVd2kqtOb+LrO7cLDwrU2a5Me70ixnB887o59kwdAVRPACqBHsG2l1p6F8/Okx32AHwdNUJtFZDPQKziuKeqWoQyrPfRQ1X8DfwAeBNaJyGMi0jbY9XzgdOBzEXlHRIY38XWd24WHhXOprcI+9AHrI8A+8FcCq4EewbpqvZMerwDuVNV2Sf/yVPW5vSxDG6xZayWAqt6vqocDg7DmqBuD9VNU9RygM9Zc9kITX9e5XXhYOJfaC8AZInKSiESBH2NNSR8CHwEx4HoRiYrIN4BhScf+EbhGRI4MOqLbiMgZIlLQxDI8B1wpIkOD/o7/xprNlonIEcHzR4FtQDmQCPpULhWRwqD5rBRI7MV5cA7wsHAuJVVdCFwGPAB8gXWGn6WqlapaCXwD+A6wEevfeCnp2KnAf2DNRJuAxcG+TS3DROAXwItYbaY/cFGwuS0WSpuwpqoNwD3BtsuBZSJSClyD9X04t1fEb37knHOuIV6zcM451yAPC+eccw3ysHDOOdcgDwvnnHMNimS6APtKp06dtG/fvpkuhnPOfalMmzbtC1Utami/r0xY9O3bl6lTp2a6GM4596UiIp83vJc3QznnnGsEDwvnnHMN8rBwzjnXoK9Mn4Vzzu2JqqoqSkpKKC8vz3RR0ionJ4eePXsSjUb36HgPC+dcq1ZSUkJBQQF9+/al9kTCXx2qyoYNGygpKaFfv3579BzeDOWca9XKy8vp2LHjVzYoAESEjh077lXtycPCOdfqfZWDotrevkcPi/It8PZdsHJapkvinHMtlocFwNv/A59/mOlSOOdaoc2bN/PQQw81+bjTTz+dzZs3p6FEqXlYZLeFaBsoXd3wvs45t4/VFxaxWGy3x40fP5527dqlq1i78NFQItC2O5SuzHRJnHOt0M0338ySJUsYOnQo0WiUnJwc2rdvz4IFC/j0008599xzWbFiBeXl5dxwww2MHj0aqJniqKysjFGjRnHMMcfw4Ycf0qNHD/7+97+Tm5u7T8vpYQFBWKzKdCmccxl2+z/mMm9V6T59zkHd2/LLsw6qd/tdd93FnDlzmDFjBm+//TZnnHEGc+bM2TnE9YknnqBDhw7s2LGDI444gvPPP5+OHTvWeo5Fixbx3HPP8cc//pELLriAF198kcsuu2yfvg9vhgILi63eDOWcy7xhw4bVuhbi/vvv55BDDuGoo45ixYoVLFq0aJdj+vXrx9ChQwE4/PDDWbZs2T4vl9csoCYsEnEIhTNdGudchuyuBtBc2rRps/Px22+/zcSJE/noo4/Iy8vj+OOPT3mtRHZ29s7H4XCYHTt27PNyec0CoKAbJGKwbX2mS+Kca2UKCgrYunVrym1btmyhffv25OXlsWDBAiZNmtTMpavhNQuAtj3sZ+kqKOia2bI451qVjh07MmLECAYPHkxubi5dunTZuW3kyJE88sgjHHjggXzta1/jqKOOylg5PSzAmqHAwqLHYZkti3Ou1Xn22WdTrs/Ozua1115Lua26X6JTp07MmTNn5/qf/OQn+7x84M1QJjksnHPO7cLDAiCvE4SisNXDwjnnUvGwAAiFrJPbaxbOOZdSWsNCREaKyEIRWSwiN6fYfo2IzBaRGSLyvogMCtZHReTJYNt8EbklneUE/MI855zbjbSFhYiEgQeBUcAg4OLqMEjyrKoOUdWhwN3AvcH6bwHZqjoEOBy4WkT6pqusgIeFc87tRjprFsOAxaq6VFUrgTHAOck7qGrydfVtAK3eBLQRkQiQC1QC+/Ya/Lqqw0K14X2dc66VSWdY9ABWJC2XBOtqEZFrRWQJVrO4Plg9FtgGrAaWA/+rqhtTHDtaRKaKyNT16/fygrq23SG2A3Zs2rvncc65JtjTKcoB7rvvPrZv376PS5Raxju4VfVBVe0P3ATcGqweBsSB7kA/4Mcisl+KYx9T1WJVLS4qKtq7ghR0s58+R5Rzrhl9WcIinRflrQR6JS33DNbVZwzwcPD4EuBfqloFrBORD4BiYGk6CgrUvoq7S+bnh3HOtQ7JU5SfcsopdO7cmRdeeIGKigrOO+88br/9drZt28YFF1xASUkJ8XicX/ziF6xdu5ZVq1Zxwgkn0KlTJ9566620ljOdYTEFGCgi/bCQuAgLgZ1EZKCqVk+heAZQ/Xg5cCLwtIi0AY4C7ktjWZMuzPP7WjjXar12M6yZvW+fs+sQGHVXvZuTpyifMGECY8eO5eOPP0ZVOfvss3n33XdZv3493bt359VXXwVszqjCwkLuvfde3nrrLTp16rRvy5xC2pqhVDUGXAe8DswHXlDVuSJyh4icHex2nYjMFZEZwI+AK4L1DwL5IjIXC50/q+qsdJUVgLxgfvjtu3SNOOdcs5gwYQITJkzg0EMP5bDDDmPBggUsWrSIIUOG8MYbb3DTTTfx3nvvUVhY2OxlS+vcUKo6HhhfZ91tSY9vqOe4Mmz4bPMJR4MXjzfryzrnWpDd1ACag6pyyy23cPXVV++ybfr06YwfP55bb72Vk046idtuuy3FM6RPxju4WwwJ7mOR8LBwzjWf5CnKTzvtNJ544gnKysoAWLlyJevWrWPVqlXk5eVx2WWXceONNzJ9+vRdjk03n3W2WigEErL7WjjnXDNJnqJ81KhRXHLJJQwfPhyA/Px8nnnmGRYvXsyNN95IKBQiGo3y8MM2Fmj06NGMHDmS7t27p72DW/QrchFacXGxTp06de+e5NdFMPxaOPlX+6JIzrkvgfnz53PggQdmuhjNItV7FZFpqlrc0LHeDJUsFPGahXPOpeBhkSwU8T4L55xLwcMiWSjsNQvnWqGvSnP87uzte/SwSObNUM61Ojk5OWzYsOErHRiqyoYNG8jJydnj5/DRUMk8LJxrdXr27ElJSQl7PRlpC5eTk0PPnj33+HgPi2TeZ+FcqxONRunXr1+mi9HieTNUMu+zcM65lDwskomHhXPOpeJhkcz7LJxzLiUPi2TeZ+Gccyl5WCTzPgvnnEvJwyKZN0M551xKHhbJPCyccy6lVh8WFbE4by1Yx4qN273Pwjnn6tHqw2JreYwr/zKFtxau8z4L55yrR6sPi2jYTkFVXL0Zyjnn6uFhERYAquIJDwvnnKtHqw+LSMhOQczDwjnn6tXqw6K6ZlEZ16DPwju4nXOurlYfFiJCJCRes3DOud1Ia1iIyEgRWSgii0Xk5hTbrxGR2SIyQ0TeF5FBSdsOFpGPRGRusM+e37WjAZGwEEt4B7dzztUnbWEhImHgQWAUMAi4ODkMAs+q6hBVHQrcDdwbHBsBngGuUdWDgOOBqnSVNRoOURlL+HUWzjlXj3TWLIYBi1V1qapWAmOAc5J3UNXSpMU2QPV9DU8FZqnqzGC/Daqatk/xaDhELOFh4Zxz9UlnWPQAViQtlwTrahGRa0VkCVazuD5YvT+gIvK6iEwXkZ+megERGS0iU0Vk6t7cEtH6LNQvynPOuXpkvINbVR9U1f7ATcCtweoIcAxwafDzPBE5KcWxj6lqsaoWFxUV7XEZouEQld7B7Zxz9UpnWKwEeiUt9wzW1WcMcG7wuAR4V1W/UNXtwHjgsLSUEhs+G/MruJ1zrl7pDIspwEAR6SciWcBFwLjkHURkYNLiGcCi4PHrwBARyQs6u48D5qWroBHvs3DOud2KpOuJVTUmItdhH/xh4AlVnSsidwBTVXUccJ2InIyNdNoEXBEcu0lE7sUCR4Hxqvpquspqo6G8z8I55+qTtrAAUNXxWBNS8rrbkh7fsJtjn8GGz6ZdNCxJNQsPC+ecqyvjHdwtQc1oKA8L55xLxcOCOqOhUEgkMl0k55xrUTwsCC7KiyeszwK8duGcc3V4WFDdZxE0Q4GHhXPO1eFhgQ2d3Tk3FHhYOOdcHR4WeM3COeca4mFBqj4LvzDPOeeSeVhgt1atinvNwjnn6uNhgTVDVcW9z8I55+rjYUH1/Sy8ZuGcc/XxsMBuq1pVazSU91k451wyDwusZlGV8IvynHOuPh4WVPdZeDOUc87Vx8MCGw0VTyjqNQvnnEvJwwKrWQDE8OssnHMuFQ8LrM8CIK5es3DOuVQ8LLC5oQBi1afDw8I552rxsCBVM5SHhXPOJfOwoKYZymsWzjmXmocFdltVSO6z8A5u55xL5mFBTc2iymsWzjmXkocFSc1Q6mHhnHOppDUsRGSkiCwUkcUicnOK7deIyGwRmSEi74vIoDrbe4tImYj8JJ3ljAQd3FUeFs45l1LawkJEwsCDwChgEHBx3TAAnlXVIao6FLgbuLfO9nuB19JVxmp+UZ5zzu1eOmsWw4DFqrpUVSuBMcA5yTuoamnSYhtAqxdE5FzgM2BuGssIJPVZeM3COedSSmdY9ABWJC2XBOtqEZFrRWQJVrO4PliXD9wE3L67FxCR0SIyVUSmrl+/fo8LGgnZaaj0sHDOuZQy3sGtqg+qan8sHG4NVv8K+J2qljVw7GOqWqyqxUVFRXtchp3NUAkPC+ecSyWSxudeCfRKWu4ZrKvPGODh4PGRwDdF5G6gHZAQkXJV/UM6ClrdDOU1C+ecSy2dYTEFGCgi/bCQuAi4JHkHERmoqouCxTOARQCqemzSPr8CytIVFJBqNJR3cDvnXLK0hYWqxkTkOuB1IAw8oapzReQOYKqqjgOuE5GTgSpgE3BFusqzO97B7Zxzu5fOmgWqOh4YX2fdbUmPb2jEc/xq35estp3NUAmrYXhYOOdcbRnv4G4JqueGqvT7WTjnXEoeFkBWpLpm4X0WzjmXiocFNTWLqgSAeM3COefq8LCg5k55VfEEhCIeFs45V4eHBZBVPetsQj0snHMuBQ8Lkq6ziFXXLLzPwjnnknlYkNxnoRAKe83COefq8LAARIRoWLzPwjnn6uFhEYiEQsQ8LJxzLqVGhYWI3CAibcU8LiLTReTUdBeuOUXCQlVcvc/COedSaGzN4qrgRkWnAu2By4G70laqDMgKh4JmKO+zcM65uhobFsGkSZwOPK2qc5PWfSVEwkIs7kNnnXMulcaGxTQRmYCFxesiUgAk0les5hcJhahKeJ+Fc86l0thZZ78LDAWWqup2EekAXJm+YjW/rEgoqc/Cw8I555I1tmYxHFioqptF5DLs9qdb0les5hcJSTAaKuwd3M45V0djw+JhYLuIHAL8GFgCPJW2UmVAJOw1C+ecq09jwyKmqgqcA/xBVR8ECtJXrOaX5RflOedcvRrbZ7FVRG7BhsweKyIhIJq+YjW/SDhEzDu4nXMupcbWLC4EKrDrLdYAPYF70laqDIiEqi/K8z4L55yrq1FhEQTEX4FCETkTKFfVr1SfhY2G8pqFc86l0tjpPi4APga+BVwATBaRb6azYM3NRkN5B7dzzqXS2D6LnwNHqOo6ABEpAiYCY9NVsOYWCXvNwjnn6tPYPotQdVAENjTh2C+F2nNDeZ+Fc84la+wH/r9E5HUR+Y6IfAd4FRjf0EEiMlJEForIYhG5OcX2a0RktojMEJH3RWRQsP4UEZkWbJsmIic25U3tiUhY/LaqzjlXj0Y1Q6nqjSJyPjAiWPWYqr68u2NEJAw8CJwClABTRGScqs5L2u1ZVX0k2P9s4F5gJPAFcJaqrhKRwcDrQI8mvK8ms/tZeFg451wqje2zQFVfBF5swnMPAxar6lIAERmDXdS3MyyCac+rtQE0WP9J0vq5QK6IZKtqRRNev0myIkKl91k451xKuw0LEdlK8AFedxOgqtp2N4f3AFYkLZcAR6Z4jWuBHwFZQKrmpvOB6amCQkRGA6MBevfuvZuiNKzmTnneZ+Gcc3Xtts9CVQtUtW2KfwUNBEWjqeqDqtofuAmboHAnETkI+C1wdT3HPqaqxapaXFRUtFflqLmfRRjUw8I555Klc0TTSqBX0nLPYF19xgDnVi+ISE/gZeDbqrokLSVMkhUOeTOUc87VI51hMQUYKCL9RCQLuAgYl7yDiAxMWjwDWBSsb4eNuLpZVT9IYxl38tFQzjlXv7SFharGgOuwkUzzgRdUda6I3BGMfAK4TkTmisgMrN/iiur1wADgtmBY7QwR6ZyusgJEwyHiCUXF+yycc66uRo+G2hOqOp4612Oo6m1Jj2+o57jfAL9JZ9nqioYtN+MSJuI1C+ecq+UrdRX23oiEBICEhL0Zyjnn6vCwCFTXLBJ4WDjnXF0eFoFo2GoWccKgCUgkMlwi55xrOTwsApHqmoWEbYVfa+Gcczt5WASqm6FiBGHhTVHOObeTh0WgphkqOCUeFs45t5OHRSASCobOes3COed24WERqNXBDX5hnnPOJfGwCNT0WXgzlHPO1eVhEYjsUrPwsHDOuWoeFoGdNQv1moVzztXlYRGo7rOIeZ+Fc87twsMiUD0aqlafxdt3wecfZbBUzjnXMqR11tkvk12aoWLlFhalK6HP8AyWzDnnMs9rFoHqZqgqDZqhtq4BFDavqP8g55xrJTwsApG6Q2dLgzvAbvGwcM45D4vALjWLLdVhUQKqGSqVc861DB4Wgeo+iyq10KB0lf2MlcO29RkqlXPOtQweFoHqO+XFqmsWpSU1G73fwjnXynlYBKKR6ppFcEqqm6EAtizPQImcc67l8LAI5ETCiMDWqmBF6Soo6G6PvWbhnGvlPCwCWZEQPdrlsnJLpa2I7YBOAyC70EdEOedavbSGhYiMFJGFIrJYRG5Osf0aEZktIjNE5H0RGZS07ZbguIUiclo6y1mtX6c2LN9cWbMivysU9vSahXOu1UtbWIhIGHgQGAUMAi5ODoPAs6o6RFWHAncD9wbHDgIuAg4CRgIPBc+XVv2L8vl8U0XNivzO0K6X1yycc61eOmsWw4DFqrpUVSuBMcA5yTuoamnSYhug+oKGc4Axqlqhqp8Bi4PnS6t+ndpQVpW0oqArFPbymoVzrtVL59xQPYDkT9kS4Mi6O4nItcCPgCzgxKRjJ9U5tkeKY0cDowF69+691wXer6hNzayzAPldQBNQsQXKt0BO4V6/hnPOfRllvINbVR9U1f7ATcCtTTz2MVUtVtXioqKivS5Lv05tiGvSKcnvYjUL8NqFc65VS2dYrAR6JS33DNbVZwxw7h4eu090L8wlFInWrMjvAu2CGsuWktQHOedcK5DOsJgCDBSRfiKShXVYj0veQUQGJi2eASwKHo8DLhKRbBHpBwwEPk5jWQEIhYQeHfJrVhQk1Sy8k9s514qlrc9CVWMich3wOhAGnlDVuSJyBzBVVccB14nIyUAVsAm4Ijh2roi8AMwDYsC1qtost67r1akASoFwNuS0s0kEw9mw+fPmeHnnnGuR0nrzI1UdD4yvs+62pMc37ObYO4E701e61Hp2bAtLQfM7IyIgAh36wYYlzV0U55xrMTLewd3S9OnUFoCKnE41K4sOgPULMlQi55zLPA+LOvp0trAojXSsWVl0AGz8DKp2ZKhUzjmXWR4WdexX1A6A9dquZmXnAwCFLxalPsg5577iPCzqKGyTzTrpyLSKnjUriw6wn94U5ZxrpTws6hLhvsEvcfcXw6mKJ2xdh/4QisC6+Zktm3POZYiHRQrH7N+Fsoo4s0o224pIlgXG+oWZLZhzzmWIh0UKw/friAi8t+iLmpWdD4D1XrNwzrVOHhYptG+TxZAehXywOCksig6ATct8RJRzrlXysKjHiAGd+GT5ZsoqYrai6ACbgdZHRDnnWiEPi3ocO6ATsYQyeekGW+EjopxzrZiHRT0O79ue3GiYifPX2oqOA0DCHhbOuVbJw6Ie2ZEwZxzcjXEzVllTVCTLahcrp2W6aM451+w8LHbjkiN7s60yzt9nBLfS6Pd1WD4JqsozWzDnnGtmHha7cWivdhzQtYBnJy9HVWG/4yBWDiVpv7WGc861KB4WuyEiXHpkb+auKmVWyRboM8L6LZa+k+miOedcs/KwaMC5h/YgLyvMn97/DHLaQo/DYenbmS6Wc841Kw+LBhTkRLlyRF/+MXOVTf+x33GwajqUb7F/FWWZLqJzzqWdh0UjXHNcfzq2yeLOV+ej/b5uF+dN/BXcNwQeP9Wv6nbOfeV5WDRCQU6UG04eyOTPNvLvsn4QyYWpT0BBd1g3F17/GSQSMPN5mPpnSDTL7cKdc67ZiKpmugz7RHFxsU6dOjVtz18VTzDq9++xZUcV/z56DgXhGIy4Ad68HT58ADrtD198ajv3PALOeQiK9k9beZxzbl8QkWmqWtzQfl6zaKRoOMSDlxzGtooY355/BBVH/xDCUTjxNug5zPouvvFHOO8x2LAEnv0WfEWC2DnnPCya4GtdC/i/bx3CJ8s38/OX59i1F5EsuPI1+OEcOPgCOORCOOV2m6F27Vw78IPfwx9P3DU8YpU1+wCsWwDPnO+d5s65FsfDoolGDenGD04eyNhpJdz9enAzpHAEQuGanQaeZj8Xvmb9F5MetmlCVs+s/WRv3g6Pfh22BVOhz/8HLJ4IJVPS/0acc64J0hoWIjJSRBaKyGIRuTnF9h+JyDwRmSUib4pIn6Rtd4vIXBGZLyL3i4iks6xNccNJA7n0yN48/PYSHnhzEbv0+xR0gR7F8Olrdk3G1tW2fuH4mn3K1sGUxyERg1UzbN2aIEzWzkn7e3DOuaZIW1iISBh4EBgFDAIuFpFBdXb7BChW1YOBscDdwbFHAyOAg4HBwBHAcekqa1OJCHecM5hzhnbn/974lGuemUZpeVXtnb420moTH9wHOe3sYr7ksPjwAYhX2OPVn9jPNbODnx4WzrmWJZ01i2HAYlVdqqqVwBjgnOQdVPUtVd0eLE4CelZvAnKALCAbiAJr01jWJguHhPsuHMqtZxzIm/PXcdYD7zN31ZaaHb52uv387F0YfD4MOtfCYPNya3aa8icY8i27t/eqGXaB36Zldkx1aDjnXAuRzrDoAaxIWi4J1tXnu8BrAKr6EfAWsDr497qq7nIDbBEZLSJTRWTq+vXr91nBG0tE+N6x+zFm9FFUVCU476EPeX7KctvYeRAU9rbHQy+pCY/ZY+Gl0XYh37E/ge5DrS+jujbRZQh8sRBiFc3+fpxzrj4tooNbRC4DioF7guUBwIFYTaMHcKKIHFv3OFV9TFWLVbW4qKioOYtcS3HfDvzz+mMY1rcDN704m5/8bSY7qhJw2LehzzHWBNVpgF2L8ebt1o9x9v12HUa3obBlRc18U0Mvtn6M9Qsz9n6cc66udIbFSqBX0nLPYF0tInIy8HPgbFWt/jp9HjBJVctUtQyrcQxPY1n3Wqf8bJ68ahjXnzSQF6eXcNYf3mdSr6vgylehum9+yAUQbQMXj7EgAatZAMz4K7QpggEn2/LaOVBeCh895ENpnXMZl86wmAIMFJF+IpIFXASMS95BRA4FHsWCYl3SpuXAcSISEZEo1rm9SzNUSxMOCT86ZX+eumoY5VVxLnpsEv/13CfMW1VqOxz7Y7hxMex/as1B3Q6xn6UroevBdvvWSK41S73zW3j9Fnjrv5v/zTjnXJK0hYWqxoDrgNexD/oXVHWuiNwhImcHu90D5AN/E5EZIlIdJmOBJcBsYCYwU1X/ka6y7mvHDizijR8ex3UnDODN+Ws5/f73uPzxyby3ZAMaza29c04hdNjPHncdYtdrdD4QlrwJH/8Rsgpg8iO1L96rpgqzXoAdm/a8sO//Dv5+LZSu2vPncM595fncUGm2ZXsVf/34c/7ywTLWba3goO5t+fnpB3L0gE41O/3tSpj7Epz/OAz5Joz7L5j+FISz4XsT4alzoNNAKP6uXbNx+Hcgtx3M/yc8fykcdS2MbKD2Me1JaNsdBp5Ssy4Rh7v72UisaBs443+tM94512r43FAtRGFelO8fP4D3bjqBu795MFt2VHHJnyZz+eOTeXbycko2bYceh9nO3YL+iy5D7Oew/4BuB8PJv4IVk+Hl0TDxl/Dqj+yD/q07bb8Zz0Dl9rovXaNsPfzzh/DsBTYzbrXVMy0oTvwFdBkEr93csu8vXlUO8VimS+FcqxTJdAFai+xImAuKe3H2Id358wfLePqjZfzsZbue4qBOA7ii/10clujKAIADzoCVU62PA6wzvNNAyOsIc1+Gt//H1q+bB0d8z67ZmPMiHHZ56hef9wpo3PpEXr7amrqGfLNmBNZh37bAevo8+PRfcNC5e/5GS6bB8g9h2NU2b1ZjrJ1n7y8c3f1+j58CvY60GlBr8flHsHoGHPWfmS6Ja+W8GSpDVJXF68p459P1vPPpeiYt3UBVXBm+X0dOHtSF4/YvYkDn/F0PjMfgiVPt6vAM3BPUAAAa10lEQVQug+Hqd+HhEfbBPPqdmpFXqjWPHz/VRlT9x5vwlzOtf+IHs+Cv37RpR77/kdVU7h1koXHxc01/Q6WrYOxVsPwjWz7ptpqw253Ny+H3h8BR34fT7qx/v61r4P++Bu37wg0z69+vvmM3fQ69j2zacS3BXy+w/qtbVkI0J9OlcV9B3gzVwokIA7sU8L1j9+Pp7x7JR7ecxI2nfY21W8v59T/ncfK973D679/jT+8tZeGarSQSQaiHI3Deo3bR32l3Wi3hiO9ak9LSt2yfldPsLn6v3Wwfkismw5DzIZoLx90EW1fBzOdg+STY73g7prq2sWgCbNsAy963CRA3fta4NzT5EZsA8bT/gf1Hwbv/C5tXNHzcogl258GPH7OyJqsos5tKQU0IbVoGW5t4Mf/EX8FTZ+++qa4lSiRgxaTgupsFmS6Na+W8ZtECrdi4nYnz1/LS9JXMXmlTiBTmRinu057ivh04om97hvQsJDsSzHRbXgoPDbcQGHIBzPs7hCJQuRWKDoT18+3bePu+9gH00FHWUV5RChc/b/NYgU0z8sgx0Hu4BQnB/42C7hCvtGG9Fz8HeR0sCEqmwOBvWC3mgcOgfT+4/CX70H9wGOw/Ei54cvdv9tkLYdUn1ncy6Bz4xmO2fuNSeOwEKL7S+mzG/xQ+ftS2XfA0DAoG1CXiFo55HaFj/12fXxXuPdDe7+UvQ/8T9/C3kgFr5sAjI+zx2X+ov5kxXV662oZ5Dz6/eV/XNavG1iy8z6IF6tUhjytH9OPKEf1YvmE7Hy/byNRlG5mybCNvLrDLUbIiIYb2bEdx3/Yc0a8Dh135NoXv/wam/cWuGL94DLx5B3zytN2cqX1fe/JQCIZ/H/5xA0gY+o6oeeGuQ6DzQfYtfuilMOIHNnPu+oUWPjOfg799B0bdbf0bW1dBfhcbmbVxKRx9vT1P+z7WBPXWnfD5h9Dn6JrXKF0Fr3wfTvqFvdbSd+xDMJpn9/0YeqmF1diroHwzTH8aTvi59YP0Hg4rp1tNadDZMPlReOdu2P6FTa1y/SdW80r2xaKaWX+XvlM7LFbPgml/hlH37HpcS1BdmwpFmn++sA1LYNYYq9F4WDg8LFq83h3z6N0xj28ebnMsbiirYOrnm5i6bCMfL9vEY+8u5aG3lyACPdufw1HdT6B9l770nVvOgYf8kiFtuhAZeFLtJz34Qnjz11ZTyC6ove28h2HLSjggmMsq+dawvYfDK9fYt92cdpDXCd69B3ofBYh1zFcbfp1dJ/LOb+Hbf69ZP+FWay7bsQlOvBViO2DgqXYr2tljrbmo6AD7kDrs2zaEeO4r9i37uJusprBisjVFTbgVuh8Gh15ms/vOe8Wa0pJ99o79LOxd87jav39tzWAHnAkD6pyjlmD5R1arK+zZ/GGx5N/2c/UMa/qr/rLhWi0Piy+ZjvnZnHZQV047qCsA2ytjzFixmWnLNvHpujLmrouydMpqyqtsZpVI6HD2nxtnSI9ZDOicT7d2OezXKZ+Bl75ENCdFB3q3Q2quKq9r6MWw6TOYOQYueR4+fd2G8q6ZbUGS37lm36w8GHG9faAvn2ydy8vet1FbPYpttNdrP4VIDvQ9xvpTrp1kU7d/+IBdO3Lyr+xakjduAxT6DLdw+egh+PB+iFfBuQ9Z89eCV23d4PNrOvbBAqKwl10/8s5vLaRy29s350UTbJ85L9UOi6pyuwnVgJObr1M5XmVNfVltbFnVRkL1GW7lnfm8NSGGmqmbcfFEyO0AOzbaTbmO/q/meV3XYnlYfMnlZUU4un8nju5fc5FfIqGs3LyDuatKmb1yM7NXljJh3hqen1pzz41oWOhckENeVglFBdkM6JxP/6J8BnTOp0e7XNrmRinMjRIO1bnn1Ak/g+NvsQ/kwp52Bfj2L2DQT3YtXPFV8P59NtT3xFut36GwF1wxDv58un1rHXiqBQVYLeeEn9lsvOGovcbg82HKH60ppucRULnNmqsmPQQHnlnTT3H0dda0Nu/vNqNvbnt77s/es5rDfsfBO3dZYB14ljVhhaK2fv4/4Mx7IZJtH9L//IE1uXUcAGfeB/12mcPSPtwbGurbWBVl8MRIe7+j37FA2Py5NfP1Hm6vM+VPtq5Dv33zmrsTq7Cp9YdeCiUf2zn1sGj1PCy+gkIhoVeHPHp1yGPk4K4715eWV7Fy0w4Wrytj3upS1pVWsK0ixprScl6evpKtFbUveMuKhOhflM9+RW3o2jaHboU5dGmbQ9fCHLq2zaFz2zyyj74O3r7LPpDrympjHzITf2lNTxKCC5+x9af9N/zl9Jqp25MlX59x8IUWFt0OseN6BcNfNVHTRwJw8EXw7zvhb1fUXle+2QKhR7H1iyx9B/odZxM3Dj7f7imyeKL9O+AM68OY+Zwdu2ISPHkmHHo5nPRL22fqE/DFp1BZBqN+a9e5qFoTWJ9jIL+Jsx8nEvDKf8LaoJnp039ZE+DnQX9F7+E1N8laM9vCduU0e1+hCPQZsWvtR9XC5YP74Vt/gZ6HN61Myz+Cqu1Ws2rbzfq+tpTYl4N9pTlrSV9Wq2bYOW/TqeF9m4GHRSvSNidK225RDuzWlrMO6V5rm6qybmsFi9eVsWZLOVvLq1i9pZxP125l3qpS/j1/HTuq4rs8Z8e8gxmS/wjy8mq6Fm6yMGmbQ4c2WXTMz6JD/8voGg8R7tCHaO9ipDC4pUnfEXDtx/btfXd6FtuH+/7Bfc3bdLJhwzmF0GtYzX7RHDjnQWveGniaDcWdNSZ4rWMtgPocbXNpffq6fdgfOdouVMztADOetQ/ECbdC/5OseStWYU1XHz4AnzwDqI0uG3y+9am8dpN10s9+wUKk93D4zqu178de+yRbH8yGxTYIIFZpH8zzx8HJt8PUx63vZeApMPNZe4+dB1lYSMiGR88cAwtfrXnOrAK7iHLUby1MYxV2hf8nz1iYvPQfcM17Nc1bjbF4IoSzrHmw4wALizkvWbNirBLGXmk1nFN/0/jnrJaIw/if2P3pr36vdriq2u+goNveDThIJKx2+LVR9u/LaMcmeOI0qwWf/6fU+yTi9v+ime447WHhALvuo0tbqzmkoqqUlsdYW1rOmi3lrEn6uXZLB9aUljN75Ra+KKtMcbQ1FYVkBj3bf0rfTm3Izw4TDYdolzufjvnZdMzPomObLNrnZdEuL4tu7XJomxM0RV0xrvbTXfaSNRnVtf+pNTP6dn/YgqVsrX07BqshbFlpV4sf91MbNQY2ZHfan2HBP6H30fCNP9oHflYenHK7dZpPf8q+aQ881cq0YzM8djw8eRYkqmC/E6z29P69Nnz5w/vtYkCwb/+Hfds+dD9+1D7EE0EtLqed9c+MuMFqPq/dCE+dC5+/b01goRCEcu1eKJMesm/8x98CA06xD5R5L1stafPnVu6x37Vjv/5T+7B/6hx4/Wcw8i7rE1n2AXz+gT1PIm6j08rWWpNh8ZXWhLfwXxZ82fmQPcDC9q07LbjnvmznCeCg8+wcLnrD7v548AU1Qbljsw1wKN9sQRiOWNPdS6NtHjSAd++G0++p+f1NfRxe/bHNidbtYAuj3kfV/h2vX2gj/Ba+ZrW96iHUyea9AtOfhGXv2e8rFLZrhjoOhIHBLQDKS+33kJWX4v9rPZqzNjR7LMTKYcF4uz4oVTmfvdB+p5e/XP8XlH3Ir7Nw+1RlLMH6sgo2llWyYVsFG7dVsml7FeVVcbZXxvh8w3aWb9zOjso4lfEEm7dXsWVHVcrnKsyNUpATIRoOEQkJ4ZDQJjtC25wIhUGfSnXfStucpMe5kZ3bCrIjSEPfvDYssb6XoZfUHubbkDVz4Olz7YP2+Fvgxe/Zh2kobN/4Og6wP/gNi60jP1Zuo8ROucOCJJxlgVZdvsrtcN9g2L4BjrsZTril5rVe/B7M/puFzln31/42OfN5m8YlnGXNc+c+DAd/y7ZNuNVqRskiOZCVb2Us6AqoNXEdfKENTd6wCM57DA650PbftsG+5W4psQEGxVfZwIMO/ayZ8YUraqaTGfwNWP+pDTioCG4zPORb9sH+8tUWVCffbiOsPnk6qF32t/nLHjjcRt/1OtJqW1tK4Jgf2kwF2zdYrbDkY/uQb1NkgXTVv2ruCQM2w8FDR9r5rSyza3KyC+z3lFVgsxVE8yzow1G46vWGmw4TcRh3vQ2W+O4bNV8+0unR42w4ekUpXPCUfaFJtnyS/U7ALoQd/v09fqnGXmfhYeEyrjKWYNP2StZvrWDLjio2bqtk9ZYdLN+4ne0VcaoSSjyRoCqubK+MsWWHBUzpjhil5VXs7r9wSKBtECbJQZKXZZXqaFgoKsihqCCbNllh8rLC5GZF7Ge0ejlMXjRCXlAbqiV5WpUdm+3bXtH+9mFf3eS2fDJ89Af7Zn709btvNljwqoXX0f9Ve7+lb9sQ4lF3p55za/rTVqs56/fQ7+s162OVMOt5G4SgCRsk0Ouo2s+RiNsw4vd/Z30i5/yh5sr+apuXwxOj7I6Pl75o/TrjrgPEpogZNtpqTqUr7dqbPiPsg37xRLs7ZChqYXbm7yyEtq6B+w+1617Oe9RGxs16Af7zQzt/5aXWXDUraeLLogOsdnjwhYDCH0+0sh/zA2tm63ygtfO/+iP7gJ3wC7tYs6LUzsP2L6zGhNpABwnba536G3udrWusBrffCTU11ETcrguaNcbeQ88j4Ip/NNxMtmOz1QRXz7JaX/t+FmqDz68ZlFGx1YJ1ywo737ntbH31xZin/bf9TvqMsItbK7fbOQxH4LmLLTC6D7X+re9/WHOrgybysHCtQiKhbK2IUbozQKooLa+qFShbdllXxfbKOAJUxpUN2yp2GzjJomEJQiRCOCREwkK7vCyK8rPJzQoTFhtgEAkJeVmRIKgsoHKzwmSFQ2RF7F92JERWOExWJEQkLORnR+jQJotISCiriFEVV/KzI2RFmqnpY/VM+1DLaZt6e1W5fViFQvYh+sRIa8664h92VX+s0r7N53Wofdx798LiNy0okq/befu38PZ/24dwosouAj3l9trHblxqzVeRbGjXp3aArpkNT55tw3uT9Si2qf2n/MkCByzgNi6xUAIL1YJu9qGrcatpdegHXyy22tMhF8Ogc60PaflHdmFo+37w0vfgkEtq+styCm3q/55H1DQFbfvCajJr51rAtettXwA2LMaGgB9jNaX1C9g5S0KXwfDtcdCmI/zrFiv7jxda898nf4XLXrS+ouy2cPzN8OJ37QvJYd+2GRm6HWLH70EzmYeFc40UiyfYuK2S7ZVxtlfG2VEVq3kc/NxeGbPHVXG2V9j2uCqxuO6sFVXGEsRViSds/bbKGFvLmz6lejgkxBM1f5fZkRAFORHysyPk50TIy4qQHQkRDYeIhoWsSJhoWMiOhMjPtu0KoEphXhbt86JkB/tEIyGywjXHRoPw2vlc1dsiwfZQiFDd4dM7T1ylfUDuaXu5qvXzLH3bvtWfca/1kzRFvMpqIRVbrFaxarqNZOs62L6J3z/Umha/9Rfrc3jxKhthdMqvLXgWTbQhygedZ81V8Sq70PTde6wmVtAdjr/J7iEDtaedSZbf1TrTo7l2/c6WlXDRMzW3SQa7kHTaX6ypsrCn1TS7DLZ+h1f+02oGnQdZn9D+p1ntaNkHNmqQYKh6ImYzEkRy4YdzrBlz5hgr6yEX71Fnt4eFcy1APKGUBTWfHVVxKmMJKmIJKmMJKuMJKqriVMWVWCLB1vIYX5RZ6LTPyyISFrZVxNhaYaFTVh6jrML+xeLWLFcVt+epiicor0pQVh5LOWptb0RCkhRM1cFSE1RZYalZFwnVXg6HyIrUWa7eHqmz3OjjQ0ST1mUFZQmHZNf+qe0brdbQ2Onyq636xCbRPOCMXQdTVN9VUtWauNYvsA7pz9619bnt4NxHak+l05Alb1ktJ5prr3n8LdaMmYjDH4qtme3SsVazm/AL6HLQXvVTJPOwcK6VSiSUUEisia48xqbtlVTGLaCq6oZMbNfQqV63czk4pub4pO2xOss7n6POc8aVqiAgK+OJRjf7NYUItcKjJmzqLNcTNiEREqokFBKqZEVCdMrPJj87QjwR1BgTiqqd32g4RG40TJts69+yZkghFJLgJ4TEQiwsFmThkBAO2f1tqvvDciJhYgmlsmwDkl1AVlbWznJFwkIktg2J5qVtxJNPJOhcK1XdbBQKCYV5UQrz9tGV5vtQPKE7a1fJAVM7oBJUBqGzczkInVrLSaG1c7mB4yuCWljy/vGEEg5ZaIhARZWN7KuM2TT5NR/6FiZV8eb7oh0J+seioRDhsBAJWcBVrzuoRyEPXHxoesuQ1md3zrkUwiEhNytMLum/PmBvqFptIpKiiSuRUMpjNX1bO6riO2sgquzsv0qokkgocVUSCYglrCmyvKrmuEhIyI6EgxCyUKuMJay5MaHE4gliCd0ZalXx2ut6d8hN+7nwsHDOuXqICNFw6k7jUDDirXoY9ledT87inHOuQWkNCxEZKSILRWSxiNycYvuPRGSeiMwSkTdFpE/Stt4iMkFE5gf79E1nWZ1zztUvbWEhImHgQWAUMAi4WEQG1dntE6BYVQ8GxgJ3J217CrhHVQ8EhgHr0lVW55xzu5fOmsUwYLGqLlXVSmAMUGuCE1V9S1W3B4uTgJ4AQahEVPWNYL+ypP2cc841s3SGRQ9gRdJySbCuPt8FXgse7w9sFpGXROQTEbknqKnUIiKjRWSqiExdv379Piu4c8652lpEB7eIXAYUA9XzFUeAY4GfAEcA+wHfqXucqj6mqsWqWlxU1MSbzjjnnGu0dIbFSqBX0nLPYF0tInIy8HPgbFUNbglGCTAjaMKKAa8Ah6WxrM4553YjnWExBRgoIv1EJAu4CKh1FxsRORR4FAuKdXWObSci1dWFE4F5aSyrc8653Ujr3FAicjpwHxAGnlDVO0XkDmCqqo4TkYnAEGB1cMhyVT07OPYU4P8AAaYBo4OO8vpeaz3w+V4UtxPwxV4c3xxaehlbevnAy7iveBn3jZZQxj6q2mA7/ldmIsG9JSJTGzOZVia19DK29PKBl3Ff8TLuG1+GMlZrER3czjnnWjYPC+eccw3ysKjxWKYL0AgtvYwtvXzgZdxXvIz7xpehjID3WTjnnGsEr1k455xrkIeFc865BrX6sGhoGvVMEJFeIvJWMDX7XBG5IVjfQUTeEJFFwc/2LaCs4WD+rn8Gy/1EZHJwPp8PLsjMZPnaichYEVkQTHc/vCWdRxH5YfA7niMiz4lITks4hyLyhIisE5E5SetSnjcx9wflnSUiaZ9toZ7y3RP8nmeJyMsi0i5p2y1B+RaKyGnpLl99ZUza9mMRURHpFCw3+zlsqlYdFo2cRj0TYsCPVXUQcBRwbVCum4E3VXUg8GawnGk3APOTln8L/E5VBwCbsAkiM+n3wL9U9QDgEKysLeI8ikgP4Hpsmv7B2MWrF9EyzuFfgJF11tV33kYBA4N/o4GHM1S+N4DBwS0PPgVugZ2zWF8EHBQc81CqiUmbqYyISC/gVGB50upMnMMmadVhQSOmUc8EVV2tqtODx1uxD7geWNmeDHZ7Ejg3MyU0ItITOAP4U7As2NQsY4NdMlpGESkEvg48DqCqlaq6mZZ1HiNArohEgDxsNoOMn0NVfRfYWGd1feftHOApNZOwqXq6NXf5VHVCMJccJN3yICjfGFWtUNXPgMXY335a1XMOAX4H/BRIHl3U7OewqVp7WDR1GvVmJ3aHwEOByUAXVa2eGmUN0CVDxap2H/afPhEsdwQ2J/3BZvp89gPWA38Omsr+JCJtaCHnUVVXAv+LfcNcDWzBprZpSecwWX3nrSX+HV1FzS0PWkz5ROQcYKWqzqyzqcWUsT6tPSxaNBHJB14EfqCqpcnb1MY8Z2zcs4icCaxT1WmZKkMjRLDZih9W1UOBbdRpcsrkeQza/M/BQq070IYUzRYtUab//+2OiPwca8r9a6bLkkxE8oCfAbdluix7orWHRaOmUc8EEYliQfFXVX0pWL22umoa/MzkrWZHAGeLyDKs+e5ErH+gXdCkApk/nyVAiapODpbHYuHRUs7jycBnqrpeVauAl7Dz2pLOYbL6zluL+TsSke8AZwKXas1FZC2lfP2xLwYzg7+bnsB0EelKyyljvVp7WDQ4jXomBG3/jwPzVfXepE3jgCuCx1cAf2/uslVT1VtUtaeq9sXO279V9VLgLeCbwW6ZLuMaYIWIfC1YdRI21X1LOY/LgaNEJC/4nVeXr8WcwzrqO2/jgG8HI3qOArYkNVc1GxEZiTWLnl3nNszjgItEJFtE+mGdyB83d/lUdbaqdlbVvsHfTQlwWPD/tEWcw91S1Vb9DzgdGzmxBPh5pssTlOkYrIo/C5gR/Dsd6xN4E1gETAQ6ZLqsQXmPB/4ZPN4P+0NcDPwNyM5w2YYCU4Nz+QrQviWdR+B2YAEwB3gayG4J5xB4DutHqcI+1L5b33nDbiPwYPA3NBsb3ZWJ8i3G2v2r/2YeSdr/50H5FgKjMnUO62xfBnTK1Dls6j+f7sM551yDWnszlHPOuUbwsHDOOdcgDwvnnHMN8rBwzjnXIA8L55xzDfKwcK4FEJHjJZi517mWyMPCOedcgzwsnGsCEblMRD4WkRki8qjY/TzKROR3wX0p3hSRomDfoSIyKen+CtX3fxggIhNFZKaITBeR/sHT50vNvTf+GlzV7VyL4GHhXCOJyIHAhcAIVR0KxIFLsQkAp6rqQcA7wC+DQ54CblK7v8LspPV/BR5U1UOAo7GrfMFmF/4Bdm+V/bB5opxrESIN7+KcC5wEHA5MCb7052KT6SWA54N9ngFeCu6l0U5V3wnWPwn8TUQKgB6q+jKAqpYDBM/3saqWBMszgL7A++l/W841zMPCucYT4ElVvaXWSpFf1NlvT+fQqUh6HMf/Pl0L4s1QzjXem8A3RaQz7LwndR/s76h6lthLgPdVdQuwSUSODdZfDryjdufDEhE5N3iO7OA+B861aP7NxblGUtV5InIrMEFEQthsotdiN1UaFmxbh/VrgE3j/UgQBkuBK4P1lwOPisgdwXN8qxnfhnN7xGeddW4viUiZquZnuhzOpZM3QznnnGuQ1yycc841yGsWzjnnGuRh4ZxzrkEeFs455xrkYeGcc65BHhbOOeca9P9MOPGN8pdFZgAAAABJRU5ErkJggg==
{{< /png >}}

We find the lowest validation loss now is 0.265, significantly lower than the 
previous best value of 0.277. We will first load the saved best model weights, 
and then plot the original and the reconstructed images from the test dataset.

{{< highlight lang="python" linenos="yes" >}}
autoencoder.load_weights('weights-ae-146-0.266.hdf5')
decoded_imgs = autoencoder.predict(x_test)
display_reconstructed(x_test, decoded_imgs, 10)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/ae_conv_fm.png" alt="sample images" class="figure img-responsive align-center" >}}

At first glance, it seems not much of improvement over the deep autoencoders 
result. However, if you notice closely, we start to see small feature 
details to appear on the reconstructed images. In order to 
improve these models further, we will likely have to go for deeper and more 
complex convolution network.

# Denoising Autoencoders

Another common variant of AE networks is the one that learns to remove noise
from the input. Mathematically, this is achieved by modifying the 
reconstruction error of the loss function.

Traditionally, autoencoders minimize some loss function:
{{< tex display="L\Big(x, g\big(f(x)\big)\Big)" >}}

where, $L$ is a loss function penalizing reconstructed input $g\big(f(x)\big)$ 
for being dissimilar to the input $x$. Also, $g(.)$ is the decoder and $f(.)$ 
is the encoder. A Denoising autoencoders (DAE) instead minimizes,
{{< tex display="L\Big(x, g\big(f(\hat{x})\big)\Big)" >}}

where, $\hat{x}$ is a copy of $x$ that has been corrupted by some form of 
noise. DAEs must therefore undo this corruption rather than simply copying 
their input. Training of DAEs forces $f(.)$, the encoder and $g(.)$, the 
decoder to implicitly learn the structure of {{< tex "p_{data}(x)," >}} the 
distribution of the input data $x$. Please refer to the works of
[Alain and Bengio (2013)][ref1] and [Bengio et al. (2013)][ref2].

[ref1]: https://arxiv.org/abs/1211.4246
[ref2]: https://arxiv.org/abs/1305.6663

For a example, we will first introduce noise to our train and test data by 
applying a guassian noise matrix and clipping the images between 0 and 1.

{{< highlight lang="python" linenos="yes" >}}
(x_train, _), (x_test, _) = fashion_mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = np.reshape(x_train, (len(x_train), 28, 28, 1))
x_test = np.reshape(x_test, (len(x_test), 28, 28, 1))

noise_factor = 0.5
x_train_noisy = x_train + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_train.shape) 
x_test_noisy = x_test + noise_factor * np.random.normal(loc=0.0, scale=1.0, size=x_test.shape) 

x_train_noisy = np.clip(x_train_noisy, 0., 1.)
x_test_noisy = np.clip(x_test_noisy, 0., 1.)
{{< /highlight >}}

Here is how the corrupted images look now. They are barely recognizable now!

{{< highlight lang="python" linenos="yes" >}}
display_reconstructed(x_test_noisy, None)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/ae_noisy_sample.png" alt="sample images" class="figure img-responsive align-center" >}}

We will use a slightly modified version of the previous convolution 
autoencoder, the one with larger number of filters in the intermediate
layers. This increases the capacity of our model.

{{< highlight lang="python" linenos="yes" >}}
input_img = Input(shape=(28, 28, 1))

x = Conv2D(32, (3, 3), activation='relu', padding='same', use_bias=False)(input_img)
x = BatchNormalization(axis=-1)(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
x = MaxPooling2D((2, 2), padding='same')(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
encoded = MaxPooling2D((2, 2), padding='same')(x)

x = Conv2D(32, (3, 3), activation='relu', padding='same', use_bias=False)(encoded)
x = BatchNormalization(axis=-1)(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(32, (3, 3), activation='relu', padding='same', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
x = UpSampling2D((2, 2))(x)
x = Conv2D(32, (3, 3), activation='relu', padding='valid', use_bias=False)(x)
x = BatchNormalization(axis=-1)(x)
x = UpSampling2D((2, 2))(x)
decoded = Conv2D(1, (3, 3), activation='sigmoid', padding='same', use_bias=False)(x)

autoencoder = Model(input_img, decoded)
autoencoder.compile(optimizer='rmsprop', loss='binary_crossentropy')
{{< /highlight >}}

We can now train this for 150 epochs. Notice the change in the training data!

{{< highlight lang="python" linenos="yes" >}}
fpath = "weights-dae-{epoch:02d}-{val_loss:.3f}.hdf5"
callbacks = [ModelCheckpoint(fpath, monitor='val_loss', verbose=1, save_best_only=True, mode='min')]
history = autoencoder.fit(x_train_noisy, x_train,
                epochs=150,
                batch_size=256,
                shuffle=True,
                validation_data=(x_test_noisy, x_test),
                callbacks=callbacks)

plot_train_history_loss(history)
{{< /highlight >}}


The loss has converged to a value of 0.287. Let's take a look at the results, 
top row are noisy images and the bottom row are the reconstructed images from 
the DAE.

{{< png >}}
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
{{< /png >}}

{{< highlight lang="python" linenos="yes" >}}
autoencoder.load_weights('weights-dae-146-0.287.hdf5')
decoded_imgs = autoencoder.predict(x_test_noisy)
display_reconstructed(x_test_noisy, decoded_imgs, 10)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/dae_conv_fm.png" alt="sample images" class="figure img-responsive align-center" >}}

{{< card "" "Sequence-to-Sequence Autoencoders" >}}
If your inputs are sequences, rather than 2D images, then you may 
want to use as encoder and decoder a type of model that can capture temporal 
structure, such as a [LSTM]. To build a LSTM-based auto-encoder, first use a 
[LSTM] encoder to turn your input sequences into a single vector that contains 
information about the entire sequence, then repeat this vector $n$ times (
where $n$ is the number of time steps in the output sequence), and run a [LSTM]
decoder to turn this constant sequence into the target sequence.

[LSTM]: https://towardsdatascience.com/recurrent-neural-networks-and-lstm-4b601dd822a5
{{< /card >}}

# Variational Autoencoders (VAE)

{{< figure src="../../images/autoencoders/vae.png" alt="VAE network" class="figure img-responsive align-right" >}}

Variational autoencoders (VAE) are stochastic version of the regular 
autoencoders. It's a type of autoencoder with added constraints on the encoded 
representations being learned. More precisely, it is an autoencoder that 
learns a [latent variable model][lvm] for its input data. So instead of 
letting your neural network learn an arbitrary function, you are learning the 
parameters of a probability distribution modeling your data. If you sample 
points from this distribution, you can generate new input data samples: a VAE 
is a "generative model". The cartoon on the side shows a typical architecture of a VAE model. Please refer to the research papers by
[Kingma et al.][vae_ref1] and [Rezende et al.][vae_ref2] for a
thorough mathematical analysis.

In the probability model framework, a variational autoencoder contains a 
specific probability model of data $x$ and latent variables $z$
(most commonly assumed as Guassian). We can write the joint 
probability of the model as $p(x, z) = p(x \vert z)p(z)$. The generative 
process can be written as, for each data point $i$:

- Draw latent variables {{< tex "z_i \sim p(z)" >}}
- Draw data point {{< tex "x_i \sim p(x\vert z)" >}}

In terms of an implementation of VAE, the latent variables
are generated by the encoder and
the data points are drawn by the decoder. The latent variable hence is a 
random variable drawn from a posterior distribution, $p(z)$. To implement the 
encoder and the decoder as a neural network, you need to backpropogate 
through random sampling and that is a problem because backpropogation cannot 
flow through a random node. To overcome this,
the **reparameterization trick** is used. Most commonly, the true posterior 
distribution for the latent space is assumed to be Guassian. Since our 
posterior is normally distributed, we can approximate it with another normal 
distribution, $\mathcal{N}(0, 1)$.

$$p(z) \sim \mu + L \mathcal{N}(0, 1)$$

Here $\mu$ and $L$ are the output of the encoder. Therefore while backpropogation, all we need is partial derivatives w.r.t. $\mu$, $L$. In
the cartoon above, $\mu$ represents the mean vector latent variable and $L$ represents the standard deviation latent variable.

You can read more about VAE models at [_**Reference 1**_][vae1],
[_**Reference 2**_][vae2], [_**Reference 3**_][vae3] and [_**Reference 4**_][vae].

In more practical terms, VAEs represent latent space (bottleneck layer) as a 
Guassian random variable (enabled by a constraint on the loss function). Hence, the loss function for the VAEs consist of two terms: a reconstruction loss forcing the decoded samples to match the initial inputs (just like in our previous autoencoders), and the KL divergence between the learned latent distribution and the prior distribution, acting as a regularization term.

{{< tex display="\min \mathcal{L}(x, x') = \min E(x, x') + KL\big(q(z\vert x)\vert \vert p(z)\big)" >}}

Here, the first term is the reconstruction loss as before (in a typical 
auto-encoder). The second term is the [Kullback-Leibler divergence][kl]
between the encoder’s distribution, $q(z\vert x)$ and the true posterior
$p(z)$, typically a Guassian.

As typically (especially for images) the binary [cross-entropy][ce] is
used as the reconstruction loss term, the above loss term for the VAEs can be 
written as,

{{< tex display="\min \mathcal{L}(x, x') = \min -\mathbf{E}_{z\sim q(z\vert x)}\big[ \log p(x' \vert z)\big] + KL\big(q(z\vert x)\vert \vert p(z)\big)" >}}


[lvm]: https://en.wikipedia.org/wiki/Latent_variable_model
[vae]: https://ermongroup.github.io/cs228-notes/extras/vae/
[vae1]: http://kvfrans.com/variational-autoencoders-explained/
[vae2]: https://wiseodd.github.io/techblog/2016/12/10/variational-autoencoder/
[vae3]: https://jaan.io/what-is-variational-autoencoder-vae-tutorial/
[vae_ref1]: https://arxiv.org/pdf/1312.6114.pdf
[vae_ref2]: https://arxiv.org/abs/1401.4082
[kl]: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
[ce]: https://en.wikipedia.org/wiki/Cross_entropy

To summarize a typical implementation of a VAE, first, an encoder network 
turns the input samples $x$ into two parameters in a latent space, `z_mean` 
and `z_log_sigma`. Then, we randomly sample similar points $z$ from the latent 
normal distribution that is assumed to generate the  data, via
$z$ = `z_mean` + `exp(z_log_sigma)` * $\mathbf{\epsilon}$,
where $\mathbf{\epsilon}$ is a random normal tensor. Finally, a decoder 
network maps these latent space points back to the original input data.

We can now implement VAE for the fashion MNIST data. To demonstrate its generalization, we will generate two versions: one with MLP and the other with the use of convolution and deconvolution layers.

In the first implementation below, we will be using a simple 2-layer deep 
encoder and a 2-layer deep decoder. Note the use of the reparameterization trick via the `sampling()` method and a `Lambda` layer.

{{< highlight lang="python" linenos="yes" >}}
from scipy.stats import norm

from keras.layers import Input, Dense, Lambda, Flatten, Reshape
from keras.layers import Conv2D, Conv2DTranspose
from keras.models import Model
from keras import backend as K
from keras import metrics

batch_size = 128
original_dim = 784
latent_dim = 2
intermediate_dim = 256
epochs = 100
epsilon_std = 1.0


x = Input(shape=(original_dim,))
h = Dense(intermediate_dim, activation='relu')(x)
z_mean = Dense(latent_dim)(h)
z_log_var = Dense(latent_dim)(h)


def sampling(args):
    z_mean, z_log_var = args
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim), mean=0.,
                              stddev=epsilon_std)
    return z_mean + K.exp(z_log_var / 2) * epsilon

# note that "output_shape" isn't necessary with the TensorFlow backend
z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])

# to reuse these later
decoder_h = Dense(intermediate_dim, activation='relu')
decoder_mean = Dense(original_dim, activation='sigmoid')
h_decoded = decoder_h(z)
x_decoded_mean = decoder_mean(h_decoded)

# instantiate VAE model
vae = Model(x, x_decoded_mean)
{{< /highlight >}}

As described above, we need to include two loss terms, binary cross entropy as 
before and the KL divergence between the encoder latent variable distribution
(calculated using the reparameterization trick) and the true posterior 
distribution, a normal distribution!

{{< highlight lang="python" linenos="yes" >}}
# Compute VAE loss
xent_loss = original_dim * metrics.binary_crossentropy(x, x_decoded_mean)
kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
vae_loss = K.mean(xent_loss + kl_loss)

vae.add_loss(vae_loss)
vae.compile(optimizer='rmsprop')
{{< /highlight >}}

we can now load the fashion MNIST dataset, normalize it and reshape it to 
correct dimensions so that it can be used with our VAE model.

{{< highlight lang="python" linenos="yes" >}}
# train the VAE on fashion MNIST images
(x_train, y_train), (x_test, y_test) = fashion_mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_test = x_test.astype('float32') / 255.
x_train = x_train.reshape((len(x_train), np.prod(x_train.shape[1:])))
x_test = x_test.reshape((len(x_test), np.prod(x_test.shape[1:])))
{{< /highlight >}}

We will now train our model for 100 epochs.

{{< highlight lang="python" linenos="yes" >}}
history = vae.fit(x_train,
        shuffle=True,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(x_test, None))

plot_train_history_loss(history)
{{< /highlight >}}

Below is the loss for the training and the validation datasets during training 
epochs. We find that loss has converged in 100 epochs without any sign of over 
fitting.

{{< figure src="../../images/autoencoders/vae_fc_hist.png" alt="VAE network" class="figure img-responsive align-center" >}}

Because our latent space is two-dimensional, there are a few cool visualizations that can be done at this point. One is to look at the neighborhoods of different classes on the latent 2D plane:

{{< highlight lang="python" linenos="yes" >}}
# build a model to project inputs on the latent space
encoder = Model(x, z_mean)

# display a 2D plot of the digit classes in the latent space
def plot_latentSpace(encoder, x_test, y_test, batch_size):
    x_test_encoded = encoder.predict(x_test, batch_size=batch_size)
    plt.figure(figsize=(6, 6))
    plt.scatter(x_test_encoded[:, 0], x_test_encoded[:, 1], c=y_test, cmap='tab10')
    plt.colorbar()
    plt.show()

plot_latentSpace(encoder, x_test, y_test, batch_size)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/vae_fc_latent.png" alt="VAE network" class="figure img-responsive align-center" >}}

Each of these colored clusters is a type of the fashion item. Close clusters 
are items that are structurally similar (i.e. items that share information in 
the latent space). We cal also look at this plot from a different perspective: 
the better our VAE model, the separation between very dissimilar fashion items 
would be larger among their clusters!

Because the VAE is a generative model (as described above), we can also use it 
to generate new images! Here, we will scan the latent plane, sampling latent 
points at regular intervals, and generating the corresponding image for each 
of these points. This gives us a visualization of the latent manifold that 
"generates" the fashion MNIST images.

{{< highlight lang="python" linenos="yes" >}}
# generator that can sample from the learned distribution
decoder_input = Input(shape=(latent_dim,))
_h_decoded = decoder_h(decoder_input)
_x_decoded_mean = decoder_mean(_h_decoded)
generator = Model(decoder_input, _x_decoded_mean)

def plot_generatedImages(generator):
    # D manifold of the fashion images
    n = 15  # figure with 15x15 images
    image_size = 28
    figure = np.zeros((image_size * n, image_size * n))
    # linearly spaced coordinates on the unit square were transformed through the # inverse CDF (ppf) of the Gaussian
    # to produce values of the latent variables z, since the prior of the latent
    # space is Gaussian
    grid_x = norm.ppf(np.linspace(0.005, 0.995, n))
    grid_y = norm.ppf(np.linspace(0.005, 0.995, n))

    for i, yi in enumerate(grid_x):
        for j, xi in enumerate(grid_y):
            z_sample = np.array([[xi, yi]])
            x_decoded = generator.predict(z_sample)
            digit = x_decoded[0].reshape(image_size, image_size)
            figure[i * image_size: (i + 1) * image_size,
                   j * image_size: (j + 1) * image_size] = digit

    plt.figure(figsize=(10, 10))
    plt.imshow(figure, cmap='Greys_r')
    plt.show()

plot_generatedImages(generator)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/vae_fc_gen.png" alt="VAE network" class="figure img-responsive align-center" >}}

We find our model has done only a so-so job in generating new images. Still, 
given the simplicity and very small amount of simple code we had to write, 
this is still quite incredible.

We can next build a more realistic VAE using  `conv` and `deconv` layers.
Below is the full code to build and train the model. 

{{< highlight lang="python" linenos="yes" >}}
# input image dimensions
img_rows, img_cols, img_chns = 28, 28, 1
# number of convolutional filters to use
filters = 64
# convolution kernel size
num_conv = 3

batch_size = 128
if K.image_data_format() == 'channels_first':
    original_img_size = (img_chns, img_rows, img_cols)
else:
    original_img_size = (img_rows, img_cols, img_chns)
latent_dim = 2
intermediate_dim = 128
epsilon_std = 1.0
epochs = 150

x = Input(shape=original_img_size)
conv_1 = Conv2D(img_chns,
                kernel_size=(2, 2),
                padding='same', activation='relu')(x)
conv_2 = Conv2D(filters,
                kernel_size=(2, 2),
                padding='same', activation='relu',
                strides=(2, 2))(conv_1)
conv_3 = Conv2D(filters,
                kernel_size=num_conv,
                padding='same', activation='relu',
                strides=1)(conv_2)
conv_4 = Conv2D(filters,
                kernel_size=num_conv,
                padding='same', activation='relu',
                strides=1)(conv_3)
flat = Flatten()(conv_4)
hidden = Dense(intermediate_dim, activation='relu')(flat)

z_mean = Dense(latent_dim)(hidden)
z_log_var = Dense(latent_dim)(hidden)


def sampling(args):
    z_mean, z_log_var = args
    epsilon = K.random_normal(shape=(K.shape(z_mean)[0], latent_dim),
                              mean=0., stddev=epsilon_std)
    return z_mean + K.exp(z_log_var) * epsilon

# note that "output_shape" isn't necessary with the TensorFlow backend
# so you could write `Lambda(sampling)([z_mean, z_log_var])`
z = Lambda(sampling, output_shape=(latent_dim,))([z_mean, z_log_var])

# we instantiate these layers separately so as to reuse them later
decoder_hid = Dense(intermediate_dim, activation='relu')
decoder_upsample = Dense(filters * 14 * 14, activation='relu')

if K.image_data_format() == 'channels_first':
    output_shape = (batch_size, filters, 14, 14)
else:
    output_shape = (batch_size, 14, 14, filters)

decoder_reshape = Reshape(output_shape[1:])
decoder_deconv_1 = Conv2DTranspose(filters,
                                   kernel_size=num_conv,
                                   padding='same',
                                   strides=1,
                                   activation='relu')
decoder_deconv_2 = Conv2DTranspose(filters,
                                   kernel_size=num_conv,
                                   padding='same',
                                   strides=1,
                                   activation='relu')
if K.image_data_format() == 'channels_first':
    output_shape = (batch_size, filters, 29, 29)
else:
    output_shape = (batch_size, 29, 29, filters)
decoder_deconv_3_upsamp = Conv2DTranspose(filters,
                                          kernel_size=(3, 3),
                                          strides=(2, 2),
                                          padding='valid',
                                          activation='relu')
decoder_mean_squash = Conv2D(img_chns,
                             kernel_size=2,
                             padding='valid',
                             activation='sigmoid')

hid_decoded = decoder_hid(z)
up_decoded = decoder_upsample(hid_decoded)
reshape_decoded = decoder_reshape(up_decoded)
deconv_1_decoded = decoder_deconv_1(reshape_decoded)
deconv_2_decoded = decoder_deconv_2(deconv_1_decoded)
x_decoded_relu = decoder_deconv_3_upsamp(deconv_2_decoded)
x_decoded_mean_squash = decoder_mean_squash(x_decoded_relu)

# instantiate VAE model
vae = Model(x, x_decoded_mean_squash)

# define the loss function
xent_loss = img_rows * img_cols * metrics.binary_crossentropy(
    K.flatten(x),
    K.flatten(x_decoded_mean_squash))
kl_loss = - 0.5 * K.sum(1 + z_log_var - K.square(z_mean) - K.exp(z_log_var), axis=-1)
vae_loss = K.mean(xent_loss + kl_loss)
vae.add_loss(vae_loss)

vae.compile(optimizer='rmsprop')

# load the data
(x_train, _), (x_test, y_test) = fashion_mnist.load_data()

x_train = x_train.astype('float32') / 255.
x_train = x_train.reshape((x_train.shape[0],) + original_img_size)
x_test = x_test.astype('float32') / 255.
x_test = x_test.reshape((x_test.shape[0],) + original_img_size)

# train the VAE model
history = vae.fit(x_train,
        shuffle=True,
        epochs=epochs,
        batch_size=batch_size,
        validation_data=(x_test, None))

plot_train_history_loss(history)
{{< /highlight >}}

Similar to the case of simple VAE model, we can look at the neighborhoods of 
different classes on the latent 2D plane:

{{< highlight lang="python" linenos="yes" >}}
# project inputs on the latent space
encoder = Model(x, z_mean)
plot_latentSpace(encoder, x_test, y_test, batch_size)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/vae_conv_latent.png" alt="VAE network" class="figure img-responsive align-center" >}}

We can now see that the separation between different class of images are larger than the simple MLP based VAE model.

Finally, we can now generate new images from our, hopefully, better VAE model.

{{< highlight lang="python" linenos="yes" >}}
# generator that can sample from the learned distribution
decoder_input = Input(shape=(latent_dim,))
_hid_decoded = decoder_hid(decoder_input)
_up_decoded = decoder_upsample(_hid_decoded)
_reshape_decoded = decoder_reshape(_up_decoded)
_deconv_1_decoded = decoder_deconv_1(_reshape_decoded)
_deconv_2_decoded = decoder_deconv_2(_deconv_1_decoded)
_x_decoded_relu = decoder_deconv_3_upsamp(_deconv_2_decoded)
_x_decoded_mean_squash = decoder_mean_squash(_x_decoded_relu)
generator = Model(decoder_input, _x_decoded_mean_squash)

plot_generatedImages(generator)
{{< /highlight >}}

{{< figure src="../../images/autoencoders/vae_conv_gen.png" alt="VAE network" class="figure img-responsive align-center" >}}

[kpca]: https://en.wikipedia.org/wiki/Kernel_principal_component_analysis

# Usage of Autoencoders

Most common uses of Autoenoders are:

- **Dimensionality Reduction**: Dimensionality reduction was one of the first
applications of representation learning and deep learning. Lower-dimensional 
representations can improve performance on many tasks, such as classification. 
Models of smaller spaces consume less memory and runtime. The hints provided 
by the mapping to the lower-dimensional space aid generalization. Due to 
non-linear nature, autoencoders tend to perform better than traditional 
techniques like [PCA], [kernel PCA][kpca] etc.
- **Denoising and Transformation**: You can distort the data and add some noise in it before feeding it to DAEs. This can help in generalizing over the test set. AEs are also useful in [image transformation tasks][ref3], eg. [document cleaning][ref4], [applying color to images][ref5], [medical image segmentation using U-net][unet], a variant of autoencoders etc.
[ref3]: https://arxiv.org/pdf/1703.00848.pdf
[ref4]: https://www.kaggle.com/c/denoising-dirty-documents
[ref5]: https://arxiv.org/pdf/1603.08511.pdf
[unet]: https://arxiv.org/abs/1505.04597
- **Information Retrieval**: the task of finding entries in a database that 
resemble a query entry. This task derives the usual benefits from 
dimensionality reduction that other tasks do, but also derives the 
additional benefit that search can become extremely efficient in certain 
kinds of low-dimensional spaces.

- **In Natural Language Processing**
  * Word Embeddings
  * Machine Translation
  * Document Clustering
  * Sentiment Analysis
  * Paraphrase Detection

- **Image/data Generation**: We saw theoretical details of generative nature of VAEs above. See [this blog post by openAI][gen] for a detailed review of image generation.


- **Anamoly detection**: For highly imbalanced data (like [credit card fraud 
detection][fraud], defects in manufacturing etc.) you may have sufficient data 
for the positive class and very few or no data for the negative class. In such 
situations, you can train an AE on your positive data and learn features and 
then compute reconstruction error on the training set to find a threshold. 
During testing, you can use this threshold to reject those test instances 
whose values are greater than this threshold. However, optimizing the 
threshold that can generalize well on the unseen test cases is challenging.
VAEs have been used as [alternative for this task][anamoly], where 
reconstruction error is probabilistic and hence easier to generalize. See this 
article by [FICO][fico] where they use autoencoders for detecting anomalies in 
credit scores.

[fico]: http://www.fico.com/en/blogs/analytics-optimization/improving-model-data-governance-auto-encoders/
[anamoly]: https://arxiv.org/pdf/1802.03903.pdf
[fraud]: https://www.kaggle.com/mlg-ulb/creditcardfraud
[gen]: https://blog.openai.com/generative-models/

This is it! its been quite a long article. Hope this is helpful to some of 
you. Please let me know via comments below if any particular issues/concepts 
you would like me to go over in more details. I would also love to know if any 
particular topic in machine/deep learning you would like me to cover in future 
posts.
