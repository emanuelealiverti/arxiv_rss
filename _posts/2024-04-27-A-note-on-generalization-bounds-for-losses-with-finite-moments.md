---
layout: post
title: "A note on generalization bounds for losses with finite moments"
date: 2024-04-27
author: Borja Rodríguez-Gálvez, Omar Rivasplata, Ragnar Thobaben, Mikael Skoglund
tags: stat.ML
---

This paper studies the truncation method from Alquier [1] to derive high-probability PAC-Bayes bounds for unbounded losses with heavy tails. Assuming that the $p$-th moment is bounded, the resulting bounds interpolate between a slow rate $1 / \sqrt{n}$ when $p=2$, and a fast rate $1 / n$ when $p \to \infty$ and the loss is essentially bounded. Moreover, the paper derives a high-probability PAC-Bayes bound for losses with a bounded variance. This bound has an exponentially better dependence on the confidence parameter and the dependency measure than previous bounds in the literature. Finally, the paper extends all results to guarantees in expectation and single-draw PAC-Bayes. In order to so, it obtains analogues of the PAC-Bayes fast rate bound for bounded losses from [2] in these settings.

[Read more](https://arxiv.org/abs/2403.16681)