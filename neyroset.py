import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


training_inputs = np.array( [[0, 0, 1],
                             [1, 1, 1],
                             [1, 0, 1],
                             [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1

print("Случайные инициализирующие веса:\n", synaptic_weights)

for i in range(30000):
    input_layer = training_inputs
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_weights += adjustments

print("Веса после обучения:\n", synaptic_weights)

print("Результат после обучения:\n", outputs)

new_inputs = np.array([1, 1, 0]) #новая ситуация
output = sigmoid(np.dot(new_inputs, synaptic_weights))
print("Новая ситуация:\n", output)
