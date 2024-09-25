# Lecture 5: Autoencoders and Variational Autoencoders

## Overview 🌐

This lecture delves into the realm of Autoencoders (AEs) and Variational Autoencoders (VAEs), key models in unsupervised learning that are essential for understanding data compression and generation. We'll explore the underlying principles that enable these networks to learn efficient representations and generate new data instances that are similar to the ones they were trained on.

## Resources 📚

- [Lecture Slides](./ae.pdf) (pptx version: [here](./ae.pptx))
- [ex1.ipynb](./ex1.ipynb) Solution to the first exercise
- [ex2.ipynb](./ex2.ipynb) Solution to the second exercise
- [ex2_logvar.ipynb](./ex2_logvar.ipynb) Solution to the second exercise with the encoder producing log(std^2) instead of std, numerically more stable


## YouTube Videos 📹:

- [AE in two minutes](https://www.youtube.com/watch?v=Rdpbnd0pCiI) good video from two minutes papers
- [VAE from Arxiv Insights](https://www.youtube.com/watch?v=9zKuYvjFFS8) VAEs and reparameterization trick

## Key Topics Covered 🧠

1. **Autoencoders (AEs):**
   - The architecture of autoencoders: encoder, bottleneck, and decoder.
   - Loss functions and the idea of data compression and reconstruction.

2. **Denoising Autoencoders (DAEs):**
   - Introduction to Denoising Autoencoders and their role in removing noise from data.

3. **Variational Autoencoders (VAEs):**
   - The theory behind VAEs and how they differ from traditional AEs.
   - The reparameterization trick and its importance.
   - Application of VAEs in generative tasks.
   - KL-divergence

## Learning Objectives 🎓

- Understand the structure and purpose of an Autoencoder and how it can be used to compress and reconstruct data.
- Grasp the principles of Variational Autoencoders, including their probabilistic foundations and how they enable data generation.
- Learn how Denoising Autoencoders works and how to train and use them.
- Develop hands-on experience by implementing simple AE and VAE models.
- Explore the potential applications of AEs and VAEs in various domains such as image denoising, dimensionality reduction, and generative modeling.
