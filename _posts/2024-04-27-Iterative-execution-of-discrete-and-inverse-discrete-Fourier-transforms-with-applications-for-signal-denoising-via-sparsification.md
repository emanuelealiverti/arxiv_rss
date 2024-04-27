---
layout: post
title: "Iterative execution of discrete and inverse discrete Fourier transforms with applications for signal denoising via sparsification"
date: 2024-04-27
author: H. Robert Frost
tags: stat.ME
---

We describe a family of iterative algorithms that involve the repeated execution of discrete and inverse discrete Fourier transforms. One interesting member of this family is motivated by the discrete Fourier transform uncertainty principle and involves the application of a sparsification operation to both the real domain and frequency domain data with convergence obtained when real domain sparsity hits a stable pattern. This sparsification variant has practical utility for signal denoising, in particular the recovery of a periodic spike signal in the presence of Gaussian noise. General convergence properties and denoising performance relative to existing methods are demonstrated using simulation studies. An R package implementing this technique and related resources can be found at https://hrfrost.host.dartmouth.edu/IterativeFT.

[Read more](https://arxiv.org/abs/2211.09284)