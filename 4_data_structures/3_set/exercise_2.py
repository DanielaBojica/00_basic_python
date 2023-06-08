# Write a Python program to remove item(s) from a given set.


def exercise_2(set_2: set) -> set:
  # There is set_2.pop() and set_2.remove(<item>) but sets are unordered so the resut is unpredictible
    return set_2

#!!! Here it should be set(["Fox", "Eagle", "Dog", "Cat"]) ??

animals_set = set("Fox", "Eagle", "Dog", "Cat")

assert exercise_2(animals_set) == {"Eagle", "Dog"}