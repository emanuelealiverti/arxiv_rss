---
layout: post
title: "Privacy-Protected Spatial Autoregressive Model"
date: 2024-04-27
author: Danyang Huang, Ziyi Kong, Shuyuan Wu, Hansheng Wang
tags: stat.ME
---

Spatial autoregressive (SAR) models are important tools for studying network effects. However, with an increasing emphasis on data privacy, data providers often implement privacy protection measures that make classical SAR models inapplicable. In this study, we introduce a privacy-protected SAR model with noise-added response and covariates to meet privacy-protection requirements. However, in this scenario, the traditional quasi-maximum likelihood estimator becomes infeasible because the likelihood function cannot be formulated. To address this issue, we first consider an explicit expression for the likelihood function with only noise-added responses. However, the derivatives are biased owing to the noise in the covariates. Therefore, we develop techniques that can correct the biases introduced by noise. Correspondingly, a Newton-Raphson-type algorithm is proposed to obtain the estimator, leading to a corrected likelihood estimator. To further enhance computational efficiency, we introduce a corrected least squares estimator based on the idea of bias correction. These two estimation methods ensure both data security and the attainment of statistically valid estimators. Theoretical analysis of both estimators is carefully conducted, and statistical inference methods are discussed. The finite sample performances of different methods are demonstrated through extensive simulations and the analysis of a real dataset.

[Read more](https://arxiv.org/abs/2403.16773)