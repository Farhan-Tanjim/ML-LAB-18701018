import numpy as np

def hamming_network(input_vector, weight_matrix):
    # Calculate the dot product of the input vector and weight matrix
    # here the weight matrix is build out of prototype patterns
    dot_product = np.dot(weight_matrix,np.transpose(input_vector))

    R=input_vector.size
    output = np.add(dot_product,np.transpose([R,R]))
    return output

def poslin(input):
    return np.where(input >= 0, input, 0)

def train_network(feedforward_output, weight_matrix):
    # Calculate the dot product of the input vectors and their transpose
    dot_product = np.dot(weight_matrix, np.transpose(feedforward_output))
    # Update the weight matrix using the Hebbian rule
    return poslin(dot_product)

def recognize_fruit(input_vector, weight_matrix):
    # Initialize the previous output as the input vector
    prev_output = input_vector
    # Keep updating the output until it converges
    while True:
        output = train_network(prev_output, weight_matrix)
        if np.array_equal(output, prev_output):
            break
        prev_output = output
    return output

# Initialize the input vectors for bananas and pineapples
fruit_array=["banana","pineapple"]
banana = np.array([-1, 1, -1])
pineapple = np.array([1, -1, 1])
weight_matrix = np.array([banana, pineapple]) # feed forward layer

weight_matrix2=np.array([[1,-0.5],[-0.5,1]]) #recurrent layer


# Train the network using the input vectors
print("Enter the features of your fruit:")
print("Is it round?(y/n)")
shape=np.where(input()=="y",1,-1)

print("Is it smooth?(y/n)")
texture=np.where(input()=="y",1,-1)

print("Is it of 1 pound?(y/n)")
weight=np.where(input()=="y",1,-1)

test_input = np.array([shape, texture, weight])
feed_output=hamming_network(test_input, weight_matrix)
print(feed_output)
final_result=recognize_fruit(feed_output,weight_matrix2)
print(final_result)

print("The fruit is:")
print(fruit_array[np.argmax(final_result)])