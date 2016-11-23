# More decision trees

## Decision tree graph representation

![Graph representation](DT-Graph.png)

## Decision Trees Accuracy

```python
from sklearn import tree
clf = tree.DecisionTreeClassifier(min_samples_split=10)
clf = clf.fit(features_train, labels_train)

from sklearn.metrics import accuracy_score
acc = accuracy_score(labels_test, clf.predict(features_test)) 
```

## Entropy

![Entropy](Entropy.png)

### Calculating Entropy Example

Suppose we have a sample like: `S S F F`, where S is slow and F is fast.
From this sample, we can infer that p<sub>i</sub> of  slow is 0.5

So the entropy could be calculated like:
```python
import math
entropy = 2*( (-0.5) * math.log(0.5, 2)) # resulting in 1
```

## Information Gain

![Information Gain](information-gain.png)