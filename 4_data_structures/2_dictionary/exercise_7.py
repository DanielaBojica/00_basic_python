# TODO: Write a Python program
#       to drop empty Items from a given Dictionary.

# Original Dictionary:
dict1 = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}


def exercise_7(dict1):
    dict1 = {k:v for (k,v) in dict1.items() if v is not None}
    return dict1


assert exercise_7(dict1) == {'c1': 'Red', 'c2': 'Green'}
