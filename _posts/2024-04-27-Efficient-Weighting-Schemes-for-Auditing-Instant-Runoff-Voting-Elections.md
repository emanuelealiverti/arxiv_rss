---
layout: post
title: "Efficient Weighting Schemes for Auditing Instant-Runoff Voting Elections"
date: 2024-04-27
author: Alexander Ek, Philip B. Stark, Peter J. Stuckey, Damjan Vukcevic
tags: stat.AP
---

Various risk-limiting audit (RLA) methods have been developed for instant-runoff voting (IRV) elections. A recent method, AWAIRE, is the first efficient approach that does not require cast vote records (CVRs). AWAIRE involves adaptively weighted averages of test statistics, essentially "learning" an effective set of hypotheses to test. However, the initial paper on AWAIRE only examined a few weighting schemes and parameter settings.
  We provide an extensive exploration of schemes and settings, to identify and recommend efficient choices for practical use. We focus only on the (hardest) case where CVRs are not available, using simulations based on real election data to assess performance.
  Across our comparisons, the most effective schemes are often those that place most or all of the weight on the apparent "best" hypotheses based on already seen data. Conversely, the optimal tuning parameters tended to vary based on the election margin. Nonetheless, we quantify the performance trade-offs for different choices across varying election margins, aiding in selecting the most desirable trade-off if a default option is needed.
  A limitation of the current AWAIRE implementation is its restriction to handling a small number of candidates (previously demonstrated up to six candidates). One path to a more computationally efficient implementation would be to use lazy evaluation and avoid considering all possible hypotheses. Our findings suggest that such an approach could be done without substantially comprising statistical performance.

[Read more](https://arxiv.org/abs/2403.15400)