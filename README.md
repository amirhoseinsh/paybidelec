[![PyPI version shields.io](https://img.shields.io/pypi/v/paybidelec.svg)](https://pypi.python.org/pypi/ansicolortags/)

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

# Pay as a Bid Package for Electricity Market

This is a package about simulation pay as a bid electricity auction.

# Instalation

To install, simply use `pip`:

```
pip install paybidelec
```

# Usage

First of all you must import Production from paybidelec 

```
from paybidelec import Production
```

Then you must define parameters as a below :

* number = number of rivals 
* prices = intial price of each 
* dispatches = maximum dispatch of each
* costs = costs of produce electriciy of each
* risks = behavioral risk of each (between 0 - 0.8)
* expectedReward = expected reward that they want

all of these must be array

```python
ss = Production(number,prices,dispatches,costs, risks, expectedReward)
```


for ploting first contributor's bid during time you must write a simple code as below:
 


