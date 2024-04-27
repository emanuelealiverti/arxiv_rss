---
layout: post
title: "Testing for linearity in scalar-on-function regression with responses missing at random"
date: 2024-04-27
author: Manuel Febrero-Bande, Pedro Galeano, Eduardo García-Portugués, Wenceslao González-Manteiga
tags: stat.ME
---

A goodness-of-fit test for the Functional Linear Model with Scalar Response (FLMSR) with responses Missing at Random (MAR) is proposed in this paper. The test statistic relies on a marked empirical process indexed by the projected functional covariate and its distribution under the null hypothesis is calibrated using a wild bootstrap procedure. The computation and performance of the test rely on having an accurate estimator of the functional slope of the FLMSR when the sample has MAR responses. Three estimation methods based on the Functional Principal Components (FPCs) of the covariate are considered. First, the simplified method estimates the functional slope by simply discarding observations with missing responses. Second, the imputed method estimates the functional slope by imputing the missing responses using the simplified estimator. Third, the inverse probability weighted method incorporates the missing response generation mechanism when imputing. Furthermore, both cross-validation and LASSO regression are used to select the FPCs used by each estimator. Several Monte Carlo experiments are conducted to analyze the behavior of the testing procedure in combination with the functional slope estimators. Results indicate that estimators performing missing-response imputation achieve the highest power. The testing procedure is applied to check for linear dependence between the average number of sunny days per year and the mean curve of daily temperatures at weather stations in Spain.

[Read more](https://arxiv.org/abs/2304.04712)