# TODO: Write a Python program
#       to remove the duplicate in the list.


def exercise_7(sample_list: list) -> list:
    no_dupl_list = []
    for item in sample_list:
        if item not in no_dupl_list:
            no_dupl_list.append(item)
    return no_dupl_list


string_list = ['abc', 'xyz', 'abc', '1221']
assert exercise_7(string_list) == ['abc', 'xyz', '1221']