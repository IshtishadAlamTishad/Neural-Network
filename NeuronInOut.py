# every input have weights and 1 bias per neuron
## output = weight * input + bias // y = mx + c
# 3 input to 1 neuron, that have 3 weight & 1 bias

input_1 = [1.0,2.0,2.5]
weight_1 = [3,1,3]
bias_1 = 1
output_1 = input_1[0]*weight_1[0] + input_1[1]*weight_1[1] + input_1[2]*weight_1[2] + bias_1
print(output_1)


# 4 inputs coming to 3 neuron,3 neuron have 3 different weights & Bias

input = [1.0,2.0,3.0,2.5]

weight1 = [0.2,0.8,-0.5,1.0]
weight2 = [0.5,-0.91,0.26,-0.5]
weight3 = [-0.26,-0.27,0.17,0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

output = [input[0]*weight1[0] + input[1]*weight1[1] + input[2]*weight1[2] + input[3]*weight1[3]+ bias1
        , input[0]*weight2[0] + input[1]*weight2[1] + input[2]*weight2[2] + input[3]*weight2[3]+ bias2,
          input[0] * weight3[0] + input[1] * weight3[1] + input[2] * weight3[2] + input[3]*weight3[3]+ bias3]

print(output)