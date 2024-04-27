---
layout: post
title: "Manifold Regularization Classification Model Based On Improved Diffusion Map"
date: 2024-04-27
author: Hongfu Guo, Wencheng Zou, Zeyu Zhang, Shuishan Zhang, Ruitong Wang, Jintao Zhang
tags: stat.ML
---

Manifold regularization model is a semi-supervised learning model that leverages the geometric structure of a dataset, comprising a small number of labeled samples and a large number of unlabeled samples, to generate classifiers. However, the original manifold norm limits the performance of models to local regions. To address this limitation, this paper proposes an approach to improve manifold regularization based on a label propagation model. We initially enhance the probability transition matrix of the diffusion map algorithm, which can be used to estimate the Neumann heat kernel, enabling it to accurately depict the label propagation process on the manifold. Using this matrix, we establish a label propagation function on the dataset to describe the distribution of labels at different time steps. Subsequently, we extend the label propagation function to the entire data manifold. We prove that the extended label propagation function converges to a stable distribution after a sufficiently long time and can be considered as a classifier. Building upon this concept, we propose a viable improvement to the manifold regularization model and validate its superiority through experiments.

[Read more](https://arxiv.org/abs/2403.16059)