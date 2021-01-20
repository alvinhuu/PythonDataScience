import numpy as py

print(py.__version__)

EquDifference = py.arange(0,21,1)
print(EquDifference)
print([ x for x in EquDifference if x%2==0])
print([ x for x in EquDifference[1:] if x%3==0])

print(EquDifference[::2] )
print(EquDifference[3::3] )