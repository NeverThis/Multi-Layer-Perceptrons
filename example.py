from src.mlp import MLP
from src.mlp import Layer
from src.mlp import Perceptron

# Pre-configured perceptrons
OR = Perceptron(weights=[1, 1], bias=-0.5)
NAND = Perceptron(weights=[-1, -1], bias=1.5)
AND = Perceptron(weights=[1, 1], bias=-1.5)

# Group them into layers to build the MLP
mlp = MLP(layers=[
    Layer(perceptrons=[OR, NAND]), 
    Layer(perceptrons=[AND])
])

X = [[0, 0], [0, 1], [1, 0], [1, 1]]
print(mlp.predict(X))