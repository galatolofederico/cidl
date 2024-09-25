# Questions you must know the answers to before attending the exam. 

## a. Autograd and SGD

- **a.01** What is the principle behind using Stochastic Gradient Descent (SGD) for optimizing a function w.r.t. its parameters?
- **a.02** Explain the concept of function composition in neural networks and how it relates to layers in a model.
- **a.03** How do you calculate the derivative of a composed function w.r.t. its inputs?
- **a.04** Describe the unfolding process of a function and its impact on derivative calculation.
- **a.05** Provide an example of applying the chain rule with multiple variables and binary operators in differentiation.
- **a.06** Explain the derivation process for a function involving a binary operator and how it splits the derivation flow.
- **a.07** What is reverse mode differentiation, and how is it applied to compute derivatives in computational graphs?
- **a.08** Discuss the concept of forward path and backward path in the context of computational graphs and differentiation.
- **a.09** Describe the differences between forward mode differentiation and reverse mode differentiation in terms of computational efficiency and application.
- **a.10** How do machine learning frameworks utilize reverse mode differentiation, and what advantages does this offer for building complex architectures?
- **a.11** Draw the computational graph of this expression ...
- **a.12** Perform the reverse mode differentiation on that CG
- **a.13** Perform the forward mode differentiation on that CG
- **a.14** Draw a one-dimensional loss function w.r.t. one parameter. Perform one step of SGD

## b. Tensor algebra and PyTorch

- **b.01** Explain the concept of a tensor in PyTorch.
- **b.02** How do the addition and multiplication between tensors work?
- **b.03** What is the difference between the 'reshape' and 'view' methods in tensor manipulation?
- **b.04** Explain the use of reduction operations like '.sum', '.mean', '.max', etc., in tensor algebra.
- **b.05** Describe the process of creating a custom dataset using 'torch.utils.data.Dataset'.
- **b.06** What is the 'torch.utils.data.IterableDataset' and how is it used?
- **b.07** How does the 'torch.utils.data.DataLoader' work in PyTorch?
- **b.08** Describe the structure and purpose of the 'torch.nn.Module' class.
- **b.09** What are the key methods in a PyTorch module, and how are they implemented?
- **b.10** Discuss the training process in PyTorch using the Stochastic Gradient Descent (SGD) algorithm.
- **b.11** Explain the concept and application of batch size in model training.
- **b.12** How do you implement a simple linear regression model in PyTorch?
- **b.13** Discuss the implementation of a custom model in PyTorch and the steps to train it on a dataset.

## c. Convolutional Neural Networks and ResNets

- **c.01** What is a CNN?
- **c.02** How does the convolution operation work in CNNs?
- **c.03** Explain the significance of kernel size, padding, and stride in convolutional layers.
- **c.04** What are the roles of pooling layers in CNNs?
- **c.05** Discuss the function of activation functions in CNNs.
- **c.06** How does a Conv2D layer in PyTorch operate?
- **c.07** Explain the concept of channels in CNNs and their significance.
- **c.08** What are skip connections in CNNs, and how do they function?
- **c.09** Define a Residual Network (ResNet) and its advantages in deep learning.
- **c.10** Draw a diagram of a ResNet and its computational graph
- **c.11** Explain the concept of feature maps in CNNs
- **c.12** Describe the architecture of a typical CNN.
- **c.13** What are the common challenges in training deep CNNs?
- **c.14** How do residual blocks in ResNets mitigate the vanishing gradient problem?
- **c.15** Discuss the application of CNNs in image classification tasks, with an example like MNIST.
- **c.16** How does the structure of a ResNet differ from a standard CNN?

## d. Recurrent Neural Networks

- **d.01** What is a Recurrent Neural Network (RNN), and how does it work?
- **d.02** Explain the concept of time-varying inputs and outputs in RNNs.
- **d.03** Describe two major application families of RNNs: Sequence to Task and Sequence to Sequence.
- **d.04** How do RNNs capture temporal dependencies and patterns in sequences?
- **d.05** Discuss the vanishing gradient problem in RNNs and its impact on learning from long sequences.
- **d.06**  Draw a diagram of a RNN and its computational graph
- **d.07** What are Long Short-Term Memory (LSTM) networks and how do they address the vanishing gradient problem?
- **d.08** What are Gated Recurrent Unit (GRU) networks and how do they differ from LSTMs?
- **d.09** Describe the functionality of the three gates in GRUs: reset, update, and new gate.
- **d.10** Explain how to train an RNN for a sequence classification problem.
- **d.11** Discuss the considerations for setting up RNNs, LSTMs, and GRUs for a classification task
- **d.12** Discuss the challenges in training RNNs and how they can be mitigated.

## e. Autoencoders and VAEs

- **e.01** What is an autoencoder, and what are its primary components?
- **e.02** Describe the roles of the encoder and decoder in an autoencoder.
- **e.03** What is meant by the "latent space" in an autoencoder?
- **e.04** How does an autoencoder learn a compact representation of input data?
- **e.05** Discuss the concept of reconstruction error in autoencoders.
- **e.06** What is a denoising autoencoder, and how does it differ from a traditional autoencoder?
- **e.07** What are Variational Autoencoders, and how do they differ from regular autoencoders?
- **e.08** How does the Reparametrization Tick work?
- **e.09** Draw a diagram of a VAE and its computational graph
- **e.10** Why VAEs are a 'generative' architecture?
- **e.11** What is the Kullback-Leibler divergence, and how is it used in VAEs?
- **e.12** Describe a practical implementation of training a simple autoencoder on the MNIST dataset.
- **e.13** Explain the procedure for training a Variational Autoencoder on the MNIST dataset.
- **e.14** How does the 'Face Swap' algorithm work?

## f. Vector Quantized Variational Autoencoders

- **f.01** What is a Vector Quantized Variational Autoencoder (VQ-VAE)?
- **f.02** Explain the process of mapping input data to a continuous latent space and then to discrete codes in a VQ-VAE.
- **f.03** How does the vector quantization process work in a VQ-VAE, and what is the role of the codebook?
- **f.04** How does the quantization trick work?
- **f.05** Draw a diagram of a VQ-VAE and its computational graph
- **f.06** Describe the function of the 'cdist' function in PyTorch in the context of VQ-VAEs.
- **f.07** What is the responsibility of the decoder in a VQ-VAE, and how does it utilize discrete codes for data reconstruction or generation?
- **f.08** Discuss the types of losses used in training a VQ-VAE, specifically reconstruction, codebook, and commitment loss.
- **f.09** Explain the practical steps involved in training a VQ-VAE on the MNIST dataset.
- **f.10** Explain how to generate images from random codes in a VQ-VAE and the insights it provides.

## g. Generative Adversarial Networks

- **g.01** What are Generative Adversarial Networks?
- **g.02** Describe the architecture of GANs, including the roles of the generator and discriminator.
- **g.03** Explain how the discriminator functions as a binary classifier in GANs.
- **g.04** Outline the steps involved in training the discriminator in a GAN.
- **g.05** Explain the training process of the generator in a GAN.
- **g.06** Draw a diagram of a GAN and its computational graph
- **g.07** What is an Auxiliary Classifier GAN (ACGAN), and how does it differ from standard GANs?
- **g.08** Discuss the challenges in training GANs and strategies to overcome them.
- **g.09** Describe the process of training a Deep Convolutional GAN (DCGAN) on the MNIST dataset.
- **g.10** How can the balance between randomness and class information be maintained in an ACGAN?

## h. Advanced Architectures

- **h.01** What is YOLO (You Only Look Once) in the context of object detection, and how does it perform real-time detection?
- **h.02** Explain how YOLO divides an image into a grid for object detection and how it predicts bounding boxes and class probabilities.
- **h.03** Describe Non-Maximum Suppression (NMS) and its role in object detection.
- **h.04** What is Faster R-CNN, and how does it combine a Region Proposal Network (RPN) with a CNN?
- **h.05** Explain the U-Net architecture and its application in semantic image segmentation.
- **h.06** What is CLIP (Contrastive Language-Image Pretraining) by OpenAI, and how does it combine vision and language?
- **h.07** Discuss Denoising Diffusion Probabilistic Models (DDPM) and Latent Diffusion, and their role in generating high-quality samples.
- **h.08** Describe the DALL-E 2 architecture