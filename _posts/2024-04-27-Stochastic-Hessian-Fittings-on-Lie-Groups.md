---
layout: post
title: "Stochastic Hessian Fittings on Lie Groups"
date: 2024-04-27
author: Xi-Lin Li
tags: stat.ML
---

This paper studies the fitting of Hessian or its inverse for stochastic optimizations using a Hessian fitting criterion from the preconditioned stochastic gradient descent (PSGD) method, which is intimately related to many commonly used second order and adaptive gradient optimizers, e.g., BFGS, Gaussian-Newton and natural gradient descent, AdaGrad, etc. Our analyses reveal the efficiency and reliability differences among a wide range of preconditioner fitting methods, from closed-form to iterative solutions, using Hessian-vector products or stochastic gradients only, with Hessian fittings in the Euclidean space, the manifold of symmetric positive definite (SPL) matrices, or a variety of Lie groups. The most intriguing discovery is that the Hessian fitting itself as an optimization problem is strongly convex under mild conditions on a specific yet general enough Lie group. This discovery turns Hessian fitting into a well behaved optimization problem, and facilitates the designs of highly efficient and elegant Lie group sparse preconditioner fitting methods for large scale stochastic optimizations.

[Read more](https://arxiv.org/abs/2402.11858)