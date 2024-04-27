---
layout: post
title: "Integrated path stability selection"
date: 2024-04-27
author: Omar Melikechi, Jeffrey W. Miller
tags: stat.ME, stat.ML
---

Stability selection is a widely used method for improving the performance of feature selection algorithms. However, stability selection has been found to be highly conservative, resulting in low sensitivity. Further, the theoretical bound on the expected number of false positives, E(FP), is relatively loose, making it difficult to know how many false positives to expect in practice. In this paper, we introduce a novel method for stability selection based on integrating the stability paths rather than maximizing over them. This yields a tighter bound on E(FP), resulting in a feature selection criterion that has higher sensitivity in practice and is better calibrated in terms of matching the target E(FP). Our proposed method requires the same amount of computation as the original stability selection algorithm, and only requires the user to specify one input parameter, a target value for E(FP). We provide theoretical bounds on performance, and demonstrate the method on simulations and real data from cancer gene expression studies.

[Read more](https://arxiv.org/abs/2403.15877)