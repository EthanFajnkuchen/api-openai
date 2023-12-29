def check_unique_elements(lst):
    return len(lst) == len(set(lst))

# Unit Tests
print(check_unique_elements([1, 2, 3]))  # True
print(check_unique_elements([1, 2, 2]))  # False
print(check_unique_elements([]))  # True
print(check_unique_elements(["a", "b", "c"]))  # True
print(check_unique_elements(["a", "a", "b", "c"]))  # False