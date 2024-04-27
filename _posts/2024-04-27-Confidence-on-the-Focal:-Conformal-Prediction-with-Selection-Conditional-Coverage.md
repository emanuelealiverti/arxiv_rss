---
layout: post
title: "Confidence on the Focal: Conformal Prediction with Selection-Conditional Coverage"
date: 2024-04-27
author: Ying Jin, Zhimei Ren
tags: stat.ME, stat.ML, stat.TH
---

Conformal prediction builds marginally valid prediction intervals that cover the unknown outcome of a randomly drawn new test point with a prescribed probability. However, a common scenario in practice is that, after seeing the data, practitioners decide which test unit(s) to focus on in a data-driven manner and seek for uncertainty quantification of the focal unit(s). In such cases, marginally valid conformal prediction intervals may not provide valid coverage for the focal unit(s) due to selection bias. This paper presents a general framework for constructing a prediction set with finite-sample exact coverage conditional on the unit being selected by a given procedure. The general form of our method works for arbitrary selection rules that are invariant to the permutation of the calibration units, and generalizes Mondrian Conformal Prediction to multiple test units and non-equivariant classifiers. We then work out the computationally efficient implementation of our framework for a number of realistic selection rules, including top-K selection, optimization-based selection, selection based on conformal p-values, and selection based on properties of preliminary conformal prediction sets. The performance of our methods is demonstrated via applications in drug discovery and health risk prediction.

[Read more](https://arxiv.org/abs/2403.03868)