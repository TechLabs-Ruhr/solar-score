# Getting started with predictions
## Overview
The folder `prediction` is our entry point to forecasting. You can import its submodules in the normal way like
```
from prediction import core
```
There are three different modules within prediction
```
prediction.core       # For generel/advanced use especially in production. Mostly .py files
prediction.test       # For self written tests to discover functionality. Mostly .ipynb files
prediction.examples   # With basic solutions from the api documentation. Mostly .ipynb files
```
To run these it is important to install the `score` environment given as environment.yml. Please have a look on <https://github.com/TechLabs-Dortmund/solar-score/wiki> to find out more about that.

I will try to keep this readme updated. For now you could already check out the `shapes.ipynp` in `prediction.test`. There you can see the basic pipeline for training a neural network based on synthetic data.

## Adaptability
Please feel free to create your own tests or examples. Everything that works should be then brought to life in the `core` submodule.
The goal there is to have general functions for training and inference, that can be used by all of us.
