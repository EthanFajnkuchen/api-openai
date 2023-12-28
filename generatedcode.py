def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Unit tests
print(is_prime(1))  # False
print(is_prime(2))  # True
print(is_prime(10))  # False
print(is_prime(17))  # True
print(is_prime(21))  # False

print("Hello" + "World")