---
layout: post
title: "Augmented Doubly Robust Post-Imputation Inference for Proteomic Data"
date: 2024-04-27
author: Haeun Moon, Jin-Hong Du, Jing Lei, Kathryn Roeder
tags: stat.ME, stat.AP
---

Quantitative measurements produced by mass spectrometry proteomics experiments offer a direct way to explore the role of proteins in molecular mechanisms. However, analysis of such data is challenging due to the large proportion of missing values. A common strategy to address this issue is to utilize an imputed dataset, which often introduces systematic bias into downstream analyses if the imputation errors are ignored. In this paper, we propose a statistical framework inspired by doubly robust estimators that offers valid and efficient inference for proteomic data. Our framework combines powerful machine learning tools, such as variational autoencoders, to augment the imputation quality with high-dimensional peptide data, and a parametric model to estimate the propensity score for debiasing imputed outcomes. Our estimator is compatible with the double machine learning framework and has provable properties. In application to both single-cell and bulk-cell proteomic data our method utilizes the imputed data to gain additional, meaningful discoveries and yet maintains good control of false positives.

[Read more](https://arxiv.org/abs/2403.15802)