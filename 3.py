import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.array([1,-1,0], dtype='f')
        self.bias = np.random.rand(1)
        self.learning_rate = learning_rate
    
    def activation(self, x):
        return 1 if x >= 0 else -1
    
    def predict(self, x):
        z = np.dot(x, self.weights) + self.bias
        return self.activation(z)
    
    def fit(self, X, y):
        errsum=0
        for x, target in zip(X, y):
            prediction = self.predict(x)
            error = target - prediction
            errsum=errsum+error
            self.weights += self.learning_rate * error * x
            self.bias += self.learning_rate * error
        return errsum
        

# Input data
X = np.array([[1, 0, 1], [0, -1, -1], [-1, -0.5, -1]], dtype='f')
y = np.array([-1, 1, 1], dtype='f')

# Train the perceptron
p = Perceptron(input_size=3)
err=1
while err!=0:
    err= p.fit(X, y)

# Test the perceptron
inputs = np.array([[1, 0, 1], [1, -1, -1], [-1, -0.5, -1], [-1, -1, 1]], dtype='f')
for x in inputs:
    prediction = p.predict(x)
    print(f"Input: {x}, Prediction: {prediction}")
