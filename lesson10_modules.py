"""
Lesson 10: Modules & Imports

Demonstrates importing a custom local module (math_utils) as well
as Python's built-in standard library modules (math, random,
datetime) to reuse existing functionality instead of rewriting it.
"""

import math_utils
from math_utils import square
import math
import random
import datetime

print(math_utils.add(3, 5))
print(square(4))
print(math.sqrt(16))
print(random.randint(1, 10))
print(datetime.date.today())
