---
layout: post
title: "Exponential Concentration in Stochastic Approximation"
date: 2024-04-27
author: Kody Law, Neil Walton, Shangda Yang
tags: stat.ML
---

We analyze the behavior of stochastic approximation algorithms where iterates, in expectation, progress towards an objective at each step. When progress is proportional to the step size of the algorithm, we prove exponential concentration bounds. These tail-bounds contrast asymptotic normality results, which are more frequently associated with stochastic approximation. The methods that we develop rely on a geometric ergodicity proof. This extends a result on Markov chains due to Hajek (1982) to the area of stochastic approximation algorithms. We apply our results to several different Stochastic Approximation algorithms, specifically Projected Stochastic Gradient Descent, Kiefer-Wolfowitz and Stochastic Frank-Wolfe algorithms. When applicable, our results prove faster $O(1/t)$ and linear convergence rates for Projected Stochastic Gradient Descent with a non-vanishing gradient.

[Read more](https://arxiv.org/abs/2208.07243)