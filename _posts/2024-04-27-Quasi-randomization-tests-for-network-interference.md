---
layout: post
title: "Quasi-randomization tests for network interference"
date: 2024-04-27
author: Supriya Tiwari, Pallavi Basu
tags: stat.ME
---

Many classical inferential approaches fail to hold when interference exists among the population units. This amounts to the treatment status of one unit affecting the potential outcome of other units in the population. Testing for such spillover effects in this setting makes the null hypothesis non-sharp. An interesting approach to tackling the non-sharp nature of the null hypothesis in this setup is constructing conditional randomization tests such that the null is sharp on the restricted population. In randomized experiments, conditional randomized tests hold finite sample validity. Such approaches can pose computational challenges as finding these appropriate sub-populations based on experimental design can involve solving an NP-hard problem. In this paper, we view the network amongst the population as a random variable instead of being fixed. We propose a new approach that builds a conditional quasi-randomization test. Our main idea is to build the (non-sharp) null distribution of no spillover effects using random graph null models. We show that our method is exactly valid in finite-samples under mild assumptions. Our method displays enhanced power over other methods, with substantial improvement in complex experimental designs. We highlight that the method reduces to a simple permutation test, making it easy to implement in practice. We conduct a simulation study to verify the finite-sample validity of our approach and illustrate our methodology to test for interference in a weather insurance adoption experiment run in rural China.

[Read more](https://arxiv.org/abs/2403.16673)