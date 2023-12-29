def check_9(lst):
    count = 0
    for num in lst:
        if num == 9:
            count += 1
    if count > 8:
        return True
    else:
        return False

# Unit Tests
print(check_9([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 9, 9]))  # True
print(check_9([1, 2, 3, 4, 5, 6, 9, 9, 9, 9, 9, 9, 9, 9, 9]))     # True
print(check_9([1, 2, 3, 4, 5, 6, 9, 9, 9, 9, 9, 9, 9, 9]))        # False
print(check_9([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]))     # True
print(check_9([1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 9, 9, 9, 9, 8, 9]))  # True