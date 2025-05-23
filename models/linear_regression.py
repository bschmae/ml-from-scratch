import numpy as np

class LinearRegression:
    # lr : learning rate
    # n_its : number of interations
    def __init__(self, lr=0.01, n_its=1000):
        self.lr = lr
        self.n_its = n_its
        self.weights = None
        self.bias = None

    def fit(self, X, y):
        # Gradient Descent implementation goes here
        pass

    def predict(self, X):
        return np.dot(X, self.weights) + self.bias
