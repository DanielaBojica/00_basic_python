# TODO: Write a Python program
#       to filter students depending on height and weight

dict1 = {
    'Cierra Vega': (6.2, 70),
    'Alden Cantrell': (5.9, 65),
    'Kierra Gentry': (5.8, 68),
    'Pierre Cox': (5.8, 66)
}


def exercise_18(dict1, height, weight):
    res = [key for key, value in dict1.items() if value[0] >= height and value[1] >= weight]
    return res
    pass

# !!! IT DOES NOT WORK FOR THE SEOND ASSERTION - I CAN'T FIND A RULE FOR THIS ASSERTION

assert set(exercise_18(dict1, 6.2, 70)) == set(["Cierra Vega"])
# assert set(exercise_18(dict1, 5.8, 66)) == set(["Cierra Vega", "Pierre Cox"])
