# TODO: Write a Python script
#       to merge two Python dictionaries.

dict1 = {"type": "dog"}
dict2 = {"name": "Waouf"}


def exercise_1(dict1, dict2):
    # Your code here
    return {**dict1, **dict2}


assert exercise_1(dict1, dict2) == {"type": "dog", "name": "Waouf"}