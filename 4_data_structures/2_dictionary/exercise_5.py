# TODO: Write a Python program
#       to remove spaces from the keys of a dictionary.

dict1 = {
    " a": 1,
    "b b b": 2,
    "e  ": 3
}


def exercise_5(dict1):
    list_keys = []
    for key in dict1:
        key = key.replace(" ", "")
        list_keys.append(key)
    list_values = list(dict1.values())
    final_dict = dict(zip(list_keys, list_values))
    return final_dict



assert exercise_5(dict1) == {"a": 1, "bbb": 2, "e": 3}