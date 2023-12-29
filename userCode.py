def sieve_of_eratosthenes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while (p * p <= n):
        if (is_prime[p] == True):
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
        p += 1
    primes = []
    for p in range(2, n + 1):
        if is_prime[p]:
            primes.append(p)
    return primes

def prime_factors(num):
    primes = sieve_of_eratosthenes(int(num**0.5) + 1)
    factors = []
    for prime in primes:
        if num % prime == 0:
            while num % prime == 0:
                factors.append(prime)
                num = num // prime
    if num > 1:
        factors.append(num)
    return factors

# Unit Tests
assert prime_factors(10) == [2, 5]
assert prime_factors(28) == [2, 2, 7]
assert prime_factors(13195) == [5, 7, 13, 29]
assert prime_factors(100) == [2, 2, 5, 5]
assert prime_factors(7919) == [7919]

print("All unit tests passed!")