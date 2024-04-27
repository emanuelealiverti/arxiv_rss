---
layout: post
title: "Learning Directed Acyclic Graphs from Partial Orderings"
date: 2024-04-27
author: Ali Shojaie, Wenyu Chen
tags: stat.ML, stat.ME
---

Directed acyclic graphs (DAGs) are commonly used to model causal relationships among random variables. In general, learning the DAG structure is both computationally and statistically challenging. Moreover, without additional information, the direction of edges may not be estimable from observational data. In contrast, given a complete causal ordering of the variables, the problem can be solved efficiently, even in high dimensions. In this paper, we consider the intermediate problem of learning DAGs when a partial causal ordering of variables is available. We propose a general estimation framework for leveraging the partial ordering and present efficient estimation algorithms for low- and high-dimensional problems. The advantages of the proposed framework are illustrated via numerical studies.

[Read more](https://arxiv.org/abs/2403.16031)