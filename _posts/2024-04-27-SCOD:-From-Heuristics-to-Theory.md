---
layout: post
title: "SCOD: From Heuristics to Theory"
date: 2024-04-27
author: Vojtech Franc, Jakub Paplham, Daniel Prusa
tags: stat.ML
---

This paper addresses the problem of designing reliable prediction models that abstain from predictions when faced with uncertain or out-of-distribution samples - a recently proposed problem known as Selective Classification in the presence of Out-of-Distribution data (SCOD). We make three key contributions to SCOD. Firstly, we demonstrate that the optimal SCOD strategy involves a Bayes classifier for in-distribution (ID) data and a selector represented as a stochastic linear classifier in a 2D space, using i) the conditional risk of the ID classifier, and ii) the likelihood ratio of ID and out-of-distribution (OOD) data as input. This contrasts with suboptimal strategies from current OOD detection methods and the Softmax Information Retaining Combination (SIRC), specifically developed for SCOD. Secondly, we establish that in a distribution-free setting, the SCOD problem is not Probably Approximately Correct learnable when relying solely on an ID data sample. Third, we introduce POSCOD, a simple method for learning a plugin estimate of the optimal SCOD strategy from both an ID data sample and an unlabeled mixture of ID and OOD data. Our empirical results confirm the theoretical findings and demonstrate that our proposed method, POSCOD, out performs existing OOD methods in effectively addressing the SCOD problem.

[Read more](https://arxiv.org/abs/2403.16916)