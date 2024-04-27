---
layout: post
title: "Electron-Tunnelling-Noise Programmable Random Variate Accelerator for Monte Carlo Sampling"
date: 2024-04-27
author: James T. Meech, Vasileios Tsoutsouras, Phillip Stanley-Marbell
tags: stat.AP, stat.CO
---

This article presents an electron tunneling noise programmable random variate accelerator for accelerating the sampling stage of Monte Carlo simulations. We used the LiteX framework to generate a Petitbateau FemtoRV RISC-V instruction set soft processor and deploy it on a Digilent Arty-100T FPGA development board. The RISC-V soft processor augmented with our programmable random variate accelerator achieves an average speedup of 8.70 times and a median speedup of 8.68 times for a suite of twelve different benchmark applications when compared to GNU Scientific Library software random number generation. These speedups are achievable because the benchmarks spend an average of 90.0 % of their execution time generating random samples. The results of the Monte Carlo benchmark programs run over the programmable random variate accelerator have an average Wasserstein distance of 1.48 times and a median Wasserstein distance of 1.41 times$that of the results produced by the GNU Scientific Library random number generators. The soft processor samples the electron tunneling noise source using the hardened XADC block in the FPGA. The flexibility of the LiteX framework allows for the deployment of any LiteX-supported soft processor with an electron tunneling noise programmable random variate accelerator on any LiteX-supported development board that contains an FPGA with an XADC.

[Read more](https://arxiv.org/abs/2403.16421)