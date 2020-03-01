from main import solve

#                75
#              95  64
#             17 47 82
#            18 35 87 10
#           20 04 82 47 65
#          19 01 23 75 03 34
#         88 02 77 73 07 63 67
#        99 65 04 28 06 16 70 92
#       41 41 26 56 83 40 80 70 33
#      41 48 72 33 47 32 37 16 94 29
#     53 71 44 65 25 43 91 52 97 51 14
#    70 11 33 28 77 73 17 78 39 68 17 57
#   91 71 52 38 17 14 91 43 58 50 27 29 48
#  63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

data = [
[75,],
[95, 64,],
[17, 47, 82,],
[18, 35, 87, 10,],
[20, 4, 82, 47, 65,],
[19, 1, 23, 75, 3, 34,],
[88, 2, 77, 73, 7, 63, 67,],
[99, 65, 4, 28, 6, 16, 70, 92,],
[41, 41, 26, 56, 83, 40, 80, 70, 33,],
[41, 48, 72, 33, 47, 32, 37, 16, 94, 29,],
[53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14,],
[70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57,],
[91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48,],
[63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,],
[4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23],
]

def sum_path(path: list) -> int:
    S = data[0][0]
    position = 0
    for i in range(1, len(data)):
        position += path[i]
        S += data[i][position]
    return S

paths = []

def generate_paths(length: int, path: list = []):
    if len(path) == length:
        paths.append(path)
        return
    for step in [[0], [1]]:
        generate_paths(length, path + step)

generate_paths(15)
longest_path = 0

for path in paths:
    length = sum_path(path)
    if length > longest_path:
        longest_path = length

solve(longest_path)
