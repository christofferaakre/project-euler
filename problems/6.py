from main import solve

N = 100

def sum_of_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

def sum_of_squares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i **2
    return sum

difference = (sum_of_numbers(N) ** 2) - sum_of_squares(N) 

solve(difference)