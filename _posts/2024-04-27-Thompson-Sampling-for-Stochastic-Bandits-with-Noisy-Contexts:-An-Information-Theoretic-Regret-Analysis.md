---
layout: post
title: "Thompson Sampling for Stochastic Bandits with Noisy Contexts: An Information-Theoretic Regret Analysis"
date: 2024-04-27
author: Sharu Theresa Jose, Shana Moothedath
tags: stat.ML
---

We explore a stochastic contextual linear bandit problem where the agent observes a noisy, corrupted version of the true context through a noise channel with an unknown noise parameter. Our objective is to design an action policy that can approximate" that of an oracle, which has access to the reward model, the channel parameter, and the predictive distribution of the true context from the observed noisy context. In a Bayesian framework, we introduce a Thompson sampling algorithm for Gaussian bandits with Gaussian context noise. Adopting an information-theoretic analysis, we demonstrate the Bayesian regret of our algorithm concerning the oracle's action policy. We also extend this problem to a scenario where the agent observes the true context with some delay after receiving the reward and show that delayed true contexts lead to lower Bayesian regret. Finally, we empirically demonstrate the performance of the proposed algorithms against baselines.

[Read more](https://arxiv.org/abs/2401.11565)