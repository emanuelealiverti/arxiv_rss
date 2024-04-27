---
layout: post
title: "Discrete Latent Graph Generative Modeling with Diffusion Bridges"
date: 2024-04-27
author: Van Khoa Nguyen, Yoann Boget, Frantzeska Lavda, Alexandros Kalousis
tags: stat.ML
---

Learning graph generative models over latent spaces has received less attention compared to models that operate on the original data space and has so far demonstrated lacklustre performance. We present GLAD a latent space graph generative model. Unlike most previous latent space graph generative models, GLAD operates on a discrete latent space that preserves to a significant extent the discrete nature of the graph structures making no unnatural assumptions such as latent space continuity. We learn the prior of our discrete latent space by adapting diffusion bridges to its structure. By operating over an appropriately constructed latent space we avoid relying on decompositions that are often used in models that operate in the original data space. We present experiments on a series of graph benchmark datasets which clearly show the superiority of the discrete latent space and obtain state of the art graph generative performance, making GLAD the first latent space graph generative model with competitive performance. Our source code is published at: \url{https://github.com/v18nguye/GLAD}.

[Read more](https://arxiv.org/abs/2403.16883)