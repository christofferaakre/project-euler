from main import solve

def is_palindrome(number):
    string = str(number)
    return string == string[::-1]

biggest_palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product) and product > biggest_palindrome:
            biggest_palindrome = product

solve(biggest_palindrome)