---
layout: post
title: "An Analytic Solution to Covariance Propagation in Neural Networks"
date: 2024-04-27
author: Oren Wright, Yorie Nakahira, José M. F. Moura
tags: stat.ML
---

Uncertainty quantification of neural networks is critical to measuring the reliability and robustness of deep learning systems. However, this often involves costly or inaccurate sampling methods and approximations. This paper presents a sample-free moment propagation technique that propagates mean vectors and covariance matrices across a network to accurately characterize the input-output distributions of neural networks. A key enabler of our technique is an analytic solution for the covariance of random variables passed through nonlinear activation functions, such as Heaviside, ReLU, and GELU. The wide applicability and merits of the proposed technique are shown in experiments analyzing the input-output distributions of trained neural networks and training Bayesian neural networks.

[Read more](https://arxiv.org/abs/2403.16163)