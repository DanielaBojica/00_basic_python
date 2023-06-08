# TODO: Write a Python program
#       to update elements in list stored as dictionary values.


def exercise_10(dict1):
    dict1['Math'] = [x + 1 for x in dict1["Math"]]
    dict1['Physics'] = [x - 2 for x in dict1['Physics']]
    return dict1
    pass


dict1 = {
    'Math': [88, 89, 90],
    'Physics': [92, 94, 89],
    'Chemistry': [90, 87, 93]
}

assert exercise_10(dict1) == {
    'Math': [89, 90, 91],
    'Physics': [90, 92, 87],
    'Chemistry': [90, 87, 93]
}