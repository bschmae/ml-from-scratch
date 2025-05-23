import argparse
import random

class UnivariateLinearRegression:
    def __init__(self, learning_rate=0.01, n_iterations=1000):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.weight = 0.0 # Scalar weight
        self.bias = 0.0 # Scalar bias
        self.mse_history = []

    def fit(self, X, y):
        """
        Train univariate linear regression using gradient descent.
        X: List of input features (length n_samples)
        y: List of target values (length n_samples)
        """
        n_samples = len(X)

        # Gradient descent
        print('Starting gradient descent.')
        for _ in range(self.n_iterations):
            # Compute predictions
            y_pred = self.predict(X)

            # Compute gradients
            # ∂(MSE)/∂w = (-2/n) * Σ (y - ŷ) * x
            # ∂(MSE)/∂b = (-2/n) * Σ (y - ŷ)
            dw = 0.0
            db = 0.0

            for i in range(n_samples):
                error = y[i] - y_pred[i]
                dw += error * X[i]
                db += error

            dw = (-2 / n_samples) * dw
            db = (-2 / n_samples) * db

            # Update parameters
            self.weight -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

            # Compute MSE for monitoring
            mse = sum((y[i] - y_pred[i]) ** 2 for i in range(n_samples)) / n_samples
            self.mse_history.append(mse)

        print('Gradient descent complete.')

    def predict(self, X):
        """Predict using the trained model."""
        #  ŷ = w ⋅ x + b
        return [self.weight * x + self.bias for x in X]

    def mean_squared_error(self, y_true, y_pred):
        """Compute Mean Squared Error."""
        n = len(y_true)
        return sum((y_true[i] - y_pred[i]) ** 2 for i in range(n)) / n

def main():
    # Set up argument parser
    parser = \
        argparse.ArgumentParser(description="Train a linear regression model.")
    parser.add_argument('--lr', type=float, default=0.01,
                        help='Learning rate for gradient descent (default: 0.01)')
    parser.add_argument('--its', type=int, default=1000,
                        help='Number of iterations for gradient descent (default: 1000)')
    parser.add_argument('--test_size', type=float, default=0.2,
                        help='Fraction of data for test set (default: 0.2)')
    parser.add_argument('--seed', type=int, default=42,
                        help='Random seed for reproducibility (default: 42)')
    parser.add_argument('--n_samples', type=int, default=100,
                        help='Number of samples for synthetic data')

    # Parse arguments
    args = parser.parse_args()
    # print('Ran with args:', args)

    random.seed(args.seed)

    #  Generate synthetic data
    X = [2 * random.random() for _ in range(args.n_samples)]

    # y = 4 + 3x + noise
    # random.gauss(0, 1): Gaussian noise with mean 0 and standard deviation 1,
    # adding randomness to simulate real-world data variability
    y = [4 + 3 * x + random.gauss(0, 1) for x in X]
    print('Generated synthetic data.')

    # Train-test split
    train_size = int((1 - args.test_size) * len(X))
    X_train, X_test = X[:train_size], X[train_size:]
    y_train, y_test = y[:train_size], y[train_size:]

    # Train the model
    model = UnivariateLinearRegression(learning_rate=args.lr, n_iterations=args.its)
    model.fit(X_train, y_train)
    print('Training complete.')

    y_pred = model.predict(X_test)

    # In main, after evaluation
    print(f"Learned weight: {model.weight:.4f}")  # Should be ~3
    print(f"Learned bias: {model.bias:.4f}")     # Should be ~4
    print(f"Mean Squared Error: {model.mean_squared_error(y_test, y_pred):.4f}")

if __name__ == "__main__":
    main()
