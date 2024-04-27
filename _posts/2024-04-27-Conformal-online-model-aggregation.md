---
layout: post
title: "Conformal online model aggregation"
date: 2024-04-27
author: Matteo Gasparin, Aaditya Ramdas
tags: stat.ML
---

Conformal prediction equips machine learning models with a reasonable notion of uncertainty quantification without making strong distributional assumptions. It wraps around any black-box prediction model and converts point predictions into set predictions that have a predefined marginal coverage guarantee. However, conformal prediction only works if we fix the underlying machine learning model in advance. A relatively unaddressed issue in conformal prediction is that of model selection and/or aggregation: for a given problem, which of the plethora of prediction methods (random forests, neural nets, regularized linear models, etc.) should we conformalize? This paper proposes a new approach towards conformal model aggregation in online settings that is based on combining the prediction sets from several algorithms by voting, where weights on the models are adapted over time based on past performance.

[Read more](https://arxiv.org/abs/2403.15527)