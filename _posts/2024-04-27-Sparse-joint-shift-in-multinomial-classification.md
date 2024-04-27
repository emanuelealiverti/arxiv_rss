---
layout: post
title: "Sparse joint shift in multinomial classification"
date: 2024-04-27
author: Dirk Tasche
tags: stat.ML, stat.TH
---

Sparse joint shift (SJS) was recently proposed as a tractable model for general dataset shift which may cause changes to the marginal distributions of features and labels as well as the posterior probabilities and the class-conditional feature distributions. Fitting SJS for a target dataset without label observations may produce valid predictions of labels and estimates of class prior probabilities. We present new results on the transmission of SJS from sets of features to larger sets of features, a conditional correction formula for the class posterior probabilities under the target distribution, identifiability of SJS, and the relationship between SJS and covariate shift. In addition, we point out inconsistencies in the algorithms which were proposed for estimating the characteristics of SJS, as they could hamper the search for optimal solutions, and suggest potential improvements.

[Read more](https://arxiv.org/abs/2303.16971)