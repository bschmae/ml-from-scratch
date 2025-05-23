# ml-from-scratch

1. Implement Linear Regression using only NumPy — no ML libraries.

Learn:
How a model learns weights (coefficients)

What loss functions like Mean Squared Error (MSE) are

How gradient descent works

How to evaluate predictions

    I. What is Linear Regression? 
        https://en.wikipedia.org/wiki/Linear_regression

        Linear regression analysis is used to predict the value of one variable
        based on the value of another variable. The variable that you are 
        estimating is the dependent variable or scalar. The variable you are 
        using to calculate your estimate is the independent variable or regressor.

        Linear regression is a supervised learning algorithm used to 
        predict a continuous value from one or more input features.  What does 
        that mean? It learns from the labelled datasets and maps the data points 
        to the most optimized linear functions that can be used for prediction 
        on new datasets.

        The Linear Model
        For 1 feature (univariate): ŷ = w ⋅ x + b
        • ŷ : predicted output
        • w : weight (slope of the line)
        • x : input feature
        • b : bias (y-intercept)

        For multiple features (multivariate): ŷ = X ⋅ w + b
        • X : input matrix

        Note: Different from multivariate linear regression, which uses multiple
        dependent variables instead of one to model relationships.

    II. Goal of Linear Regression
        If the goal is error i.e. variance reduction in prediction or 
        forecasting, linear regression can be used to fit a predictive model to 
        an observed data set of values of the response and explanatory variables.
        
        The most common loss function is: 

        Mean Squared Error (MSE)
        MSE = (1/n) * Σ (y - y_pred)^2

        The MSE is a measure of the quality of an estimator. As it is derived 
        from the square of Euclidean distance, it is always a positive value 
        that decreases as the error approaches zero. Put simply, we want 
        predictions ŷ (estimated values) to be as close to as possible to the 
        true value (y).

    III. Gradient Descent is used to update the weights to minimize the MSE.
        It is an interative omptimazation algorithm used to minimize a cost 
        function by moving in the direction of the negative gradient.

        What is the gradient? The gradient of a function is a vector that
        contains the partial derivatives with respect to each parameter (weights
         and bias). It tells you the direction of steepest increase in 
        the function.

        The negative gradient points in the direction of the steepest decrease 
        of the cost function. Since we usually want to minimize the cost 
        (i.e., reduce prediction error), we move against the gradient.

        For each parameter (weights and bias):

        w = w - α * ∂(MSE)/∂w  
        b = b - α * ∂(MSE)/∂b

        Where:
        w is the weight

        b is the bias

        α (alpha) is the learning rate

        Update rules
        weights = weights - learning_rate * w
        bias = bias - learning_rate * b