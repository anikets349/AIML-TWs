import numpy as np

def sigmod(x):
    return 1/(1 + np.exp(-x))

def derivative_sigmoid(x):
    return x * (1 - x)

inputs = np.array([[0,0],[0,1],[1,0],[1,1]])
outputs = np.array([[0],[1],[1],[0]])
inputLayerNeurons, hiddenLayerNeurons,outputLayerNeurons = 2,2,1
a = 0.1
epochs = 20000

wh = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
bh = np.random.uniform(size=(1,hiddenLayerNeurons))
wout = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
bout = np.random.uniform(size=(1,outputLayerNeurons))

for i in range(epochs):
    #Feedforward network
    hiddenLayerInput = np.dot(inputs,wh) + bh
    hiddenLayerOuput = sigmod(hiddenLayerInput)
    outputLayerInput = np.dot(hiddenLayerOuput,wout) + bout
    predOutput = sigmod(outputLayerInput)

    #Backpropagation
    error_outputLayer = outputs - predOutput
    #print(error_outputLayer)
    #delta k = yk(1-yk) * ek
    d_outputLayer = derivative_sigmoid(predOutput) * error_outputLayer
    #print(d_outputLayer)
    #delta j = yj(i-yj) * sumation (delta k * wjk)
    #error_hidden_layer = np.dot(d_outputLayer,wout.T)
    d_hiddenLayer =  derivative_sigmoid(hiddenLayerOuput) * np.dot(d_outputLayer,wout.T)
    #print(d_hiddenLayer)
    #Wij = Wij + (a * Xi * deltaj)
    #wjk = Wjk + (a * Yj * deltak)
    wout = wout + np.dot(hiddenLayerOuput.T,d_outputLayer)*a
    wh = wh + np.dot(inputs.T,d_hiddenLayer)*a
    bh = bh + np.sum(d_hiddenLayer,axis=0, keepdims=True ) * a
    bout = bout + np.sum(d_outputLayer, axis=0, keepdims=True) * a

print("Predicted Outputs are:")
print(np.round(predOutput))




