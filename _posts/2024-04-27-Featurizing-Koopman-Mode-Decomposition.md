---
layout: post
title: "Featurizing Koopman Mode Decomposition"
date: 2024-04-27
author: David Aristoff, Jeremy Copperman, Nathan Mankovich, Alexander Davies
tags: stat.ML
---

This article introduces an advanced Koopman mode decomposition (KMD) technique -- coined Featurized Koopman Mode Decomposition (FKMD) -- that uses time embedding and Mahalanobis scaling to enhance analysis and prediction of high dimensional dynamical systems. The time embedding expands the observation space to better capture underlying manifold structure, while the Mahalanobis scaling, applied to kernel or random Fourier features, adjusts observations based on the system's dynamics. This aids in featurizing KMD in cases where good features are not a priori known. We find that the Mahalanobis scaling from FKMD can be used for effective dimensionality reduction of alanine dipeptide data. We also show that FKMD improves predictions for a high-dimensional Lorenz attractor and a cell signaling problem from cancer research.

[Read more](https://arxiv.org/abs/2312.09146)