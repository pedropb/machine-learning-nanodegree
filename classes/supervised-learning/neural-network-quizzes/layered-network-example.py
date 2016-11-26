import numpy as np

input = np.array([1,2,3])
h1 = np.array([1,1,-5])
h2 = np.array([3,-4,2])
ol = np.array([2,-1])
print np.array([input.dot(h1), input.dot(h2)]).dot(ol)
# -25
