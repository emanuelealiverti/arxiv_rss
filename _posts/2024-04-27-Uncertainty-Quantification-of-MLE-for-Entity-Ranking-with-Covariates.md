---
layout: post
title: "Uncertainty Quantification of MLE for Entity Ranking with Covariates"
date: 2024-04-27
author: Jianqing Fan, Jikai Hou, Mengxin Yu
tags: stat.ME, stat.ML, stat.TH
---

This paper concerns with statistical estimation and inference for the ranking problems based on pairwise comparisons with additional covariate information such as the attributes of the compared items. Despite extensive studies, few prior literatures investigate this problem under the more realistic setting where covariate information exists. To tackle this issue, we propose a novel model, Covariate-Assisted Ranking Estimation (CARE) model, that extends the well-known Bradley-Terry-Luce (BTL) model, by incorporating the covariate information. Specifically, instead of assuming every compared item has a fixed latent score $\{\theta_i^*\}_{i=1}^n$, we assume the underlying scores are given by $\{\alpha_i^*+{x}_i^\top\beta^*\}_{i=1}^n$, where $\alpha_i^*$ and ${x}_i^\top\beta^*$ represent latent baseline and covariate score of the $i$-th item, respectively. We impose natural identifiability conditions and derive the $\ell_{\infty}$- and $\ell_2$-optimal rates for the maximum likelihood estimator of $\{\alpha_i^*\}_{i=1}^{n}$ and $\beta^*$ under a sparse comparison graph, using a novel `leave-one-out' technique (Chen et al., 2019) . To conduct statistical inferences, we further derive asymptotic distributions for the MLE of $\{\alpha_i^*\}_{i=1}^n$ and $\beta^*$ with minimal sample complexity. This allows us to answer the question whether some covariates have any explanation power for latent scores and to threshold some sparse parameters to improve the ranking performance. We improve the approximation method used in (Gao et al., 2021) for the BLT model and generalize it to the CARE model. Moreover, we validate our theoretical results through large-scale numerical studies and an application to the mutual fund stock holding dataset.

[Read more](https://arxiv.org/abs/2212.09961)