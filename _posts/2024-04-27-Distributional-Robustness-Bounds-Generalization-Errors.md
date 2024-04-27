---
layout: post
title: "Distributional Robustness Bounds Generalization Errors"
date: 2024-04-27
author: Shixiong Wang, Haowei Wang
tags: stat.ML
---

Bayesian methods, distributionally robust optimization methods, and regularization methods are three pillars of trustworthy machine learning combating distributional uncertainty, e.g., the uncertainty of an empirical distribution compared to the true underlying distribution. This paper investigates the connections among the three frameworks and, in particular, explores why these frameworks tend to have smaller generalization errors. Specifically, first, we suggest a quantitative definition for "distributional robustness", propose the concept of "robustness measure", and formalize several philosophical concepts in distributionally robust optimization. Second, we show that Bayesian methods are distributionally robust in the probably approximately correct (PAC) sense; in addition, by constructing a Dirichlet-process-like prior in Bayesian nonparametrics, it can be proven that any regularized empirical risk minimization method is equivalent to a Bayesian method. Third, we show that generalization errors of machine learning models can be characterized using the distributional uncertainty of the nominal distribution and the robustness measures of these machine learning models, which is a new perspective to bound generalization errors, and therefore, explain the reason why distributionally robust machine learning models, Bayesian models, and regularization models tend to have smaller generalization errors in a unified manner.

[Read more](https://arxiv.org/abs/2212.09962)