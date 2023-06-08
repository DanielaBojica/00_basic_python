# TODO: Write a Python function
#       that takes two lists
#       and returns True if they have at least one common member
#       else False


def exercise_11(list1: list, list2: list) -> bool:
    flag = False
    for i in list1:
        for j in list2:
            if i == j:
                flag = True
    return flag


# 1st test
list1 = ["train", "bike", "cat", "do", "I"]
list2 = []
assert exercise_11(list1, list2) is False

# 2nd test
list1 = ["train", "bike", "cat", "do", "I"]
list2 = ["cat"]
assert exercise_11(list1, list2) is True
