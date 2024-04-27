---
layout: post
title: "Agile gesture recognition for low-power applications: customisation for generalisation"
date: 2024-04-27
author: Ying Liu, Liucheng Guo, Valeri A. Makarovc, Alexander Gorbana, Evgeny Mirkesa, Ivan Y. Tyukin
tags: stat.AP
---

Automated hand gesture recognition has long been a focal point in the AI community. Traditionally, research in this field has predominantly focused on scenarios with access to a continuous flow of hand's images. This focus has been driven by the widespread use of cameras and the abundant availability of image data. However, there is an increasing demand for gesture recognition technologies that operate on low-power sensor devices. This is due to the rising concerns for data leakage and end-user privacy, as well as the limited battery capacity and the computing power in low-cost devices. Moreover, the challenge in data collection for individually designed hardware also hinders the generalisation of a gesture recognition model.
  In this study, we unveil a novel methodology for pattern recognition systems using adaptive and agile error correction, designed to enhance the performance of legacy gesture recognition models on devices with limited battery capacity and computing power. This system comprises a compact Support Vector Machine as the base model for live gesture recognition. Additionally, it features an adaptive agile error corrector that employs few-shot learning within the feature space induced by high-dimensional kernel mappings. The error corrector can be customised for each user, allowing for dynamic adjustments to the gesture prediction based on their movement patterns while maintaining the agile performance of its base model on a low-cost and low-power micro-controller. This proposed system is distinguished by its compact size, rapid processing speed, and low power consumption, making it ideal for a wide range of embedded systems.

[Read more](https://arxiv.org/abs/2403.15421)