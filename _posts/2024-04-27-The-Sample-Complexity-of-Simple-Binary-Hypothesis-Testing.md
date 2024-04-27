---
layout: post
title: "The Sample Complexity of Simple Binary Hypothesis Testing"
date: 2024-04-27
author: Ankit Pensia, Varun Jog, Po-Ling Loh
tags: stat.ML, stat.TH
---

The sample complexity of simple binary hypothesis testing is the smallest number of i.i.d. samples required to distinguish between two distributions $p$ and $q$ in either: (i) the prior-free setting, with type-I error at most $\alpha$ and type-II error at most $\beta$; or (ii) the Bayesian setting, with Bayes error at most $\delta$ and prior distribution $(\alpha, 1-\alpha)$. This problem has only been studied when $\alpha = \beta$ (prior-free) or $\alpha = 1/2$ (Bayesian), and the sample complexity is known to be characterized by the Hellinger divergence between $p$ and $q$, up to multiplicative constants. In this paper, we derive a formula that characterizes the sample complexity (up to multiplicative constants that are independent of $p$, $q$, and all error parameters) for: (i) all $0 \le \alpha, \beta \le 1/8$ in the prior-free setting; and (ii) all $\delta \le \alpha/4$ in the Bayesian setting. In particular, the formula admits equivalent expressions in terms of certain divergences from the Jensen--Shannon and Hellinger families. The main technical result concerns an $f$-divergence inequality between members of the Jensen--Shannon and Hellinger families, which is proved by a combination of information-theoretic tools and case-by-case analyses. We explore applications of our results to robust and distributed (locally-private and communication-constrained) hypothesis testing.

[Read more](https://arxiv.org/abs/2403.16981)