"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    return np.exp(x) / np.sum(np.exp(x), axis=0)


def test_1():
    scores = [1.0, 2.0, 3.0]
    print scores, softmax(scores)
    print "Test 1: " + ("passed" if [float("{:.8f}".format(i)) for i in softmax(scores)] == [ 0.09003057,  0.24472847,  0.66524096] else "failed")

def test_2():
    scores = np.array([[1, 2, 3, 6],
                       [2, 4, 5, 6],
                       [3, 8, 7, 6]])

    result = softmax(scores)

    r = []
    r1 = result.tolist()
    for i in r1:
        t = []
        for j in i:
            t.append(float("{:.8f}".format(j)))
        r.append(t)
    
    print "Test 2: " + ("passed" if r == [[ 0.09003057,  0.00242826,  0.01587624,  0.33333333],
                               [ 0.24472847,  0.01794253,  0.11731043,  0.33333333],
                               [ 0.66524096,  0.97962921,  0.86681333,  0.33333333]] else "failed")

test_1()

test_2()

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()

