#Different ways to import modules
# Import the whole module

# import math
# print(math.sqrt(9))

# import as an alias
# import math as m
# print(m.sqrt(25))

# Import specific functions or variables
from math import sqrt, pi
print(sqrt(36))
print(pi)

# Import everything from the module
from math import *
print(sqrt(49))
print(pi)

