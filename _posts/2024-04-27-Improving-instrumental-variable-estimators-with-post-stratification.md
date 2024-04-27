---
layout: post
title: "Improving instrumental variable estimators with post-stratification"
date: 2024-04-27
author: Nicole E. Pashley, Luke Keele, Luke W. Miratrix
tags: stat.ME
---

Experiments studying get-out-the-vote (GOTV) efforts estimate the causal effect of various mobilization efforts on voter turnout. However, there is often substantial noncompliance in these studies. A usual approach is to use an instrumental variable (IV) analysis to estimate impacts for compliers, here being those actually contacted by the investigators. Unfortunately, popular IV estimators can be unstable in studies with a small fraction of compliers. We explore post-stratifying the data (e.g., taking a weighted average of IV estimates within each stratum) using variables that predict complier status (and, potentially, the outcome) to mitigate this. We present the benefits of post-stratification in terms of bias, variance, and improved standard error estimates, and provide a finite-sample asymptotic variance formula. We also compare the performance of different IV approaches and discuss the advantages of our design-based post-stratification approach over incorporating compliance-predictive covariates into the two-stage least squares estimator. In the end, we show that covariates predictive of compliance can increase precision, but only if one is willing to make a bias-variance trade-off by down-weighting or dropping strata with few compliers. By contrast, standard approaches such as two-stage least squares fail to use such information. We finally examine the benefits of our approach in two GOTV applications.

[Read more](https://arxiv.org/abs/2303.10016)