# TODO: Write a Python program
#       to return a dictionary containing
#       the frequency of elements found in a list.


def exercise_14(list1: list) -> dict:
    my_dict = {}
    for elem in list1:
        if elem not in my_dict:
            my_dict[elem] = 0
        if elem in my_dict:
            my_dict[elem] = my_dict[elem] + 1

    return my_dict


list1 = ["a", "a", "b", "b", "c", "d", "d", "d"]
assert exercise_14(list1) == {
    'a': 2,
    'b': 2,
    'c': 1,
    'd': 3
}
