from main import solve, is_prime

sum = 0

for i in range(1, 2000000):
    if is_prime(i):
        print(i)
        sum += i



solve(sum)