---
layout: post
title: "Log-rank test with coarsened exact matching"
date: 2024-04-27
author: Tomoya Baba, Nakahiro Yoshida
tags: stat.TH
---

It is of special importance in the clinical trial to compare survival times between the treatment group and the control group. Propensity score methods with a logistic regression model are often used to reduce the effects of confounders. However, the modeling of complex structures between the covariates, the treatment assignment and the survival time is difficult. In this paper, we consider coarsened exact matching (CEM), which does not need any parametric models, and we propose the weighted log-rank statistic based on CEM. We derive asymptotic properties of the weighted log-rank statistic, such as the weak convergence to a Gaussian process in Skorokhod space, in particular the asymptotic normality, under the null hypothesis and the consistency of the log-rank test. Simulation studies show that the log-rank statistic based on CEM is more robust than the log-rank statistic based on the propensity score.

[Read more](https://arxiv.org/abs/2403.16121)