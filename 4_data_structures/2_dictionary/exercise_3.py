# TODO: Write a Python program
#       to print all unique values in a dictionary.

dict1 = {
    1: 3,
    2: 3,
    4: 70,
    67: 9888
}


def exercise_3(dict1):
    list1 = []
    for value in dict1.values():
        if value not in list1:
            list1.append(value)
    # print(*list1)
    pass


exercise_3(dict1)
