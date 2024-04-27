---
layout: post
title: "Spectral clustering in the Gaussian mixture block model"
date: 2024-04-27
author: Shuangping Li, Tselil Schramm
tags: stat.ML, stat.TH
---

Gaussian mixture block models are distributions over graphs that strive to model modern networks: to generate a graph from such a model, we associate each vertex $i$ with a latent feature vector $u_i \in \mathbb{R}^d$ sampled from a mixture of Gaussians, and we add edge $(i,j)$ if and only if the feature vectors are sufficiently similar, in that $\langle u_i,u_j \rangle \ge \tau$ for a pre-specified threshold $\tau$. The different components of the Gaussian mixture represent the fact that there may be different types of nodes with different distributions over features -- for example, in a social network each component represents the different attributes of a distinct community. Natural algorithmic tasks associated with these networks are embedding (recovering the latent feature vectors) and clustering (grouping nodes by their mixture component).
  In this paper we initiate the study of clustering and embedding graphs sampled from high-dimensional Gaussian mixture block models, where the dimension of the latent feature vectors $d\to \infty$ as the size of the network $n \to \infty$. This high-dimensional setting is most appropriate in the context of modern networks, in which we think of the latent feature space as being high-dimensional. We analyze the performance of canonical spectral clustering and embedding algorithms for such graphs in the case of 2-component spherical Gaussian mixtures, and begin to sketch out the information-computation landscape for clustering and embedding in these models.

[Read more](https://arxiv.org/abs/2305.00979)