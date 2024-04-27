---
layout: post
title: "Asymptotics of predictive distributions driven by sample means and variances"
date: 2024-04-27
author: Samuele Garelli, Fabrizio Leisen, Luca Pratelli, Pietro Rigo
tags: stat.ME, stat.TH
---

Let $\alpha_n(\cdot)=P\bigl(X_{n+1}\in\cdot\mid X_1,\ldots,X_n\bigr)$ be the predictive distributions of a sequence $(X_1,X_2,\ldots)$ of $p$-variate random variables. Suppose $$\alpha_n=\mathcal{N}_p(M_n,Q_n)$$ where $M_n=\frac{1}{n}\sum_{i=1}^nX_i$ and $Q_n=\frac{1}{n}\sum_{i=1}^n(X_i-M_n)(X_i-M_n)^t$. Then, there is a random probability measure $\alpha$ on $\mathbb{R}^p$ such that $\alpha_n\rightarrow\alpha$ weakly a.s. If $p\in\{1,2\}$, one also obtains $\lVert\alpha_n-\alpha\rVert\overset{a.s.}\longrightarrow 0$ where $\lVert\cdot\rVert$ is total variation distance. Moreover, the convergence rate of $\lVert\alpha_n-\alpha\rVert$ is arbitrarily close to $n^{-1/2}$. These results (apart from the one regarding the convergence rate) still apply even if $\alpha_n=\mathcal{L}_p(M_n,Q_n)$, where $\mathcal{L}_p$ belongs to a class of distributions much larger than the normal. Finally, the asymptotic behavior of copula-based predictive distributions (introduced in [13]) is investigated and a numerical experiment is performed.

[Read more](https://arxiv.org/abs/2403.16828)