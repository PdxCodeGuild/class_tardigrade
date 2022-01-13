# import the whole module
import arithmetic

import random

print(arithmetic.add(1, 2))

print(random.random())

# import just what you need
from arithmetic import divide

from random import randrange

print(divide(10, 5))

print(randrange(1, 100))