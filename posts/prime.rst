.. title: Two Simple Math Puzzles
.. slug: PrimeNumberAndPath
.. date: 2015-06-21 23:08:34 UTC-07:00
.. tags: mathjax, Math, Algorithms, Puzzle
.. category: Puzzle
.. link:
.. description:
.. type: text
.. author: Sadanand Singh

Puzzle 1: Prime Numbers
-----------------------

Prove that :math:`p^2-1` is divisible by 24, where :math:`p` is a prime
number with :math:`p>3`.

This is a simple one - do not go by the technicality of the problem statement.

.. TEASER_END

Solution
^^^^^^^^

:math:`p^2-1 = (p-1)\times (p+1)` Given, :math:`p`
is a prime number :math:`>3`, :math:`p-1` and :math:`p+1`
are even. We can also
write,

.. math::
    p-1=2K, \mbox{ and   } p+1=2K+2=2(K+1)

Given, :math:`K \in \mathbb{N}`, either :math:`K`
or :math:`K+1` are also even.
Hence, :math:`(p-1)\times (p+1)` is divisible by :math:`2\times 4 = 8`.

Furthermore, as :math:`p` is prime, we can write it as either
:math:`p = 3s+1` or :math:`p = 3s-1`, where :math:`s \in \mathbb{N}`. In
either case, one of :math:`p-1` or :math:`p+1` are divisible by 3 as
well.

Hence, :math:`p^2-1` is divisible by :math:`8\times 3 = 24`.

Puzzle 2: Hopping on a Chess Board
----------------------------------

On a chess board, basically a :math:`8\times 8` grid, how many ways one
can go from the left most bottom corner to the right most upper corner?
In chess naming conventions, from "a1" to "h8".

**Clarification:**
In the original post this problem was ill defined.

*Please solve this problem with the constraints that only up and right moves are allowed.*

.. figure:: https://upload.wikimedia.org/wikipedia/commons/4/4b/Ternblad_grid_chess_problem.png
   :alt: Chess Board

   Chess Board

Can you find the generic answer for the case of :math:`N\times M` grid.

Solution
^^^^^^^^

**Correction:**
For an :math:`N\times M` grid, we need only :math:`N-1`
right and :math:`M-1` up moves. Thank you Devin for pointing this
out.

Given only forward moves are allowed, for any arbitrary grid of
:math:`N\times M`, a total of :math:`(N-1) + (M-1)` moves are needed.

Any :math:`N-1` of these moves can be of type *right* and :math:`M-1` of
type *up*. In short, this is a combinatorial problem of distributing
:math:`N+M-2` objects into groups of :math:`N-1` and :math:`M-1`. This
is simply,

.. math::
    \dbinom{N+M-2}{N-1} = \frac{(N+M-2)!}{(N-1)! (M-1)!}

In the particular case of the chess board, :math:`N = M = 8`. Hence,
total number of possible paths are:

.. math::
    \mbox{No. of Paths} = \frac{14!}{7! 7!} =3432

Thank you Rohit and Amber for posting quick solutions!

Let me know if you have any other interesting alternative solutions to
these problems.
