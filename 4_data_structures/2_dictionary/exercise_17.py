# TODO: Write a Python program
#       which returns the list of keys
#       where the value equals the maximum value found.


def exercise_17(dict1):
    return [key for key, value in dict1.items() if value == max(dict1.values())]
    pass
#!! IT DOES NOT WORK FOR THE 2nd TEST BECAUSE MY SOLUTION IS ['Theodore', 'Roxanne'] AND NOT ['Roxanne', 'Theodore']

# 1st test
dict1 = {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 22}
assert exercise_17(dict1) == ['Roxanne', 'Betty']

# 2nd test
dict1 = {'Theodore': 25, 'Roxanne': 25, 'Mathew': 21, 'Betty': 20}
assert exercise_17(dict1) == ['Roxanne', 'Theodore']
