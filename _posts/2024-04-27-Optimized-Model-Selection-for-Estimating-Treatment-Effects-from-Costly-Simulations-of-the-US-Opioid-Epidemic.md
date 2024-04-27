---
layout: post
title: "Optimized Model Selection for Estimating Treatment Effects from Costly Simulations of the US Opioid Epidemic"
date: 2024-04-27
author: Abdulrahman A. Ahmed, M. Amin Rahimian, Mark S. Roberts
tags: stat.ME, stat.AP
---

Agent-based simulation with a synthetic population can help us compare different treatment conditions while keeping everything else constant within the same population (i.e., as digital twins). Such population-scale simulations require large computational power (i.e., CPU resources) to get accurate estimates for treatment effects. We can use meta models of the simulation results to circumvent the need to simulate every treatment condition. Selecting the best estimating model at a given sample size (number of simulation runs) is a crucial problem. Depending on the sample size, the ability of the method to estimate accurately can change significantly. In this paper, we discuss different methods to explore what model works best at a specific sample size. In addition to the empirical results, we provide a mathematical analysis of the MSE equation and how its components decide which model to select and why a specific method behaves that way in a range of sample sizes. The analysis showed why the direction estimation method is better than model-based methods in larger sample sizes and how the between-group variation and the within-group variation affect the MSE equation.

[Read more](https://arxiv.org/abs/2403.15755)