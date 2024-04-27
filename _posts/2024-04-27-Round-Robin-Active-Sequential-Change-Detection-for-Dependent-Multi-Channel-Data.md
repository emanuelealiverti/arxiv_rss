---
layout: post
title: "Round Robin Active Sequential Change Detection for Dependent Multi-Channel Data"
date: 2024-04-27
author: Anamitra Chaudhuri, Georgios Fellouris, Ali Tajer
tags: stat.ME, stat.TH
---

This paper considers the problem of sequentially detecting a change in the joint distribution of multiple data sources under a sampling constraint. Specifically, the channels or sources generate observations that are independent over time, but not necessarily independent at any given time instant. The sources follow an initial joint distribution, and at an unknown time instant, the joint distribution of an unknown subset of sources changes. Importantly, there is a hard constraint that only a fixed number of sources are allowed to be sampled at each time instant. The goal is to sequentially observe the sources according to the constraint, and stop sampling as quickly as possible after the change while controlling the false alarm rate below a user-specified level. The sources can be selected dynamically based on the already collected data, and thus, a policy for this problem consists of a joint sampling and change-detection rule. A non-randomized policy is studied, and an upper bound is established on its worst-case conditional expected detection delay with respect to both the change point and the observations from the affected sources before the change.

[Read more](https://arxiv.org/abs/2403.16297)