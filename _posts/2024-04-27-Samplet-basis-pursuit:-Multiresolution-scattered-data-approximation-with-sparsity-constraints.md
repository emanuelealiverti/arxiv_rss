---
layout: post
title: "Samplet basis pursuit: Multiresolution scattered data approximation with sparsity constraints"
date: 2024-04-27
author: Davide Baroli, Helmut Harbrecht, Michael Multerer
tags: stat.ML
---

We consider scattered data approximation in samplet coordinates with $\ell_1$-regularization. The application of an $\ell_1$-regularization term enforces sparsity of the coefficients with respect to the samplet basis. Samplets are wavelet-type signed measures, which are tailored to scattered data. They provide similar properties as wavelets in terms of localization, multiresolution analysis, and data compression. By using the Riesz isometry, we embed samplets into reproducing kernel Hilbert spaces and discuss the properties of the resulting functions. We argue that the class of signals that are sparse with respect to the embedded samplet basis is considerably larger than the class of signals that are sparse with respect to the basis of kernel translates. Vice versa, every signal that is a linear combination of only a few kernel translates is sparse in samplet coordinates. Therefore, samplets enable the use of well-established multiresolution techniques on general scattered data sets.
  We propose the rapid solution of the problem under consideration by combining soft-shrinkage with the semi-smooth Newton method. Leveraging on the sparse representation of kernel matrices in samplet coordinates, this approach converges faster than the fast iterative shrinkage thresholding algorithm and is feasible for large-scale data. Numerical benchmarks are presented and demonstrate the superiority of the multiresolution approach over the single-scale approach. As large-scale applications, the surface reconstruction from scattered data and the reconstruction of scattered temperature data using a dictionary of multiple kernels are considered.

[Read more](https://arxiv.org/abs/2306.10180)