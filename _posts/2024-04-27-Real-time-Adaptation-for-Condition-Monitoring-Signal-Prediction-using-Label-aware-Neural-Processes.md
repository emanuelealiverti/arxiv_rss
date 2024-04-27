---
layout: post
title: "Real-time Adaptation for Condition Monitoring Signal Prediction using Label-aware Neural Processes"
date: 2024-04-27
author: Seokhyun Chung, Raed Al Kontar
tags: stat.ML
---

Building a predictive model that rapidly adapts to real-time condition monitoring (CM) signals is critical for engineering systems/units. Unfortunately, many current methods suffer from a trade-off between representation power and agility in online settings. For instance, parametric methods that assume an underlying functional form for CM signals facilitate efficient online prediction updates. However, this simplification leads to vulnerability to model specifications and an inability to capture complex signals. On the other hand, approaches based on over-parameterized or non-parametric models can excel at explaining complex nonlinear signals, but real-time updates for such models pose a challenging task. In this paper, we propose a neural process-based approach that addresses this trade-off. It encodes available observations within a CM signal into a representation space and then reconstructs the signal's history and evolution for prediction. Once trained, the model can encode an arbitrary number of observations without requiring retraining, enabling on-the-spot real-time predictions along with quantified uncertainty and can be readily updated as more online data is gathered. Furthermore, our model is designed to incorporate qualitative information (i.e., labels) from individual units. This integration not only enhances individualized predictions for each unit but also enables joint inference for both signals and their associated labels. Numerical studies on both synthetic and real-world data in reliability engineering highlight the advantageous features of our model in real-time adaptation, enhanced signal prediction with uncertainty quantification, and joint prediction for labels and signals.

[Read more](https://arxiv.org/abs/2403.16377)