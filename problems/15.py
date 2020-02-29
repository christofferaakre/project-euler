from main import solve
from scipy.special import comb

def number_of_routes(n: int) -> int:
    return int(comb(2 * n, n))

solve(number_of_routes(20))