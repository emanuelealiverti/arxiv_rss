---
layout: post
title: "Deep Gaussian Covariance Network with Trajectory Sampling for Data-Efficient Policy Search"
date: 2024-04-27
author: Can Bogoclu, Robert Vosshall, Kevin Cremanns, Dirk Roos
tags: stat.ML
---

Probabilistic world models increase data efficiency of model-based reinforcement learning (MBRL) by guiding the policy with their epistemic uncertainty to improve exploration and acquire new samples. Moreover, the uncertainty-aware learning procedures in probabilistic approaches lead to robust policies that are less sensitive to noisy observations compared to uncertainty unaware solutions. We propose to combine trajectory sampling and deep Gaussian covariance network (DGCN) for a data-efficient solution to MBRL problems in an optimal control setting. We compare trajectory sampling with density-based approximation for uncertainty propagation using three different probabilistic world models; Gaussian processes, Bayesian neural networks, and DGCNs. We provide empirical evidence using four different well-known test environments, that our method improves the sample-efficiency over other combinations of uncertainty propagation methods and probabilistic models. During our tests, we place particular emphasis on the robustness of the learned policies with respect to noisy initial states.

[Read more](https://arxiv.org/abs/2403.15908)