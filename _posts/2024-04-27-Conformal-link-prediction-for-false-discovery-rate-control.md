---
layout: post
title: "Conformal link prediction for false discovery rate control"
date: 2024-04-27
author: Ariane Marandon
tags: stat.ME, stat.ML
---

Most link prediction methods return estimates of the connection probability of missing edges in a graph. Such output can be used to rank the missing edges from most to least likely to be a true edge, but does not directly provide a classification into true and non-existent. In this work, we consider the problem of identifying a set of true edges with a control of the false discovery rate (FDR). We propose a novel method based on high-level ideas from the literature on conformal inference. The graph structure induces intricate dependence in the data, which we carefully take into account, as this makes the setup different from the usual setup in conformal inference, where data exchangeability is assumed. The FDR control is empirically demonstrated for both simulated and real data.

[Read more](https://arxiv.org/abs/2306.14693)