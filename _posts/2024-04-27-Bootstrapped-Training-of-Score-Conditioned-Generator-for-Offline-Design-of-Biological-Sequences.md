---
layout: post
title: "Bootstrapped Training of Score-Conditioned Generator for Offline Design of Biological Sequences"
date: 2024-04-27
author: Minsu Kim, Federico Berto, Sungsoo Ahn, Jinkyoo Park
tags: stat.ML
---

We study the problem of optimizing biological sequences, e.g., proteins, DNA, and RNA, to maximize a black-box score function that is only evaluated in an offline dataset. We propose a novel solution, bootstrapped training of score-conditioned generator (BootGen) algorithm. Our algorithm repeats a two-stage process. In the first stage, our algorithm trains the biological sequence generator with rank-based weights to enhance the accuracy of sequence generation based on high scores. The subsequent stage involves bootstrapping, which augments the training dataset with self-generated data labeled by a proxy score function. Our key idea is to align the score-based generation with a proxy score function, which distills the knowledge of the proxy score function to the generator. After training, we aggregate samples from multiple bootstrapped generators and proxies to produce a diverse design. Extensive experiments show that our method outperforms competitive baselines on biological sequential design tasks. We provide reproducible source code: \href{https://github.com/kaist-silab/bootgen}{https://github.com/kaist-silab/bootgen}.

[Read more](https://arxiv.org/abs/2306.03111)