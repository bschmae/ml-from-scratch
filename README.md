# ml-from-scratch

1. Implement Linear Regression using only NumPy — no ML libraries.

Learn:
How a model learns weights (coefficients)

What loss functions like Mean Squared Error (MSE) are

How gradient descent works

How to evaluate predictions

    I. What is Linear Regression? 
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
        If the goal is minimizing prediction error in prediction or
        forecasting, linear regression can be used to fit a predictive model to
        an observed data set of values of the response and explanatory variables.
        
        The most common loss function is: 

        Mean Squared Error (MSE)
        MSE = (1/n) * Σ (y - ŷ)²

        n: Number of data points
        y: True output values
        ŷ: Predicted output values

        The MSE is a measure of the quality of an estimator. As it is derived
        from the square of Euclidean distance, it is always a positive value
        that decreases as the error approaches zero. Put simply, we want
        predictions ŷ (estimated values) to be as close to as possible to the
        true value (y).

        Beyond MSE, model performance can be evaluated using metrics like:

        • R² (Coefficient of Determination): Measures how much of the variance
        in the dependent variable is explained by the model (ranges from 0 to 1,
        higher is better).
        • Mean Absolute Error (MAE): Measures the average absolute difference
        between predictions and actual values, which is less sensitive to outliers than MSE.

    III. Gradient Descent is used to update the weights to minimize the MSE.
        It is an interative omptimazation algorithm used to minimize a cost
        function by moving in the direction of the negative gradient.

        What is the gradient? The gradient of a function is a vector that
        contains the partial derivatives with respect to each parameter (weights
        and bias). It tells you the direction of steepest increase in
        the function. 

        partial derivative with respect to weight:
        ∂(MSE)/∂w = (-2/n) * Σ (y - ŷ) * x

        partial derivative with respect to bias:
        ∂(MSE)/∂b = (-2/n) * Σ (y - ŷ)
    
        Or, more beginner friendly explanation, gradient indicates the "slope"
        of the loss function with respect to each parameter, guiding the model
        to adjust weights to reduce error.

        The negative gradient points in the direction of the steepest decrease
        of the cost function. Since we usually want to minimize the cost
        (i.e., reduce prediction error), we move against the gradient.

        For each parameter (weights and bias):

        Update rules
        w = w - α * ∂(MSE)/∂w
        b = b - α * ∂(MSE)/∂b

        Where:
        • w is the weight
        • b is the bias
        • α (alpha) is the learning rate

        What is the learning rate? 
        The learning rate α determines how much the model’s parameters (w and b) are adjusted in the direction of the negative gradient during each iteration of gradient descent.
        α acts as a scaling factor, controlling how large or small each step is.

        The negative gradient (-∂(MSE)/∂w, -∂(MSE)/∂b) ensures we move toward
        the minimum of the loss function.
