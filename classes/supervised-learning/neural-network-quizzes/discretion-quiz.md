How many combinations of outputs the perceptron network can produce with the following setup:

    2 input perceptrons
    2 hidden perceptrons
    1 output perceptron

![Perceptron Network](http://g.gravizo.com/g?
  digraph G {
    "Input 1";
    "Input 2";
    "Input 1" -> "Hidden 1" [label="0,1"];
    "Input 1" -> "Hidden 2" [label="0,1"];
    "Input 2" -> "Hidden 1" [label="0,1"];
    "Input 2" -> "Hidden 2" [label="0,1"];
    "Hidden 1" -> "Output" [label="0,1"];
    "Hidden 2" -> "Output" [label="0,1"];
  }
)

As we can see from the graph above, there are only 4 combinations of inputs to the output layer. This means that there are only 4 combinations of possible results to this network. 