from main import solve

big = 600851475143

def largest_prime_factor(number):
    b = 2
    a = number
    while a > b:
        if int(a % b) is 0:
            a /= b
            b = 2
        else:
            b += 1
    return int(a)

solve(largest_prime_factor(big))