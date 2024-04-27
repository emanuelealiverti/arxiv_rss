---
layout: post
title: "Causal Discovery from Poisson Branching Structural Causal Model Using High-Order Cumulant with Path Analysis"
date: 2024-04-27
author: Jie Qiao, Yu Xiang, Zhengming Chen, Ruichu Cai, Zhifeng Hao
tags: stat.ML
---

Count data naturally arise in many fields, such as finance, neuroscience, and epidemiology, and discovering causal structure among count data is a crucial task in various scientific and industrial scenarios. One of the most common characteristics of count data is the inherent branching structure described by a binomial thinning operator and an independent Poisson distribution that captures both branching and noise. For instance, in a population count scenario, mortality and immigration contribute to the count, where survival follows a Bernoulli distribution, and immigration follows a Poisson distribution. However, causal discovery from such data is challenging due to the non-identifiability issue: a single causal pair is Markov equivalent, i.e., $X\rightarrow Y$ and $Y\rightarrow X$ are distributed equivalent. Fortunately, in this work, we found that the causal order from $X$ to its child $Y$ is identifiable if $X$ is a root vertex and has at least two directed paths to $Y$, or the ancestor of $X$ with the most directed path to $X$ has a directed path to $Y$ without passing $X$. Specifically, we propose a Poisson Branching Structure Causal Model (PB-SCM) and perform a path analysis on PB-SCM using high-order cumulants. Theoretical results establish the connection between the path and cumulant and demonstrate that the path information can be obtained from the cumulant. With the path information, causal order is identifiable under some graphical conditions. A practical algorithm for learning causal structure under PB-SCM is proposed and the experiments demonstrate and verify the effectiveness of the proposed method.

[Read more](https://arxiv.org/abs/2403.16523)