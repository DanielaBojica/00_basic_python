# TODO: Write a Python program
#       to create a list of dictionaries of dictionary of lists.


def exercise_9(dict1):
    keys = dict1.keys()
    vals = zip(*[dict1[key] for key in keys])
    res = [dict(zip(keys, val)) for val in vals]
    return res
    pass


dict1 = {
    'Science': [88, 89, 62, 95],
    'Language': [77, 78, 84, 80]
}

assert exercise_9(dict1) == [
    {'Science': 88, 'Language': 77},
    {'Science': 89, 'Language': 78},
    {'Science': 62, 'Language': 84},
    {'Science': 95, 'Language': 80}
]