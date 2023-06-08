# TODO: Write a Python program
#       to remove duplicates from Dictionary.

dict1 = {
    ("1"): 2,
    ("2"): 2,
    ("3"): 4
}


def exercise_2(dict1):
    # Your code here
    return dict1

# It seems you want to remove ALL items that are the same, not only the duplicates.
assert exercise_2(dict1) == {("3"): 4}
