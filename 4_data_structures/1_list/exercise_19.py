# TODO: Write a Python program
#       to create a multidimensional list (lists of lists) with zeros.
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]

def exercise_19(col, row) -> list:
    a = [[0 for x in range(col)] for y in range(row)]
    return a

# this one is wrong:
# assert exercise_19(2, 3) == [
#     [0, 0, 0],
#     [0, 0, 0]
# ]

# it should be:
assert exercise_19(2, 3) == [
    [0, 0],
    [0, 0],
    [0, 0]
]

assert exercise_19(4, 4) == [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
