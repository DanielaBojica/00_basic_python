# TODO: Write a Python program
#       to generate all permutations of a list in Python.


def exercise_18(list1: list) -> list:
    lsit1Perm = []
    for i in len(list1):
        list1Perm = [(list1[i],)
                     for list1[i]

                     if list[i] != list[i+1]
                     ]

    return


list1 = [1, 2, 3]
assert exercise_18(list1) == [
    (1, 2, 3),
    (1, 3, 2),
    (2, 1, 3),
    (2, 3, 1),
    (3, 1, 2),
    (3, 2, 1)
]
