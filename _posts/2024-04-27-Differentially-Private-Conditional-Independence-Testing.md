---
layout: post
title: "Differentially Private Conditional Independence Testing"
date: 2024-04-27
author: Iden Kalemaj, Shiva Prasad Kasiviswanathan, Aaditya Ramdas
tags: stat.ML
---

Conditional independence (CI) tests are widely used in statistical data analysis, e.g., they are the building block of many algorithms for causal graph discovery. The goal of a CI test is to accept or reject the null hypothesis that $X \perp \!\!\! \perp Y \mid Z$, where $X \in \mathbb{R}, Y \in \mathbb{R}, Z \in \mathbb{R}^d$. In this work, we investigate conditional independence testing under the constraint of differential privacy. We design two private CI testing procedures: one based on the generalized covariance measure of Shah and Peters (2020) and another based on the conditional randomization test of Cand\`es et al. (2016) (under the model-X assumption). We provide theoretical guarantees on the performance of our tests and validate them empirically. These are the first private CI tests with rigorous theoretical guarantees that work for the general case when $Z$ is continuous.

[Read more](https://arxiv.org/abs/2306.06721)