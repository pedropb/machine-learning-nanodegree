# ----------
# 
# As with the previous perceptron exercises, you will complete some of the core
# methods of a sigmoid unit class.
#
# There are two functions for you to finish:
# First, in activate(), write the sigmoid activation function.
# Second, in update(), write the gradient descent update rule. Updates should be
#   performed online, revising the weights after each data point.
# 
# ----------

import numpy as np


class Sigmoid:
    """
    This class models an artificial neuron with sigmoid activation function.
    """

    def __init__(self, weights = np.array([1])):
        """
        Initialize weights based on input arguments. Note that no type-checking
        is being performed here for simplicity of code.
        """
        self.weights = weights

        # NOTE: You do not need to worry about these two attribues for this
        # programming quiz, but these will be useful for if you want to create
        # a network out of these sigmoid units!
        self.last_input = 0 # strength of last input
        self.delta      = 0 # error signal

    @staticmethod
    def logistic(activation):
        return 1/(1+np.exp(-activation))

    def activate(self, values):
        """
        Takes in @param values, a list of numbers equal to length of weights.
        @return the output of a sigmoid unit with given inputs based on unit
        weights.
        """
        
        # YOUR CODE HERE
        
        # First calculate the strength of the input signal.
        strength = np.dot(values, self.weights)
        self.last_input = strength
        
        # TODO: Modify strength using the sigmoid activation function and   
        # return as output signal.
        # HINT: You may want to create a helper function to compute the
        #   logistic function since you will need it for the update function.
        
        return Sigmoid.logistic(strength)
    
    def update(self, values, train, eta=.1):
        """
        Takes in a 2D array @param values consisting of a LIST of inputs and a
        1D array @param train, consisting of a corresponding list of expected
        outputs. Updates internal weights according to gradient descent using
        these values and an optional learning rate, @param eta.
        """

        # TODO: for each data point...
        for X, y_true in zip(values, train):
            # obtain the output signal for that point
            y_pred = self.activate(X)

            # YOUR CODE HERE

            # TODO: compute derivative of logistic function at input strength
            # Recall: d/dx logistic(x) = logistic(x)*(1-logistic(x))
            derivative = Sigmoid.logistic(self.last_input)*(1-Sigmoid.logistic(self.last_input))

            # TODO: update self.weights based on learning rate, signal accuracy,
            # function slope (derivative) and input value
            self.weights = self.weights + eta*(y_true - y_pred)*derivative*X

            

def test():
    """
    A few tests to make sure that the perceptron class performs as expected.
    Nothing should show up in the output if all the assertions pass.
    """
    def sum_almost_equal(array1, array2, tol = 1e-5):
        return sum(abs(array1 - array2)) < tol

    u1 = Sigmoid(weights=[3,-2,1])
    assert abs(u1.activate(np.array([1,2,3])) - 0.880797) < 1e-5
    
    u1.update(np.array([[1,2,3]]),np.array([0]))
    assert sum_almost_equal(u1.weights, np.array([2.990752, -2.018496, 0.972257]))

    u2 = Sigmoid(weights=[0,3,-1])
    u2.update(np.array([[-3,-1,2],[2,1,2]]),np.array([1,0]))
    assert sum_almost_equal(u2.weights, np.array([-0.030739, 2.984961, -1.027437]))

if __name__ == "__main__":
    test()