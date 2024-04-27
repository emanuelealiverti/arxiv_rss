---
layout: post
title: "Out-of-Distribution Detection via Deep Multi-Comprehension Ensemble"
date: 2024-04-27
author: Chenhui Xu, Fuxun Yu, Zirui Xu, Nathan Inkawhich, Xiang Chen
tags: stat.ML
---

Recent research underscores the pivotal role of the Out-of-Distribution (OOD) feature representation field scale in determining the efficacy of models in OOD detection. Consequently, the adoption of model ensembles has emerged as a prominent strategy to augment this feature representation field, capitalizing on anticipated model diversity.
  However, our introduction of novel qualitative and quantitative model ensemble evaluation methods, specifically Loss Basin/Barrier Visualization and the Self-Coupling Index, reveals a critical drawback in existing ensemble methods. We find that these methods incorporate weights that are affine-transformable, exhibiting limited variability and thus failing to achieve the desired diversity in feature representation.
  To address this limitation, we elevate the dimensions of traditional model ensembles, incorporating various factors such as different weight initializations, data holdout, etc., into distinct supervision tasks. This innovative approach, termed Multi-Comprehension (MC) Ensemble, leverages diverse training tasks to generate distinct comprehensions of the data and labels, thereby extending the feature representation field.
  Our experimental results demonstrate the superior performance of the MC Ensemble strategy in OOD detection compared to both the naive Deep Ensemble method and a standalone model of comparable size. This underscores the effectiveness of our proposed approach in enhancing the model's capability to detect instances outside its training distribution.

[Read more](https://arxiv.org/abs/2403.16260)