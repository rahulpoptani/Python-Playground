'''
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
'''

class Solution:
    def isPalindrome2(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    def isPalindrome(self, x: int) -> bool: # does not work with 10, 100, ... instead compare first and last element iteratively
        y = x
        power = 1
        result = 0
        while (y > 0):
            last_element = y % 10
            result += last_element * power
            print('Last Element: {} | Result: {} | Power: {}'.format(last_element, result, power))
            power = power * 10
            y = y // 10
        return x == result


sol = Solution()
print(sol.isPalindrome(100))