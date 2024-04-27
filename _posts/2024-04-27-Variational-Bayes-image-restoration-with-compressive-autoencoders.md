---
layout: post
title: "Variational Bayes image restoration with compressive autoencoders"
date: 2024-04-27
author: Maud Biquard, Marie Chabert, Thomas Oberlin
tags: stat.ML
---

Regularization of inverse problems is of paramount importance in computational imaging. The ability of neural networks to learn efficient image representations has been recently exploited to design powerful data-driven regularizers. While state-of-the-art plug-and-play methods rely on an implicit regularization provided by neural denoisers, alternative Bayesian approaches consider Maximum A Posteriori (MAP) estimation in the latent space of a generative model, thus with an explicit regularization. However, state-of-the-art deep generative models require a huge amount of training data compared to denoisers. Besides, their complexity hampers the optimization involved in latent MAP derivation. In this work, we first propose to use compressive autoencoders instead. These networks, which can be seen as variational autoencoders with a flexible latent prior, are smaller and easier to train than state-of-the-art generative models. As a second contribution, we introduce the Variational Bayes Latent Estimation (VBLE) algorithm, which performs latent estimation within the framework of variational inference. Thanks to a simple yet efficient parameterization of the variational posterior, VBLE allows for fast and easy (approximate) posterior sampling. Experimental results on image datasets BSD and FFHQ demonstrate that VBLE reaches similar performance than state-of-the-art plug-and-play methods, while being able to quantify uncertainties faster than other existing posterior sampling techniques.

[Read more](https://arxiv.org/abs/2311.17744)