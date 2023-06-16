import numpy as np

class Perceptron:
    def __init__(self, input_size):
        #self.weights = np.random.rand(input_size)
        self.weights = [0,1,0]
        self.bias = 0
        #self.bias = np.random.rand(1)
    
    def activation(self, x): #hardlim
        return 1 if x >= 0 else 0
    
    def predict(self, x):
        z = np.dot(x, self.weights) + self.bias
        return self.activation(z)
    
    def fit(self, X, y):
        for x, target in zip(X, y):
            prediction = self.predict(x)
            #error = target - prediction
            #self.weights += error * x
            #self.bias +=  error

# Input data

# shape: round 1 & elliptical -1
# texture: smooth 1 & rough -1
# weight: 1 pound 1 & less than 1 pound -1

# apple 1 1 -1    >> 1
# orange 1 -1 -1  >> 0


X = np.array([[1, 1, 1], [1, -1, 1], [-1, 1, -1], [-1, -1, -1]])
y = np.array([1, 0, 0, 1])

dict1={0: "orange",1: "apple"}
shape={1: "round", -1: "elliptical"}
texture={1: "smooth", -1: "rough"}
weight={1: "1 pound", -1: "< 1 pound"}

# Train the perceptron
p = Perceptron(input_size=3)
for _ in range(100):
    p.fit(X, y)

# Test the perceptron
inputs = np.array([[1, 1, 1], [1, -1, -1], [-1, 1, -1], [-1, -1, 1]])
for x in inputs:
    prediction = p.predict(x)
    print(f"Input: {x}, [{shape[x[0]]}, {texture[x[1]]}, {weight[x[2]]}]")
    print(f"Prediction: {prediction}  {dict1[prediction]}")

print()
print()

print("Enter the features of your fruit:")
print("Is it round?(y/n)")
shapex=np.where(input()=="y",1,-1)

print("Is it smooth?(y/n)")
texturex=np.where(input()=="y",1,-1)

print("Is it of 1 pound?(y/n)")
weightx=np.where(input()=="y",1,-1)


x=[int(shapex),int(texturex),int(weightx)]
prediction = p.predict(x)
print(f"Input: {x}, [{shape[int(shapex)]}, {texture[int(texturex)]}, {weight[int(weightx)]}]")
print(f"Prediction: {prediction}  {dict1[prediction]}")

