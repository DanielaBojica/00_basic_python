# TODO: Write a Python program
#       to count integer in a given mixed list.


def exercise_20(list1: list) -> int:
    sum = 0
    for i in list1:
        if type(i) == int:
            sum += i
    return sum


list1 = [1, 2, 'a', 'b', 50]

assert exercise_20(list1) == 53
