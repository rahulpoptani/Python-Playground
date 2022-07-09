'''
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

        S is empty;
        S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

Given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise
For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

'''

def solution(s):
    valid = True
    stack = []
    for c in s:
        try:
            if (c == '{' or c == '(' or c == '['):
                stack.append(c)
            elif (c == ')'):
                if (stack.pop() != '('): return 0
            elif c == ']':
                if (stack.pop() != '['): return 0
            elif c == '}':
                if (stack.pop() != '{'): return 0
        except IndexError:
            return 0
    if stack: return 0 
    else: return 1


print(solution('[(())]')) # valid
print(solution('')) # valid
print(solution('[(())][')) # invalid extra open brackets
print(solution('[(())]]')) # invalid extra close brackets
