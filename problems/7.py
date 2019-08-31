from main import solve, is_prime

number_of_primes = 0
largest_prime = 0

i = 2

N = 10001

while number_of_primes < N:
    if is_prime(i):
        print(number_of_primes)
        largest_prime = i
        number_of_primes += 1
    i += 1
solve(largest_prime)