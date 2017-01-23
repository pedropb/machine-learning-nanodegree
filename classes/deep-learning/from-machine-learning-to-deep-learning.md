# From Machine Learning to Deep Learning

## Training your Logistic Classifier

A Logistic Classifier is a function that outputs scores for a given input. It is trained by adapting the weights and the bias.

![Logistic Classifier](images/logistic-classifier.png)

When we train a classifier, we want to output probabilities, instead of scores. This probabilities will be checked against a threshold so that we have a binary classification.

![Probabilities Classifier](images/probabilities-classifier.png)

To transform scores into probabilities we can use a softmax function as described below.

![Softmax Function](images/softmax.png)

## Cross Entropy

![One Hot Encoding Problem](images/cross-entropy-intro.png)

![Cross Entropy Definition](images/cross-entropy-definition.png)

![Multinomial Logistic Classification Recap](images/multinomial-logistic-classification-recap.png)

![Multinomial  Logistic Classification](images/multinomial-logistic-classification.png)

## Minimizing Cross Entropy

We want to find the `W` and `b` that provide a high distance to the incorrect class while having a low distance to the correct class.

![Intro](images/minimizing-cross-entropy-intro.png)

For this, we define something called `loss function`:

![Loss Function](images/loss-function-cross-entropy.png)

This loss function is the average cross-entropy of all our data, so it is a big expensive operation. To understand how to minimize this function, suppose we could represent it in terms of 2 weights (W and b):

![Loss Function Representation](images/loss-function-representation.png)

Now we turned our machine learning problem into a numerical optimization problem. We have to find the 2 weights that provide the minimal loss function. And we can do this using gradient descent.

![Gradient descent solution](images/gradient-descent-solver.png)

## Normalized Inputs And Initial Weights

When handling big data, we have to be aware of rounding problems, while handling very big and small numbers simultaneously. As a good practice, we want our variables to have zero mean and equal variance, whenever possible.

![Zero mean](images/zero-mean.png)

This well-conditioned variables make it easier for optimizers to find a solution for the problem.

![Well conditioned variables](images/well-conditioned.png)

On images, we can normalize the data by subtracting and dividing each channel by 128. This helps the optimizer to converge on a solution faster.

![Normalizing Images](images/normalizing-images.png)

The same idea applies to the weight initialization for the logistic function. Using gaussian distributions and small standard deviations, select the weights. Small sigmas represent more uncertainty, while large sigmas, represent more bias.

![Weight initialization](images/weight-initialization.png)

So now we know all steps for initializing the Logistic Classifier.

![Logistic Classifier initialization](images/logistic-classifier-initialization.png)

And the optimization steps consist of taking the derivative of the loss function on each weight and updating the weight to its new value, hence and repeat.

![optimization steps](images/optimization-steps.png)

## Validation Test Set Size Continued

As a rule of the thumb, a change in the model that affects the classification of less than 30 samples can be interpreted as noise. In contrast, a change that affects 30 or more samples, can be interpreted as a gain in accuracy for the model. Because of this, a validation set should have at least 30,000 samples, so that we can measure gains of 0.1% in accuracy.

![Validation Test Set Size](images/validation-test-size.png)

## Stochastic Gradient Descent

Stochastic Gradient Descent is an alternative to Gradient Descent. It is a trade-off in in which we select a tiny random sample from the dataset to compute the global loss function and the derivative faster and, instead of taking tens of large steps to find the minimum optiaml function, we take hunderds to thousands smaller steps.

 ![Gradient Descent](images/gd-vs-sgd-1.png)

 ![Stochastic Gradient Descent](images/gd-vs-sgd-2.png)

 Usually we prefer SGD to GD, because it scales better with model and data size, and we want both on deep learning.