import numpy as np

# Input Layer
inputL = 0.8
weightsL = [0.99,1.27,1.0]
biasL = 0.98

LayerOutput = np.dot(weightsL,inputL) + biasL
print("Layer's Output = ",LayerOutput)

# Layer 1

weightsL1 = [[2.9,4.8,1.0],
             [2.89,1.69,0.86],
             [2.0,2.3,1.01]]
biasesL1 = [1.3,0.89,0.56]

Layer1Output = np.dot(weightsL1,LayerOutput) + biasesL1
print("Layer 1's Output = ",Layer1Output)

# Layer 2
weightsL2 = [[0.3,0.5,0.1],
             [1.6,2.0,3.0],
             [7.7,5.9,0.9]]
biasesL2 = [2.0,0.78,0.48]
Layer2Output = np.dot(weightsL2,Layer1Output) + biasesL2
print("Layer 2's Output =",Layer2Output)

weightsL3 = [0.2,0.1,0.3]
biasesL3 = 3.0

Layer3Output = np.dot(weightsL3,Layer2Output) + biasesL3
print("Layer 3's Output = ",Layer3Output)