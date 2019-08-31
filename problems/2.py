import math
from main import solve

def fibo(n):
    return round((((1 + math.sqrt(5)) / 2) ** n - ((1 - math.sqrt(5)) / 2) ** n) / math.sqrt(5))

fib = 1
sum = 0
i = 1
while fib <= 4000000:
    fib = fibo(i)
    if fib % 2 == 0:
        sum += fib
    i += 1

solve(sum)