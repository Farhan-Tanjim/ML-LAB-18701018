import numpy as np

def predict(X, weights, bias):
    """
    Make a prediction given input X and weights
    """
    z = np.dot(X, weights) + bias
    return np.where(z >= 0, 1, -1)

def train_weights(X, y, weights, bias, learning_rate, epochs):
    """
    Train the weights using the Perceptron rule
    """
    for _ in range(epochs):
        for i in range(X.shape[0]):
            prediction = predict(X[i], weights, bias)
            if prediction != y[i]:
                weights += learning_rate * y[i] * X[i]
                bias += learning_rate * y[i]
    return weights, bias

# Input vectors
X = np.array([[2, 2], [1, -2], [-2, 2], [-1, 1]])
# Labels
y = np.array([1, 1, -1, -1])
# Initial weights and bias
weights = np.zeros(X.shape[1])
bias = 0
# Learning rate and number of epochs
learning_rate = 1
epochs = 100

weights, bias = train_weights(X, y, weights, bias, learning_rate, epochs)
# Print the weight and bias values
print("Weights:", weights)
print("Bias:", bias)

# Make a prediction for the input vector [2 2]
input_vector = np.array([-2, 2])
prediction = predict(input_vector, weights, bias)
print("Prediction for [2, 2]: ", prediction)
