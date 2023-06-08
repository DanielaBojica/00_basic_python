# Write a Python program to add member(s) in a set.


def exercise_1_first_solution(fruits_set: set) -> set:
    additional_set = {"🥝", "🍓", "Orange", "🥭", "Peach"}
    fruits_set.update(additional_set)
    return fruits_set


fruits_set = {"🍐"}

assert exercise_1_first_solution(fruits_set) == {"🥝", "🍐", "🍓", "Orange", "🥭", "Peach"}