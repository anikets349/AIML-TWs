import numpy as np

def unitStep(x, t):
    if x > t:
        return 1
    return 0

def perceptronLearn(inputs, outputs, w, a, th):
    epochs = 30
    numInstances = inputs.shape[0]
    numInputs = inputs.shape[1]
    for j in range(0, epochs):
        print("Epoch", j + 1)
        flag = False
        for i in range(0, numInstances):
            print("Training instance ", i + 1, ":", inputs[i])
            x = inputs[i]
            weightedSum = np.dot(w, x)
            pred = unitStep(weightedSum, th)
            print("Target:", outputs[i], "Predicted:", pred)
            error = outputs[i] - pred
            if pred == outputs[i]:
                print("Output matching. Weights need not be updated")
            else:
                flag = True
                print("Output not matching. Weights need to be updated")
                for k in range(0, numInputs):
                    w[k] = round(w[k] + (a * x[k] * error), 1)
                print("Updated weights:", w)
        if not flag:
            print("\nFinal weights:", w)
            break
        print("")

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
inputsNOT = np.array([[0], [1]])
outputsOR = np.array([0, 1, 1, 1])
outputsAND = np.array([0, 0, 0, 1])
outputsNOT = np.array([1, 0])

print("-----------------------------------------------")
print("OR gate")
perceptronLearn(inputs, outputsOR, [-0.2, 0.4], 0.2, 0)

print("-----------------------------------------------")
print("AND gate")
perceptronLearn(inputs, outputsAND, [0.2, 0.4], 0.5, 1)

print("-----------------------------------------------")
print("NOT gate")
perceptronLearn(inputsNOT, outputsNOT, [-0.3], 0.5, -1)

