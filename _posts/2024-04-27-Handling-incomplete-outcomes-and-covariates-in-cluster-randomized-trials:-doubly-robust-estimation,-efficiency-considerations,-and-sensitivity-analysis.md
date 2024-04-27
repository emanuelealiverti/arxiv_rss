---
layout: post
title: "Handling incomplete outcomes and covariates in cluster-randomized trials: doubly-robust estimation, efficiency considerations, and sensitivity analysis"
date: 2024-04-27
author: Bingkai Wang, Fan Li, Rui Wang
tags: stat.ME
---

In cluster-randomized trials (CRTs), missing data can occur in various ways, including missing values in outcomes and baseline covariates at the individual or cluster level, or completely missing information for non-participants. Among the various types of missing data in CRTs, missing outcomes have attracted the most attention. However, no existing methods can simultaneously address all aforementioned types of missing data in CRTs. To fill in this gap, we propose a new doubly-robust estimator for the average treatment effect on a variety of scales. The proposed estimator simultaneously handles missing outcomes under missingness at random, missing covariates without constraining the missingness mechanism, and missing cluster-population sizes via a uniform sampling mechanism. Furthermore, we detail key considerations to improve precision by specifying the optimal weights, leveraging machine learning, and modeling the treatment assignment mechanism. Finally, to evaluate the impact of violating missing data assumptions, we contribute a new sensitivity analysis framework tailored to CRTs. Simulation studies and a real data application both demonstrate that our proposed methods are effective in handling missing data in CRTs and superior to the existing methods.

[Read more](https://arxiv.org/abs/2401.11278)