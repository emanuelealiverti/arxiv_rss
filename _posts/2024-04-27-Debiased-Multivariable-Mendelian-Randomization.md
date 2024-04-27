---
layout: post
title: "Debiased Multivariable Mendelian Randomization"
date: 2024-04-27
author: Yinxiang Wu, Hyunseung Kang, Ting Ye
tags: stat.ME
---

Multivariable Mendelian randomization (MVMR) uses genetic variants as instrumental variables to infer the direct effect of multiple exposures on an outcome. Compared to univariable Mendelian randomization, MVMR is less prone to horizontal pleiotropy and enables estimation of the direct effect of each exposure on the outcome. However, MVMR faces greater challenges with weak instruments -- genetic variants that are weakly associated with some exposures conditional on the other exposures. This article focuses on MVMR using summary data from genome-wide association studies (GWAS). We provide a new asymptotic regime to analyze MVMR estimators with many weak instruments, allowing for linear combinations of exposures to have different degrees of instrument strength, and formally show that the popular multivariable inverse-variance weighted (MV-IVW) estimator's asymptotic behavior is highly sensitive to instruments' strength. We then propose a multivariable debiased IVW (MV-dIVW) estimator, which effectively reduces the asymptotic bias from weak instruments in MV-IVW, and introduce an adjusted version, MV-adIVW, for improved finite-sample robustness. We establish the theoretical properties of our proposed estimators and extend them to handle balanced horizontal pleiotropy. We conclude by demonstrating the performance of our proposed methods in simulated and real datasets. We implement this method in the R package mr.divw.

[Read more](https://arxiv.org/abs/2402.00307)