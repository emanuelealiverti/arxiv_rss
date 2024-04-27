---
layout: post
title: "Extracting Emotion Phrases from Tweets using BART"
date: 2024-04-27
author: Mahdi Rezapour
tags: stat.AP
---

Sentiment analysis is a natural language processing task that aims to identify and extract the emotional aspects of a text. However, many existing sentiment analysis methods primarily classify the overall polarity of a text, overlooking the specific phrases that convey sentiment. In this paper, we applied an approach to sentiment analysis based on a question-answering framework. Our approach leverages the power of Bidirectional Autoregressive Transformer (BART), a pre-trained sequence-to-sequence model, to extract a phrase from a given text that amplifies a given sentiment polarity. We create a natural language question that identifies the specific emotion to extract and then guide BART to pay attention to the relevant emotional cues in the text. We use a classifier within BART to predict the start and end positions of the answer span within the text, which helps to identify the precise boundaries of the extracted emotion phrase. Our approach offers several advantages over most sentiment analysis studies, including capturing the complete context and meaning of the text and extracting precise token spans that highlight the intended sentiment. We achieved an end loss of 87% and Jaccard score of 0.61.

[Read more](https://arxiv.org/abs/2403.14050)