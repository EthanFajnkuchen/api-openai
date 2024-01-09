def count_common_chars(s1, s2):
    return len(set(s1) & set(s2))

assert count_common_chars("abcdef", "defghi") == 3
assert count_common_chars("abc", "def") == 0
assert count_common_chars("hello", "world") == 1
assert count_common_chars("python", "code") == 2
assert count_common_chars("12345", "54321") == 5

print("All unit tests pass")