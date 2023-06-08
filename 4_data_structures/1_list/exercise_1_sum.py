# TODO: Write a Python program
#       to sum all the items in a list


# def exercise_1(numbers: list) -> int:
#     total = 0
#     for i in numbers:
#         total = total + i
#     return total

# or:
# def exercise_1(numbers: list) -> int:
#     return sum(numbers)

# or:
# def exercise_1(numbers: list) -> int:
#     return sum([i for i in numbers])

numbers = [1, 2, 3, 4]

sum = exercise_1(numbers)
assert sum == 10
