---
layout: post
title: "Fast and Unified Path Gradient Estimators for Normalizing Flows"
date: 2024-04-27
author: Lorenz Vaitl, Ludwig Winkler, Lorenz Richter, Pan Kessel
tags: stat.ML
---

Recent work shows that path gradient estimators for normalizing flows have lower variance compared to standard estimators for variational inference, resulting in improved training. However, they are often prohibitively more expensive from a computational point of view and cannot be applied to maximum likelihood training in a scalable manner, which severely hinders their widespread adoption. In this work, we overcome these crucial limitations. Specifically, we propose a fast path gradient estimator which improves computational efficiency significantly and works for all normalizing flow architectures of practical relevance. We then show that this estimator can also be applied to maximum likelihood training for which it has a regularizing effect as it can take the form of a given target energy function into account. We empirically establish its superior performance and reduced variance for several natural sciences applications.

[Read more](https://arxiv.org/abs/2403.15881)