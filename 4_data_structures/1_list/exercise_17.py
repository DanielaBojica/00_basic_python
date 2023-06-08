# TODO: Write a Python program
#       to sort a list of dictionaries.
#       by qty


def exercise_17(list1: list) -> list:
    list_sorted = []
    max = list1[0]["qty"]
    for i in range(len(list1)):
        if list1[i]["qty"] > max:
            max = list1[i]["qty"]
        list_sorted.append(list1[i])

    return list_sorted


list1 = [
    {"fruit": "Apple", "qty": 4},
    {"fruit": "Peach", "qty": 10},
    {"fruit": "Plum", "qty": 5},
    {"fruit": "Banana", "qty": 8},
]

assert exercise_17(list1)
