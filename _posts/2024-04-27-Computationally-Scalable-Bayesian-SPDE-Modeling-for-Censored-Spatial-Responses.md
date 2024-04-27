---
layout: post
title: "Computationally Scalable Bayesian SPDE Modeling for Censored Spatial Responses"
date: 2024-04-27
author: Indranil Sahoo, Suman Majumder, Arnab Hazra, Ana G. Rappold, Dipankar Bandyopadhyay
tags: stat.ME, stat.AP, stat.CO
---

Observations of groundwater pollutants, such as arsenic or Perfluorooctane sulfonate (PFOS), are riddled with left censoring. These measurements have impact on the health and lifestyle of the populace. Left censoring of these spatially correlated observations are usually addressed by applying Gaussian processes (GPs), which have theoretical advantages. However, this comes with a challenging computational complexity of $\mathcal{O}(n^3)$, which is impractical for large datasets. Additionally, a sizable proportion of the data being left-censored creates further bottlenecks, since the likelihood computation now involves an intractable high-dimensional integral of the multivariate Gaussian density. In this article, we tackle these two problems simultaneously by approximating the GP with a Gaussian Markov random field (GMRF) approach that exploits an explicit link between a GP with Mat\'ern correlation function and a GMRF using stochastic partial differential equations (SPDEs). We introduce a GMRF-based measurement error into the model, which alleviates the likelihood computation for the censored data, drastically improving the speed of the model while maintaining admirable accuracy. Our approach demonstrates robustness and substantial computational scalability, compared to state-of-the-art methods for censored spatial responses across various simulation settings. Finally, the fit of this fully Bayesian model to the concentration of PFOS in groundwater available at 24,959 sites across California, where 46.62\% responses are censored, produces prediction surface and uncertainty quantification in real time, thereby substantiating the applicability and scalability of the proposed method. Code for implementation is made available via GitHub.

[Read more](https://arxiv.org/abs/2403.15670)