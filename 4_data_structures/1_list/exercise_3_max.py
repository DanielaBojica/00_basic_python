# TODO: Write a Python program
#       to get the largest number from a list.


# def exercise_3(numbers: list) -> int:
#     max = numbers[0]
#     for number in numbers:
#         if number > max:
#             max = number
#     return max

# or:
# def exercise_3(numbers: list) -> int:
#     return max(numbers)

# or:
# def exercise_3(numbers: list) -> int:
#     numbers.sort()
#     return numbers[-1]

numbers = [1, 2, 3, 4]
largest_number = exercise_3(numbers)
assert largest_number == 4
