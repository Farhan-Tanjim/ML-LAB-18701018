import numpy as np

# Define training data
X = np.array([[2, 2], [1, -2], [-2, 2], [-1, 1]])
y = np.array([0, 1, 0, 1])

# Define initial weight and bias
w = np.array([0, 0])
b = 0

# Define hardlimit function
def hardlim(x):
    return 1 if x >= 0 else 0

# Train the perceptron
r = np.zeros(y.shape)
print(r)
while not np.array_equal(r, y):
    for i in range(len(X)):
        a = hardlim(np.dot(w, X[i]) + b)
        r[i] = a
        if a != y[i]:
            e = y[i] - a
            w = w + e * X[i]
            b = b + e

# Print final weight and bias
print(f'Final weight: {w}')
print(f'Final bias: {b}')