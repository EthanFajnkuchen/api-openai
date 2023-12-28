# Python code
def check_substring(string):
    if 'aa' in string:
        return True
    else:
        return False

print(check_substring("hello"))  # Expected output: False
print(check_substring("banana"))  # Expected output: False
print(check_substring("alpaca"))  # Expected output: False
print(check_substring("aadfaa"))  # Expected output: True
print(check_substring("aa"))  # Expected output: True