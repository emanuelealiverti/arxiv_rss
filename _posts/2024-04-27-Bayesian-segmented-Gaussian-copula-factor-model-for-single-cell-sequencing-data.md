---
layout: post
title: "Bayesian segmented Gaussian copula factor model for single-cell sequencing data"
date: 2024-04-27
author: Junsouk Choi, Hee Cheol Chung, Irina Gaynanova, Yang Ni
tags: stat.ME
---

Single-cell sequencing technologies have significantly advanced molecular and cellular biology, offering unprecedented insights into cellular heterogeneity by allowing for the measurement of gene expression at an individual cell level. However, the analysis of such data is challenged by the prevalence of low counts due to dropout events and the skewed nature of the data distribution, which conventional Gaussian factor models struggle to handle effectively. To address these challenges, we propose a novel Bayesian segmented Gaussian copula model to explicitly account for inflation of zero and near-zero counts, and to address the high skewness in the data. By employing a Dirichlet-Laplace prior for each column of the factor loadings matrix, we shrink the loadings of unnecessary factors towards zero, which leads to a simple approach to automatically determine the number of latent factors, and resolve the identifiability issue inherent in factor models due to the rotational invariance of the factor loadings matrix. Through simulation studies, we demonstrate the superior performance of our method over existing approaches in conducting factor analysis on data exhibiting the characteristics of single-cell data, such as excessive low counts and high skewness. Furthermore, we apply the proposed method to a real single-cell RNA-sequencing dataset from a lymphoblastoid cell line, successfully identifying biologically meaningful latent factors and detecting previously uncharacterized cell subtypes.

[Read more](https://arxiv.org/abs/2403.15983)