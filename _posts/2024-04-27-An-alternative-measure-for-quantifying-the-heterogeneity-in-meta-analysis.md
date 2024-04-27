---
layout: post
title: "An alternative measure for quantifying the heterogeneity in meta-analysis"
date: 2024-04-27
author: Ke Yang, Enxuan Lin, Wangli Xu, Liping Zhu, Tiejun Tong
tags: stat.ME
---

Quantifying the heterogeneity is an important issue in meta-analysis, and among the existing measures, the $I^2$ statistic is most commonly used. In this paper, we first illustrate with a simple example that the $I^2$ statistic is heavily dependent on the study sample sizes, mainly because it is used to quantify the heterogeneity between the observed effect sizes. To reduce the influence of sample sizes, we introduce an alternative measure that aims to directly measure the heterogeneity between the study populations involved in the meta-analysis. We further propose a new estimator, namely the $I_A^2$ statistic, to estimate the newly defined measure of heterogeneity. For practical implementation, the exact formulas of the $I_A^2$ statistic are also derived under two common scenarios with the effect size as the mean difference (MD) or the standardized mean difference (SMD). Simulations and real data analysis demonstrate that the $I_A^2$ statistic provides an asymptotically unbiased estimator for the absolute heterogeneity between the study populations, and it is also independent of the study sample sizes as expected. To conclude, our newly defined $I_A^2$ statistic can be used as a supplemental measure of heterogeneity to monitor the situations where the study effect sizes are indeed similar with little biological difference. In such scenario, the fixed-effect model can be appropriate; nevertheless, when the sample sizes are sufficiently large, the $I^2$ statistic may still increase to 1 and subsequently suggest the random-effects model for meta-analysis.

[Read more](https://arxiv.org/abs/2403.16706)