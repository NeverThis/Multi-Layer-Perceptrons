class MLP:
    """A Multi-Layer Perceptron."""

    def __init__(self, layers: list):
        self.layers = layers

    def predict(self, X):
        """Passes input sequentially through all layers of perceptrons."""
        current_input = X
        for layer in self.layers:
            current_input = layer.forward(current_input)
        return current_input

class Layer:
    """A layer consisting of multiple Perceptrons."""

    def __init__(self, perceptrons: list):
        self.perceptrons = perceptrons

    def forward(self, X):
        """Passes the input through all perceptrons in this layer."""
        neuron_outputs = [p.predict(X) for p in self.perceptrons]
        return [list(sample) for sample in zip(*neuron_outputs)]

class Perceptron:
    """A single Perceptron."""

    def __init__(self, weights=None, bias=0.0):
        self.weights = weights
        self.bias = bias

    def _sum(self, xi: list) -> float:
        """Calculates the weighted sum."""
        return sum(w * x for w, x in zip(self.weights, xi)) + self.bias

    def _activation_function(self, z) -> int:
        """Applies the Heaviside step function."""
        return 1 if z >= 0 else 0

    def predict(self, X):
        """Make a prediction using current weights and bias."""

        if self.weights is None:
            raise ValueError("Weights have not been set yet!")
        return [self._activation_function(self._sum(xi)) for xi in X]