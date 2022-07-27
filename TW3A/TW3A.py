import numpy as np

def unitStep(x, t):
    if x > t:
        return 1
    return 0

def perceptronLearn(inputs, outputs, w, a, th):
    epochs = 10
    for j in range(0, epochs):
        print("Epoch", j + 1)
        flag = False
        for i in range(0, inputs.shape[0]):
            print("Training instance ", i + 1, ":", inputs[i])
            x0 = inputs[i][0]
            x1 = inputs[i][1]
            weightedSum = x0 * w[0] + x1 * w[1]
            pred = unitStep(weightedSum, th)
            print("Target:", outputs[i], "Predicted:", pred)
            error = outputs[i] - pred
            if pred == outputs[i]:
                print("Output matching. Weights need not be updated")
            else:
                flag = True
                print("Output not matching. Weights need to be updated")
                w[0] = round(w[0] + (a * x0 * error), 1)
                w[1] = round(w[1] + (a * x1 * error), 1)
                print("Updated weights:", w)
        if not flag:
            print("\nFinal weights:", w)
            break
        print("")

inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
outputsOR = np.array([0, 1, 1, 1])
outputsAND = np.array([0, 0, 0, 1])

print("")
print("OR gate")
perceptronLearn(inputs, outputsOR, [-0.2, 0.4], 0.2, 0)


print("\n\n")
print("AND gate")
perceptronLearn(inputs, outputsAND, [0.2, 0.4], 0.5, 1)
