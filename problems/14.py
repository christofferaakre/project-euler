from main import solve

def collatz(n: int) -> int:
    # even
    if n % 2 == 0:
        return int(n / 2)
    # odd
    else:
        return int(3 * n + 1)

def collatz_sequence(n: int) -> list:
    x = n
    sequence = [x]
    while x != 1:
        x = collatz(x)
        sequence.append(x)
    return sequence

longest_chain = 0
leading = 0

for i in range(1, 1000001):
    chain = len(collatz_sequence(i))
    if chain > longest_chain:
        longest_chain = chain
        leading = i
        print(f"{i} leading with longest chain {longest_chain}")

solve(f"{leading} has the longest chain with length {longest_chain}")