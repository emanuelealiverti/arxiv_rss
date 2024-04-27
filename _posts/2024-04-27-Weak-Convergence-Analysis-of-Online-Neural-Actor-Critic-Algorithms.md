---
layout: post
title: "Weak Convergence Analysis of Online Neural Actor-Critic Algorithms"
date: 2024-04-27
author: Samuel Chun-Hei Lam, Justin Sirignano, Ziheng Wang
tags: stat.ML
---

We prove that a single-layer neural network trained with the online actor critic algorithm converges in distribution to a random ordinary differential equation (ODE) as the number of hidden units and the number of training steps $\rightarrow \infty$. In the online actor-critic algorithm, the distribution of the data samples dynamically changes as the model is updated, which is a key challenge for any convergence analysis. We establish the geometric ergodicity of the data samples under a fixed actor policy. Then, using a Poisson equation, we prove that the fluctuations of the model updates around the limit distribution due to the randomly-arriving data samples vanish as the number of parameter updates $\rightarrow \infty$. Using the Poisson equation and weak convergence techniques, we prove that the actor neural network and critic neural network converge to the solutions of a system of ODEs with random initial conditions. Analysis of the limit ODE shows that the limit critic network will converge to the true value function, which will provide the actor an asymptotically unbiased estimate of the policy gradient. We then prove that the limit actor network will converge to a stationary point.

[Read more](https://arxiv.org/abs/2403.16825)