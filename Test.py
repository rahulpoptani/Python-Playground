def climb_stairs(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return 1
    memo[n] = climb_stairs(n - 1, memo) + climb_stairs(n - 2, memo)
    print(memo)
    return memo[n]

print(climb_stairs(10))  # Output: 89
