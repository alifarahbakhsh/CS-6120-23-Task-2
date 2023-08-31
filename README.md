# CS-6120-23-Task-2

This repo contains a simple python code that receives a .json representation of a Bril program as the input, locates the `add` and `mul` instructions, and swaps
their arguments.

I'm still having difficulties at testing this with turnt. I have to compare the outputs of two Bril programs - the one before swapping, and the one after it.
Technically, the results should be the same. However, I'm having difficulties at reshaping this specific pipeline into a turnt test.
The easiest way of testing this seems to be a simple script that executes the two programs using Brili, writes the output to some file, and compares them.
