## Dot Product

# 4 inputs coming to 3 neuron,3 neuron have 3 different weights & Bias

import numpy as np

input = [1.0,2.0,3.0,2.5]

weights = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

bias = [2, 3, 0.5]

'''
layer_outputs = []
for i, j in zip(weights,bias) :
    neuron_output=0
    for n_input, k in zip(input, i):
        neuron_output += n_input * k
    neuron_output += j
    layer_outputs.append(neuron_output)
'''
output = np.dot(weights, input) + bias

print(output)