import math

def solve(solution):
    print(solution)

def is_prime(x):
    is_prime = True
    if x < 2: 
        return False
    if x == 2:
            return True

    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            break
    return is_prime