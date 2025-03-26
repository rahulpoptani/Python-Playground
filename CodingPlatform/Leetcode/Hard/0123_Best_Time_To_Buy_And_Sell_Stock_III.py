'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
Find the maximum profit you can achieve. You may complete at most two transactions.
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example 1:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Example 2:
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

Example 3:
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''
from typing import List

def maxProfit(prices: List[int]) -> int:
    left = 0
    right = 1
    max_profit = 0
    res = []
    for right in range(1, len(prices)):
        if prices[right] >= prices[left]:
            right += 1
            continue
        else:
            if len(prices[left:right]) > 1: res.append(prices[left:right])
            left = right
            right += 1
    if len(prices[left:right]) > 1: res.append(prices[left:right])
    print(res)
    res = sorted(list(map(lambda x: x[-1] - x[0], res)), reverse=True)
    print(res, res[:2])
    max_profit = sum(res[:2])
    return max_profit


print(maxProfit([3,3,5,0,0,3,1,4]))
print(maxProfit([1,2,3,4,5]))
print(maxProfit([7,6,4,3,1]))
print(maxProfit([1,2,4,2,5,7,2,4,9,0]))

# prices = [1]
# maxProfit(prices)
# prices = [1,2]
# maxProfit(prices)
# prices = [2,1]
# maxProfit(prices)
# prices = [1,2,4]
# maxProfit(prices)
# prices = [1,4,2]
# maxProfit(prices)
# prices = [1,2,4,2]
# maxProfit(prices)
# prices = [1,2,4,2,5]
# maxProfit(prices)
# prices = [1,2,4,2,5,7]
# maxProfit(prices)
# prices = [1,2,4,2,5,7,2,4,9,0]
# maxProfit(prices)