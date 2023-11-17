import numpy as np

input = [[1.0, 2.0, 3.0, 2.5],
         [2.0, 5.0, -1.0, 2.0],
         [-1.5, 2.7, 3.3, -0.8]]

weights1 = [[0.2, 0.8, -0.5, 1.0],
           [0.5, -0.91, 0.26, -0.5],
           [-0.26, -0.27, 0.17, 0.87]]

bias1 = [2, 3, 0.5]

weights2 = [[0.1, -.14, 0.5],
            [-0.5, .12, -.33],
            [-.44, .73, -.13]]

bias2 = [-1, 2, -.5]

layer1_output = np.dot(input, np.array(weights1).T) + bias1
layer2_output = np.dot(layer1_output, np.array(weights2).T) + bias2

print(layer2_output)

