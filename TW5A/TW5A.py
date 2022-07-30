# Implementation of AND logic for bipolar inputs (1 and -1) using Hebbian Rule

# Inputs
inputs = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
# Target / Actual outputs
outputs = [1, -1, -1, -1]

# Initialise the weights and bias to 0
w1 = w2 = b = 0

def hebbian():
    # Use the global variables
    global w1, w2, b
    print("dw1\tdw2\ty\tw1\tw2\tb")
    for i in range(0, len(inputs)):
        x1, x2 = inputs[i]
        y = outputs[i]
        # update weights and bias for each instance using the formula
        # wi(new) = wi(old) + (xi * y)
        # b(new) = b(old) + y
        w1 = w1 + (y * x1)
        w2 = w2 + (y * x2)
        b = b + y
        print(x1, x2, y, w1, w2, b, sep ="\t")
    print("Final weights and bias:", w1, w2, b)

hebbian()
print("Learning completed")
print("Output of AND using computed weights and bias is")
# Use the computed values to print the AND logic
print("x1\tx2\ty")
for i in range(0, len(inputs)):
    x1, x2 = inputs[i]
    y = outputs[i]
    # calculate predicted value for each instance using
    # (w1 * x1) + (w2 * x2) + b
    # if this value is > 0 then predicted value is 1 else -1
    pred = 1 if(w1 * x1) + (w2 * x2) + b > 0 else -1
    print(x1, x2, pred, sep = "\t")
    
    
    

