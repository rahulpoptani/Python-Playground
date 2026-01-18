def sum(n: int) -> int:
    if n == 0:
        return 0
    return sum(n // 10) + n % 10

print(sum(1234))  # Output: 10
