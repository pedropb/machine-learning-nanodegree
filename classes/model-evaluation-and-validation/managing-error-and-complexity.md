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

## Overfitting vs Underfitting

![](http://scikit-learn.org/stable/_images/sphx_glr_plot_underfitting_overfitting_0011.png)

## Curse of Dimensionality

As the number of features or dimensions grows, the amount of data we need to generalize accurately grows exponentially.

## Learning Curves - Identifying Bias and Variance

### Bias
When the training and testing errors converge and are quite high this usually means the model is biased. No matter how much data we feed it, the model cannot represent the underlying relationship and therefore has systematic high errors.

### Variance
When there is a large gap between the training and testing error this generally means the model suffers from high variance. Unlike a biased model, models that suffer from variance generally require more data to improve. We can also limit variance by simplifying the model to represent only the most important features of the data.