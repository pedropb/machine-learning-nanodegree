# Deep Neural Networks

Linear models provide various benefits:

![Linear Model Complexity](images/deep-neural-networks/linear-model-complexity.png)

![Linear Models are linear](images/deep-neural-networks/linear-models-are-linear.png)

![Linear Models are efficient](images/deep-neural-networks/linear-models-are-efficient.png)

![Linear Models are stable](images/deep-neural-networks/linear-models-are-stable-1.png)

![Linear Models are stable](images/deep-neural-networks/linear-models-are-stable-2.png)

So we want to keep using linear models. But we need to introduce some non-linearity into these models to better represent other functions. Multiplying `W` by linear functions, doesn't solve this problem.

![Linear Models are here to stay](images/deep-neural-networks/linear-models-stay.png)

![Linear Models are here to stay](images/deep-neural-networks/linear-models-stay-2.png)

The easiest way to introduce non-linearities is to use the Rectified Linear Unit functions (RELU).

![RELU](images/deep-neural-networks/relus.png)

And the derivative from this function is also easy to compute.

![RELU Derivative](images/deep-neural-networks/relus-derivative.png)

So using RELUs, we can introduce non-linearities into our model and build our first neural network.

![Neural Network with RELUs](images/deep-neural-networks/neural-network-relus.png)

But where are the neurons?

![Neural Network Question](images/deep-neural-networks/neural-network-question.png)

In this class, we won't make analogies to the biological neuroscience side of neural networks. Instead, we will focus on the math behind it, and how we can use GPUs to make them work with little effort as possible.

## Neural Networks

![2-layer neural network](images/deep-neural-networks/2-layer-neural-network.png)

**Note**: Depicted above is a "2-layer" neural network:

1. The first layer effectively consists of the set of weights and biases applied to X and passed through ReLUs. The output of this layer is fed to the next one, but is not observable outside the network, hence it is known as a *hidden layer*.
2. The second layer consists of the weights and biases applied to these intermediate outputs, followed by the softmax function to generate probabilities.