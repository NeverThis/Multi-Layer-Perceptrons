# Multi-Layer Perceptron (MLP)

> [!TIP] 
> AI Agents. Large Language Models. Neural Networks. These buzzwords seem to be everywhere, used by seemingly everyone. But how did we get here? Well... plenty of people have answered that question. I haven't understood their answers. Yet.
> 
> This repository is part of my journey to catch up with modern Large Language Models, one step at a time. I'm documenting what I learn, what I build, and probably a few things I get spectacularly wrong along the way. If you're on a similar journey, why not check out my other repositories and see where I've been or where I'm headed next?

## Preamble

Gee, Brain, what do you want to do tonight?

The same thing we do every night, Pinky: learn about perceptrons! More specifically, their bigger, more powerful sibling: the Multi-Layer Perceptron (MLP).

Quick, for 100 points: What was the fundamental limitation of a perceptron? Yes, that's right, Pinky! Its inability to distinguish data that isn't linearly separable. Our lonely little perceptron couldn't even learn something as simple as XOR. But how are we supposed to take over the world then? We'll simply stack perceptrons into multiple layers! This allows them to learn much more complex patterns. And that’s exactly what we’ll do by solving XOR!

> [!NOTE]
> Already lost? Check out my explanation of perceptrons: [Here](https://github.com/NeverThis/Perceptron).

## Solving XOR with an Ensemble of Perceptrons

But how do we go about this? Well... it looks like it’s time to dust off our Boolean algebra! Our perceptrons are still stuck with simple algebraic operations, but luckily, XOR can be expressed using just those:

$A \oplus B = (A \lor B) \land \neg(A \land B)$

Now we just need to reuse the weights and biases our perceptrons learned last time (or, you know, spend a minute or two thinking about solutions):
* **OR:** $1*x_1 + 1*x_2 - 0.5 \ge 0$
* **AND:** $1*x_1 + 1*x_2 - 1.5 \ge 0$
* **NAND:** $-1*x_1 - 1*x_2 + 1.5 \ge 0$

> [!NOTE]
> You should now be able to follow the Python code included in this repository.

## Results

What we've built here is a tiny neural network made up of multiple perceptrons. They're arranged into layers, where the output of one layer becomes the input to the next. We differentiate between the Input Layer, Hidden Layer, and Output Layer.

The term "Input Layer" is a bit misleading (at least in my opinion) because it doesn't actually perform any computation. It simply represents the values we're feeding into the network: Our boolean values A and B. You can think of it as a fancy name for the entry point of our data. The Hidden Layer is where the actual processing happens. Our hidden layer contains two perceptrons: one calculates OR, while the other calculates NAND. Finally, the Output Layer takes these two intermediate results and combines them using an AND perceptron. Just like the equation! 

And there we have it. XOR done. But why did we go through all this fun manually? Couldn't we have just made the perceptrons learn this like last time? 

Unfortunately, our trusty Heaviside activation function gets in the way. We can tell whether the neural network made the right or wrong prediction, but we don’t get any information about how wrong it was. The network might have been 100% confident in its guess, or it might have been barely leaning one way. In the latter case, we’d naturally want to adjust the weights less than in the former. With a single perceptron, the weighted sum gave us a good idea of how strongly each input influenced the decision and therefore how much we need to adjust its weight. But with multiple perceptrons, we lose that information. A single input is (transitively) connected to multiple weights, and changing one of them can have unpredictable consequences for the perceptrons further down the line. As a result, we don't know how much to adjust the weights, or even which direction to adjust them in.

Sure, we could try random changes or educated guesses, but training like this would be a bit like throwing darts in the dark. Which is why we need a different approach. That approach involves the sigmoid function I mentioned last time. But we'll get into that next time.

One last thing, though: This problem had researchers scratching their heads for quite a while. If knowing whether our neural network guessed right or wrong doesn't help during training, then perhaps we don't need to bother with knowing the target answer at all. This is where unsupervised learning moved into the spotlight. Hebb's learning rule, for example, relied purely on associations: If two features kept cropping up together, the network would simply strengthen the connection between those neurons. But we're getting of track...