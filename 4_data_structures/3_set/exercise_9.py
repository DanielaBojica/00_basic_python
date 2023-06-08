# Write a Python program to remove all elements from a given set


def exercise_9(initial_set: set):
    initial_set.clear()
    return {}


animals = {"Fox", "Cat", "Dog"}

assert exercise_9(animals) == {}
