'''
iven an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself. For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

def numSquares(n: int):
    dp = [n] * (n+1)
    dp[0] = 0
    print(dp)

    for target in range(1, n+1):
        print(f'target: {target}')
        for s in range(1, target+1):
            print(f's: {s}')
            square = s*s
            if target - square < 0:
                break
            print(f'dp[target]: {dp[target]} | 1 + dp[target - square]: {1 + dp[target - square]} | Min: {min(dp[target], 1 + dp[target - square])}')
            dp[target] = min(dp[target], 1 + dp[target - square])
            print(dp)
    
    return dp[n]


print(numSquares(13))
# print(numSquares(12))
