---
layout: post
title: "Approximation and Estimation Ability of Transformers for Sequence-to-Sequence Functions with Infinite Dimensional Input"
date: 2024-04-27
author: Shokichi Takakura, Taiji Suzuki
tags: stat.ML
---

Despite the great success of Transformer networks in various applications such as natural language processing and computer vision, their theoretical aspects are not well understood. In this paper, we study the approximation and estimation ability of Transformers as sequence-to-sequence functions with infinite dimensional inputs. Although inputs and outputs are both infinite dimensional, we show that when the target function has anisotropic smoothness, Transformers can avoid the curse of dimensionality due to their feature extraction ability and parameter sharing property. In addition, we show that even if the smoothness changes depending on each input, Transformers can estimate the importance of features for each input and extract important features dynamically. Then, we proved that Transformers achieve similar convergence rate as in the case of the fixed smoothness. Our theoretical results support the practical success of Transformers for high dimensional data.

[Read more](https://arxiv.org/abs/2305.18699)