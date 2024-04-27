---
layout: post
title: "Online Action Learning in High Dimensions: A Conservative Perspective"
date: 2024-04-27
author: Claudio Cardoso Flores, Marcelo Cunha Medeiros
tags: stat.ML
---

Sequential learning problems are common in several fields of research and practical applications. Examples include dynamic pricing and assortment, design of auctions and incentives and permeate a large number of sequential treatment experiments. In this paper, we extend one of the most popular learning solutions, the $\epsilon_t$-greedy heuristics, to high-dimensional contexts considering a conservative directive. We do this by allocating part of the time the original rule uses to adopt completely new actions to a more focused search in a restrictive set of promising actions. The resulting rule might be useful for practical applications that still values surprises, although at a decreasing rate, while also has restrictions on the adoption of unusual actions. With high probability, we find reasonable bounds for the cumulative regret of a conservative high-dimensional decaying $\epsilon_t$-greedy rule. Also, we provide a lower bound for the cardinality of the set of viable actions that implies in an improved regret bound for the conservative version when compared to its non-conservative counterpart. Additionally, we show that end-users have sufficient flexibility when establishing how much safety they want, since it can be tuned without impacting theoretical properties. We illustrate our proposal both in a simulation exercise and using a real dataset.

[Read more](https://arxiv.org/abs/2009.13961)