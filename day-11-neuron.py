import math


class Neuron:
    """A single artificial neuron performing forward and backward passes."""

    def _init_(self, num_inputs, lr=0.5):
        # Initialize weights and bias to small default values
        self.weights = [0.1] * num_inputs
        self.bias = 0.0
        self.lr = lr

    def forward(self, inputs):
        """Calculates weighted sum and applies Sigmoid activation."""
        # Compute dot product: (x1 * w1) + (x2 * w2) + ...
        total_sum = sum(i * w for i, w in zip(inputs, self.weights)) + self.bias
        # Squash output values between 0.0 and 1.0
        return 1.0 / (1.0 + math.exp(-max(min(total_sum, 50), -50)))

    def train(self, inputs, target):
        """Updates internal weights and bias using prediction errors."""
        prediction = self.forward(inputs)
        error = target - prediction

        # Adjust weights based on input scale and learning rate step size
        for idx in range(len(self.weights)):
            self.weights[idx] += self.lr * error * inputs[idx]
        # Update the bias balance tracking independently
        self.bias += self.lr * error


if _name_ == "_main_":
    print("⚡ Day 2: Compact Python Neuron Project ⚡")
    print("-" * 50)

    # Dataset simulating a logical 'AND' truth table operation
    dataset = [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)]

    # Instantiate model infrastructure with 2 input connections
    model = Neuron(num_inputs=2)

    # Execute optimization pipeline training across 50 iterations
    for epoch in range(50):
        for inputs, target in dataset:
            model.train(inputs, target)

    print("✅ System Training Loop Complete!\n")
    print(f"Final Parameters -> Weights: {model.weights} | Bias: {model.bias:.4f}")
    print("\n🔬 Target Verification Evaluation Results:")
    print(f"{'Inputs':<10}{'Prediction':<15}{'Target':<10}")
    print("-" * 50)

    # Evaluate absolute accuracy configurations
    for inputs, target in dataset:
        pred = model.forward(inputs)
        print(f"{str(inputs):<10}{pred:<15.4f}{target:<10}"
