# CS228

This repository contains the project done as a part of CS228: Logic for Computer Science at IIT Bombay in Spring 2022.

## Problem Statement

There are several cars parked in a large parking and a particular car wants to leave. The cars can move along their lengths only. Certain squares are invalid. An example of this problem is given below. 

<p align="center">
  <img src="https://github.com/Adu3108/SAT-Solver/assets/81511060/4b5e1cea-546b-46b9-8bd4-ec37e7ed18fb" />
</p>

The goal of the game is to decide whether a solution exists for a particular given car (whether it can leave the car park successfully). We model it as a Boolean Satisfiability Problem and use a SAT solver to solve the same.

## z3 Installation

We use z3, a high performance theorem prover to solve the Boolean Satisfiability Problem. 

Mac users can install using homebrew

```bash
brew install z3
```

Other users can also try installing it by cloning the [source repository](https://github.com/Z3Prover/z3)

## Resources

[Z3Py Tutorial](https://ericpony.github.io/z3py-tutorial/guide-examples.htm)

[Rush Hour Puzzle](https://en.wikipedia.org/wiki/Rush_Hour_(puzzle))

## References

https://theory.stanford.edu/~nikolaj/programmingz3.html

https://github.com/Z3Prover/z3/tree/master/examples%2Fpython

https://www.programcreek.com/python/example/97293/z3.Solver

https://colab.research.google.com/github/philzook58/z3_tutorial/blob/master/Z3%20Tutorial.ipynb#scrollTo=pKKcoB-nwwxx

https://stackoverflow.com/questions/11867611/z3py-checking-all-solutions-for-equation
