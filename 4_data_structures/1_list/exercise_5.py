# TODO: Write a Python program to count the number of elements
#       containing a string where length is 2 or more
#       and the first and last character of thst string are the same


def exercise_5(strings: list) -> int:
    res = []
    for string in strings:
        if len(string) >= 2 and string[0] == string[-1]:
            res.append(string)
    return len(res)


string_list = ['abc', 'xyz', 'aba', '1221']
assert exercise_5(string_list) == 2
