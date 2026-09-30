'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

Example 1:
    Input: num1 = "2", num2 = "3"
    Output: "6"

Example 2:
    Input: num1 = "123", num2 = "456"
    Output: "56088"
'''

from Common.Tags import SIMULATION

def multiply(num1: str, num2: str) -> str:
    if num1 == "0" or num2 == "0":
        return "0"

    m, n = len(num1), len(num2)
    result = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            digit1 = ord(num1[i]) - ord('0')
            digit2 = ord(num2[j]) - ord('0')
            product = digit1 * digit2

            pos = i + j + 1
            total = product + result[pos]

            result[pos] = total % 10
            result[pos - 1] += total // 10

    return ''.join(map(str, result)).lstrip('0')

# Example usage:
print(multiply("123", "456"))  # Output: "56088"
print(multiply("2", "3"))  # Output: "6"