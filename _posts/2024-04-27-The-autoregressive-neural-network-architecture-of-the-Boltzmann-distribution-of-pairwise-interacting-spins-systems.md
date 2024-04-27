---
layout: post
title: "The autoregressive neural network architecture of the Boltzmann distribution of pairwise interacting spins systems"
date: 2024-04-27
author: Indaco Biazzo
tags: cond-mat.stat-mech, stat.ML
---

Generative Autoregressive Neural Networks (ARNNs) have recently demonstrated exceptional results in image and language generation tasks, contributing to the growing popularity of generative models in both scientific and commercial applications. This work presents an exact mapping of the Boltzmann distribution of binary pairwise interacting systems into autoregressive form. The resulting ARNN architecture has weights and biases of its first layer corresponding to the Hamiltonian's couplings and external fields, featuring widely used structures such as the residual connections and a recurrent architecture with clear physical meanings. Moreover, its architecture's explicit formulation enables the use of statistical physics techniques to derive new ARNNs for specific systems. As examples, new effective ARNN architectures are derived from two well-known mean-field systems, the Curie-Weiss and Sherrington-Kirkpatrick models, showing superior performance in approximating the Boltzmann distributions of the corresponding physics model compared to other commonly used architectures. The connection established between the physics of the system and the neural network architecture provides a means to derive new architectures for different interacting systems and interpret existing ones from a physical perspective.

[Read more](https://arxiv.org/abs/2302.08347)