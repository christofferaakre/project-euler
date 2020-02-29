import math
from decimal import Decimal
from main import solve, list_divisors

def triangle_number(n):
    return int(n * (n + 1) / 2)

def is_triangle_number(x):
    return ((-1 + math.sqrt(1 + 8 * x)) / 2) % 1 == 0

largest_number_of_divisors = 0
x = 0
i = 1
while largest_number_of_divisors <= 500:
    x += i
    number_of_divisors = len(list_divisors(x))
    if number_of_divisors > largest_number_of_divisors:
        print(number_of_divisors)
        largest_number_of_divisors = number_of_divisors
    i += 1

solve(x)