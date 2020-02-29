import numpy as np
def solve(solution):
    print(solution)

def is_prime(x: int):
    is_prime = True
    if x < 2: 
        return False
    if x == 2:
            return True

    for i in range(2, int(np.sqrt(x)) + 1):
        if x % i == 0:
            is_prime = False
            break
    return is_prime

def list_divisors(x: int) -> list:
        divisors = []
        for i in range(1, int(np.sqrt(x) + 1)):
                if x % i == 0:
                   divisors.append(i)
                   if x / i != i:
                       divisors.append(int(x / i))     
                        

        return sorted(divisors)