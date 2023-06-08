# TODO: Write a Python program
#       to find the list of words that are longer
#       than n from a given list of words.


# def exercise_10(sample_list: list, n: int) -> bool:
#     longer_than_n = []
#     for word in sample_list:
#         if len(word) > n:
#             longer_than_n.append(word)
#     return longer_than_n

# or:
# def exercise_10(sample_list: list, n: int) -> bool:
#     return list(word for word in sample_list if len(word) > n)


sample_list = ["train", "bike", "cat", "do", "I"]
assert exercise_10(sample_list, 3) == ["train", "bike"]
assert exercise_10(sample_list, 1) == ["train", "bike", "cat", "do"]