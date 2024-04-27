---
layout: post
title: "Private measures, random walks, and synthetic data"
date: 2024-04-27
author: March Boedihardjo, Thomas Strohmer, Roman Vershynin
tags: stat.TH
---

Differential privacy is a mathematical concept that provides an information-theoretic security guarantee. While differential privacy has emerged as a de facto standard for guaranteeing privacy in data sharing, the known mechanisms to achieve it come with some serious limitations. Utility guarantees are usually provided only for a fixed, a priori specified set of queries. Moreover, there are no utility guarantees for more complex - but very common - machine learning tasks such as clustering or classification. In this paper we overcome some of these limitations. Working with metric privacy, a powerful generalization of differential privacy, we develop a polynomial-time algorithm that creates a private measure from a data set. This private measure allows us to efficiently construct private synthetic data that are accurate for a wide range of statistical analysis tools. Moreover, we prove an asymptotically sharp min-max result for private measures and synthetic data for general compact metric spaces. A key ingredient in our construction is a new superregular random walk, whose joint distribution of steps is as regular as that of independent random variables, yet which deviates from the origin logarithmicaly slowly.

[Read more](https://arxiv.org/abs/2204.09167)