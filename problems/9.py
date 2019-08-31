import math
from main import solve

a = 1
b = 1

def get_c(a, b):
    return math.sqrt(a **2 + b ** 2)

found = False

for a in range(1, 1000):
    if not found:
        for b in range(1, 1000):
            c = get_c(a, b)
            if c.is_integer():
                if int(a + b + c) == 1000:
                    found = True
                    A = int(a)
                    B = int(b)
                    C = int(c)
                    break
    else:
        break


solve(A * B * C)