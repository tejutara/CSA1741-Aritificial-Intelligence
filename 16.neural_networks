# Define the number of inputs, hidden units, and outputs
n_inputs = 2
n_hidden = 2
n_outputs = 1

# Define the activation functions for the hidden and output layers
def sigmoid(x):
    return 1 / (1 + 2.718281828459045 ** (-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# Initialize the weights and biases for the layers
weights1 = [[0.1, 0.2], [0.3, 0.4]]
weights2 = [[0.5], [0.6]]
bias1 = [0.7, 0.8]
bias2 = [0.9]

# Define the training data and labels
X_train = [[0, 0], [0, 1], [1, 0], [1, 1]]
y_train = [[0], [1], [1], [0]]

# Define the learning rate and number of epochs
learning_rate = 0.1
n_epochs = 10

# Train the network
for epoch in range(n_epochs):
    # Forward pass
    hidden_layer = []
    for i in range(n_hidden):
        sum = 0
        for j in range(n_inputs):
            sum += X_train[epoch % 4][j] * weights1[j][i]
        sum += bias1[i]
        hidden_layer.append(sigmoid(sum))

    output_layer = 0
    for i in range(n_hidden):
        output_layer += hidden_layer[i] * weights2[i][0]
    output_layer += bias2[0]
    output_layer = sigmoid(output_layer)

    # Backward pass
    output_error = y_train[epoch % 4][0] - output_layer
    hidden_error = [0] * n_hidden
    for i in range(n_hidden):
        hidden_error[i] = output_error * weights2[i][0] * sigmoid_derivative(hidden_layer[i])

    # Update the weights and biases
    for i in range(n_hidden):
        for j in range(n_inputs):
            weights1[j][i] += learning_rate * X_train[epoch % 4][j] * hidden_error[i]
        bias1[i] += learning_rate * hidden_error[i]
    for i in range(n_hidden):
        weights2[i][0] += learning_rate * hidden_layer[i] * output_error
    bias2[0] += learning_rate * output_error

    # Print the loss at each epoch
    loss = (y_train[epoch % 4][0] - output_layer) ** 2
    print(f"Epoch {epoch+1}, Loss: {loss:.4f}")

# Use the trained network to make predictions
def predict(X):
    hidden_layer = [0] * n_hidden
    for i in range(n_hidden):
        sum = 0
        for j in range(n_inputs):
            sum += X[j] * weights1[j][i]
        sum += bias1[i]
        hidden_layer[i] = sigmoid(sum)

    output_layer = 0
    for i in range(n_hidden):
        output_layer += hidden_layer[i] * weights2[i][0]
    output_layer += bias2[0]
    output_layer = sigmoid(output_layer)
    return output_layer

# Test the network
X_test = [0, 0]
y_pred = predict(X_test)
print("Prediction:")
print(y_pred)
