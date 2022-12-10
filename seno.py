import numpy as np
import math
from sympy import*

y = Symbol('y')

x = sin(3*y).diff(y)
print(x)