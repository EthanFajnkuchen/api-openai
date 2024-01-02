def candy(ratings):
    if not ratings:
        return 0
    n = len(ratings)
    candies = [1] * n
    for i in range(1, n):
        if ratings[i] > ratings[i-1]:
            candies[i] = candies[i-1] + 1
    for i in range(n-2, -1, -1):
        if ratings[i] > ratings[i+1]:
            candies[i] = max(candies[i], candies[i+1] + 1)
    return sum(candies)

# Unit tests
assert candy([1, 2, 3, 4, 5]) == 15
assert candy([5, 4, 3, 2, 1]) == 15
assert candy([1, 3, 2, 4, 5]) == 9
assert candy([1, 2, 2, 2, 1]) == 7
assert candy([1, 2, 3, 2, 1]) == 9

print("All unit tests pass")