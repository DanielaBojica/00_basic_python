# TODO: Write a Python program
#       to find the highest 3 keys of the dictionary.

dict1 = {1: 0, 2: 6, 3: 20, 9: 40}


def exercise_4(dict_input):
    list_keys = []
    for key in dict_input:
        if key not in list_keys:
            list_keys.append(key)
    list_keys.sort(reverse=True)
    return list_keys[:3]

assert set(exercise_4(dict1)) == set([9, 3, 2])
