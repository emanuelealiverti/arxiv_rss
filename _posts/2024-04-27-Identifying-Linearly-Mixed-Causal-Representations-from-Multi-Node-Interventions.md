---
layout: post
title: "Identifying Linearly-Mixed Causal Representations from Multi-Node Interventions"
date: 2024-04-27
author: Simon Bing, Urmi Ninad, Jonas Wahl, Jakob Runge
tags: stat.ML, stat.ME, stat.TH
---

The task of inferring high-level causal variables from low-level observations, commonly referred to as causal representation learning, is fundamentally underconstrained. As such, recent works to address this problem focus on various assumptions that lead to identifiability of the underlying latent causal variables. A large corpus of these preceding approaches consider multi-environment data collected under different interventions on the causal model. What is common to virtually all of these works is the restrictive assumption that in each environment, only a single variable is intervened on. In this work, we relax this assumption and provide the first identifiability result for causal representation learning that allows for multiple variables to be targeted by an intervention within one environment. Our approach hinges on a general assumption on the coverage and diversity of interventions across environments, which also includes the shared assumption of single-node interventions of previous works. The main idea behind our approach is to exploit the trace that interventions leave on the variance of the ground truth causal variables and regularizing for a specific notion of sparsity with respect to this trace. In addition to and inspired by our theoretical contributions, we present a practical algorithm to learn causal representations from multi-node interventional data and provide empirical evidence that validates our identifiability results.

[Read more](https://arxiv.org/abs/2311.02695)