'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1:
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

from Common.Tags import DYNAMIC_PROGRAMMING

def climbStairs(n: int) -> int:
    if n <= 2:
        return n
    prev_prev = 1
    prev = 2
    for _ in range(3, n + 1):
        current = prev_prev + prev
        prev_prev = prev
        prev = current
    
    return prev

# test case
print(climbStairs(2))  # expected output: 2
print(climbStairs(3))  # expected output: 3
print(climbStairs(4))  # expected output: 5