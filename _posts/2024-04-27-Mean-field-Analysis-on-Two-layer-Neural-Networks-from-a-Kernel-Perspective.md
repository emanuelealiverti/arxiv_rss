---
layout: post
title: "Mean-field Analysis on Two-layer Neural Networks from a Kernel Perspective"
date: 2024-04-27
author: Shokichi Takakura, Taiji Suzuki
tags: stat.ML
---

In this paper, we study the feature learning ability of two-layer neural networks in the mean-field regime through the lens of kernel methods. To focus on the dynamics of the kernel induced by the first layer, we utilize a two-timescale limit, where the second layer moves much faster than the first layer. In this limit, the learning problem is reduced to the minimization problem over the intrinsic kernel. Then, we show the global convergence of the mean-field Langevin dynamics and derive time and particle discretization error. We also demonstrate that two-layer neural networks can learn a union of multiple reproducing kernel Hilbert spaces more efficiently than any kernel methods, and neural networks acquire data-dependent kernel which aligns with the target function. In addition, we develop a label noise procedure, which converges to the global optimum and show that the degrees of freedom appears as an implicit regularization.

[Read more](https://arxiv.org/abs/2403.14917)