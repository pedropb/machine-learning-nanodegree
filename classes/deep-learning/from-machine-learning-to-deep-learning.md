# From Machine Learning to Deep Learning

## Training your Logistic Classifier

A Logistic Classifier is a function that outputs scores for a given input. It is trained by adapting the weights and the bias.

![Logistic Classifier](images/logistic-classifier.png)

When we train a classifier, we want to output probabilities, instead of scores. This probabilities will be checked against a threshold so that we have a binary classification.

![Probabilities Classifier](images/probabilities-classifier.png)

To transform scores into probabilities we can use a softmax function as described below.

![Softmax Function](images/softmax-function.png)