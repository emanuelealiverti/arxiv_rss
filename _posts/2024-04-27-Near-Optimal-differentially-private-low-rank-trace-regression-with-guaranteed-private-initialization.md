---
layout: post
title: "Near-Optimal differentially private low-rank trace regression with guaranteed private initialization"
date: 2024-04-27
author: Mengyue Zha
tags: stat.ML
---

We study differentially private (DP) estimation of a rank-$r$ matrix $M \in \RR^{d_1\times d_2}$ under the trace regression model with Gaussian measurement matrices. Theoretically, the sensitivity of non-private spectral initialization is precisely characterized, and the differential-privacy-constrained minimax lower bound for estimating $M$ under the Schatten-$q$ norm is established. Methodologically, the paper introduces a computationally efficient algorithm for DP-initialization with a sample size of $n \geq \wt O (r^2 (d_1\vee d_2))$. Under certain regularity conditions, the DP-initialization falls within a local ball surrounding $M$. We also propose a differentially private algorithm for estimating $M$ based on Riemannian optimization (DP-RGrad), which achieves a near-optimal convergence rate with the DP-initialization and sample size of $n \geq \wt O(r (d_1 + d_2))$. Finally, the paper discusses the non-trivial gap between the minimax lower bound and the upper bound of low-rank matrix estimation under the trace regression model. It is shown that the estimator given by DP-RGrad attains the optimal convergence rate in a weaker notion of differential privacy. Our powerful technique for analyzing the sensitivity of initialization requires no eigengap condition between $r$ non-zero singular values.

[Read more](https://arxiv.org/abs/2403.15999)