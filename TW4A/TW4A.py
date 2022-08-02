import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivative_sigmoid(x):
    return x * (1 - x)

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputs = np.array([[0], [1], [1], [0]])
inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2, 2, 1
a = 0.1
epochs = 10000

wh = np.random.uniform(size=(inputLayerNeurons, hiddenLayerNeurons))
bh = np.random.uniform(size=(1, hiddenLayerNeurons))
wout = np.random.uniform(size=(hiddenLayerNeurons, outputLayerNeurons))
bout = np.random.uniform(size=(1, outputLayerNeurons))

for i in range(epochs):
    # forward propagation
    hidden_layer_input = np.dot(inputs, wh) + bh
    hidden_layer_output = sigmoid(hidden_layer_input)
    output_layer_input = np.dot(hidden_layer_output, wout) + bout
    pred_output = sigmoid(output_layer_input)
    # backward propagation
    e = outputs - pred_output
    d_output = e * derivative_sigmoid(pred_output)
    error_hidden_layer = np.dot(d_output, wout.T)
    d_hidden = error_hidden_layer * derivative_sigmoid(hidden_layer_output)
    wout += np.dot(hidden_layer_output.T, d_output) * a
    bout += np.sum(d_output, axis=0, keepdims=True) * a
    wh += np.dot(inputs.T, d_hidden) * a
    bh += np.sum(d_hidden, axis=0, keepdims=True) * a

print("Predicted outputs: ")
print(pred_output)
print(np.round(pred_output))