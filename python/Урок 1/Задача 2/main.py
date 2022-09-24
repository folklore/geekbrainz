variants = [
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
    [1, 1, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 1],
]

for x, y, z in variants:
    left = not(x and y and z)
    right = not(x) or not(y) or not(z)

    print(x, y, z, left == right)
