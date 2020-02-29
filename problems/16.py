from main import solve

n = str(2 ** 1000)
result = sum([int(char) for char in n])
solve(result)