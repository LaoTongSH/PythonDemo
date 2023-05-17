import math
def is_sqr(x):
    return math.sqrt(x).is_integer()
print(list(filter(is_sqr, range(1,101))))