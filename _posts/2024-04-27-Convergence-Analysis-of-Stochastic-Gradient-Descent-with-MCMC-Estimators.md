---
layout: post
title: "Convergence Analysis of Stochastic Gradient Descent with MCMC Estimators"
date: 2024-04-27
author: Tianyou Li, Fan Chen, Huajie Chen, Zaiwen Wen
tags: stat.ML
---

Understanding stochastic gradient descent (SGD) and its variants is essential for machine learning. However, most of the preceding analyses are conducted under amenable conditions such as unbiased gradient estimator and bounded objective functions, which does not encompass many sophisticated applications, such as variational Monte Carlo, entropy-regularized reinforcement learning and variational inference. In this paper, we consider the SGD algorithm that employ the Markov Chain Monte Carlo (MCMC) estimator to compute the gradient, called MCMC-SGD. Since MCMC reduces the sampling complexity significantly, it is an asymptotically convergent biased estimator in practice. Moreover, by incorporating a general class of unbounded functions, it is much more difficult to analyze the MCMC sampling error. Therefore, we assume that the function is sub-exponential and use the Bernstein inequality for non-stationary Markov chains to derive error bounds of the MCMC estimator. Consequently, MCMC-SGD is proven to have a first order convergence rate $O(\log K/\sqrt{n K})$ with $K$ iterations and a sample size $n$. It partially explains how MCMC influences the behavior of SGD. Furthermore, we verify the correlated negative curvature condition under reasonable assumptions. It is shown that MCMC-SGD escapes from saddle points and reaches $(\epsilon,\epsilon^{1/4})$ approximate second order stationary points or $\epsilon^{1/2}$-variance points at least $O(\epsilon^{-11/2}\log^{2}(1/\epsilon) )$ steps with high probability. Our analysis unveils the convergence pattern of MCMC-SGD across a broad class of stochastic optimization problems, and interprets the convergence phenomena observed in practical applications.

[Read more](https://arxiv.org/abs/2303.10599)