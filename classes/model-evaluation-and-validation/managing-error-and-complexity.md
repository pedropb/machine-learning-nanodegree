# Managing error and complexity

## Causes of error

Errors are mainly due to 2 common causes:

- Bias: which means a model is unable to represent the whole complexity of the underlying data.
- Variance: whcih means a model is too sensitive due to the limited data it was trained on.

## Error due to Bias - Accuracy and Underfitting

Bias occurs when a model has enough data but is not complex enough to capture the underlying relationships. As a result, the model consistently and systematically misrepresents the data, leading to low accuracy in prediction. This is known as *underfitting*.

To overcome error from bias, we need a more complex model.

## Error due to Variance - Precision and Overfitting

Some variance is normal, but too much variance indicates that the model is unable to generalize its predictions to the larger population. High sensitivity to the training set is also known as *overfitting*, and generally occurs when either the model is too complex or when we do not have enough data to support it.

We can typically reduce the variability of a model's predictions and increase precision by training on more data. If more data is unavailable, we can also control variance by limiting our model's complexity.

