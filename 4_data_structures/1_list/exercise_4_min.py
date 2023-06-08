# TODO: Write a Python program
#       to get the smallest number from a list.


# def exercise_4(numbers: list) -> int:
#     min = numbers[0]
#     for number in numbers:
#         if number < min:
#             min = number
#     return min

    # or:
# def exercise_4(numbers: list) -> int:
#     return min(numbers)
    #
    # or:
# def exercise_4(numbers: list) -> int:
#     numbers.sort()
#     return numbers[0]


numbers = [1, 2, 3, 4]
largest_number = exercise_4(numbers)
assert largest_number == 1
