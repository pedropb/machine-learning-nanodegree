Given:
- inputs: [x, y]
- hidden layer: [[3,2], [-1,4], [3,-5]]
- output layer: [1,2,-1]

Write down a single node 2x1, that computes the same result as above.

**Answer**

3x+2y + 2*(-x + 4y) - (3x -5y)
3x + 2y - 2x + 8y - 3x + 5y
-2x + 15y -> [-2, 15]