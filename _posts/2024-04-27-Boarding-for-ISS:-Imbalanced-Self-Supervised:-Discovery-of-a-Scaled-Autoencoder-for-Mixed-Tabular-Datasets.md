---
layout: post
title: "Boarding for ISS: Imbalanced Self-Supervised: Discovery of a Scaled Autoencoder for Mixed Tabular Datasets"
date: 2024-04-27
author: Samuel Stocksieker, Denys Pommeret, Arthur Charpentier
tags: stat.ML
---

The field of imbalanced self-supervised learning, especially in the context of tabular data, has not been extensively studied. Existing research has predominantly focused on image datasets. This paper aims to fill this gap by examining the specific challenges posed by data imbalance in self-supervised learning in the domain of tabular data, with a primary focus on autoencoders. Autoencoders are widely employed for learning and constructing a new representation of a dataset, particularly for dimensionality reduction. They are also often used for generative model learning, as seen in variational autoencoders. When dealing with mixed tabular data, qualitative variables are often encoded using a one-hot encoder with a standard loss function (MSE or Cross Entropy). In this paper, we analyze the drawbacks of this approach, especially when categorical variables are imbalanced. We propose a novel metric to balance learning: a Multi-Supervised Balanced MSE. This approach reduces the reconstruction error by balancing the influence of variables. Finally, we empirically demonstrate that this new metric, compared to the standard MSE: i) outperforms when the dataset is imbalanced, especially when the learning process is insufficient, and ii) provides similar results in the opposite case.

[Read more](https://arxiv.org/abs/2403.15790)