# Model Evaluation and Validation

## SKLearn: Train and Test split data

We split data into training sets and testing sets, so we don't overfit the model to a single set of data. That way our model is more resilient to changes in the data and can infer better results onto data not seen before.

```python
# scikit 0.17
from sklearn.cross_validation import train_test_split
train_x, test_x, train_y, test_y = \
    train_test_split(data, target, test_size, random_state)

# scikit 0.18
from sklearn.model_selection import train_test_split
train_x, test_x, train_y, test_y = \
    train_test_split(data, target, test_size, random_state)
```

[Official Documentation](http://scikit-learn.org/stable/modules/cross_validation.html)

## Confusion Matrix

Confusion Matrix is the matrix composed by the results plotted on predicted vs real axis. For example, given the following matrix:

```
    45 32
    20 67
```

We can observe that:
- 45 were labeled correctly as Negative (aka `True Negative`)
- 32 were labeled incorrectly as Positive (aka `False Positive`)
- 20 were labeled incorrectly as Negative (aka `False Negative`)
- 67 were labeled correctly as Positive (aka `True Positive`)

## Recall

**Recall** is the fraction given by: `True Positives / (True Positives + False Negatives)`

## Precision

**Precision** is the fraction given by: `True Positives / (True Positives + False Positives)`  

## F1 Score

**F1 score** is the weighted average between precision and recall: `F1 = 2 * (precision * recall) / (precision + recall)`

## Mean Absolute Error

For continuous data, we need to care how close the prediction is. For this, we can use **Mean Absolute Error**, which is the sum of the absolute deviations from the corresponding data points divided by the number of data points.

