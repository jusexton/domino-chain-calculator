# Domino Chain Calculator

Used to calculate all possible chains of dominoes given a list of dominoes and a starting value.

The calculator builds a tree of all possible plays with [anytree](https://pypi.org/project/anytree/)

![alt text](result_tree.png)

# Running Locally

## Clone
```
git clone https://github.com/jusexton/domino-chain-calculator && cd domino-chain-calculator
```

## Setup Virtual Environment
```
poetry install
```

## Program Usage
```
poetry run -- python domino-chain-calculator -h (display help)

poetry run -- python domino-chain-calculator -s dominoes.json (for best route to be displayed)

poetry run -- python domino-chain-calculator -s dominoes.json -v (for all routes to be displayed) 

poetry run -- python domino-chain-calculator -s dominoes.json -v -i (for all routes to be displayed with sums)
```