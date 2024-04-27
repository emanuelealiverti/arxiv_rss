---
layout: post
title: "Testing for sufficient follow-up in survival data with a cure fraction"
date: 2024-04-27
author: Tsz Pang Yuen, Eni Musta
tags: stat.ME
---

In order to estimate the proportion of `immune' or `cured' subjects who will never experience failure, a sufficiently long follow-up period is required. Several statistical tests have been proposed in the literature for assessing the assumption of sufficient follow-up, meaning that the study duration is longer than the support of the survival times for the uncured subjects. However, for practical purposes, the follow-up would be considered sufficiently long if the probability for the event to happen after the end of the study is very small. Based on this observation, we formulate a more relaxed notion of `practically' sufficient follow-up characterized by the quantiles of the distribution and develop a novel nonparametric statistical test. The proposed method relies mainly on the assumption of a non-increasing density function in the tail of the distribution. The test is then based on a shape constrained density estimator such as the Grenander or the kernel smoothed Grenander estimator and a bootstrap procedure is used for computation of the critical values. The performance of the test is investigated through an extensive simulation study, and the method is illustrated on breast cancer data.

[Read more](https://arxiv.org/abs/2403.16832)