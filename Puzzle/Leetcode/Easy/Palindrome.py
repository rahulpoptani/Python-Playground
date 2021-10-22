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
            print('Last Element: {} | Power: {} | Result: {} '.format(last_element, power, result))
            power = power * 10
            y = y // 10
        return x == result
    

    def isPalindrome3(self, x: int):
        divisor = 1
        while(x/divisor >= 10):
            divisor *= 10
            print('Incrementing Divisor to: {}'.format(divisor))
        
        while(x != 0):
            leading = x // divisor
            trailing = x % 10
            print('Leading: {} | Trailing: {}'.format(leading, trailing))

            if(leading != trailing):
                return False
            
            x = (x % divisor) // 10
            divisor = divisor / 100
            print('New X: {} | Divisor: {}'.format(x, divisor))
        
        return True


sol = Solution()
print(sol.isPalindrome3(1221))
