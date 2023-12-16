#include <bits/stdc++.h>
using namespace std;

#define int long long int
#define mx MAX

double sigmoid(double x) {
    return 1 / (1 + exp(-x));
}

double sigmoidDerivative(double x) {
    double sigmoidX = sigmoid(x);
    return sigmoidX * (1 - sigmoidX);
}

class NeuralNetwork {
private:
    std::vector<double> weights;
    double bias;
    double learningRate;

public:
    NeuralNetwork(double lr) {
        weights = {0.5, -0.5};
        bias = 0.5;
        learningRate = lr;
    }

    double feedForward(double input1, double input2) {
        double sum = input1 * weights[0] + input2 * weights[1] + bias;
        return sigmoid(sum);
    }

    void train(double input1, double input2, double target) {
        double output = feedForward(input1, input2);
        double error = target - output;
        double dOutput = error * sigmoidDerivative(output);

        double dWeight1 = input1 * dOutput;
        double dWeight2 = input2 * dOutput;
        double dBias = dOutput;

        weights[0] += learningRate * dWeight1;
        weights[1] += learningRate * dWeight2;
        bias += learningRate * dBias;
    }
};

int main() {
    NeuralNetwork neuralNetwork(0.1);
    vector<std::vector<double>> trainingData = {
        {0, 0, 0},
        {0, 1, 1},
        {1, 0, 1},
        {1, 1, 0}
    };

    for (const auto& data : trainingData) {
        double input1 = data[0];
        double input2 = data[1];
        double target = data[2];
        neuralNetwork.train(input1, input2, target);
    }
    double input1, input2;
    cout << "Enter input 1: ";
    cin >> input1;
    cout << "Enter input 2: ";
    cin >> input2;

    double output = neuralNetwork.feedForward(input1, input2);
    cout << "Output: " << output << '\n';
}
