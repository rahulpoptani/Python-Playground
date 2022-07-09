'''
A string S consisting of N characters is called properly nested if:

        S is empty;
        S has the form "(U)" where U is a properly nested string;
        S has the form "VW" where V and W are properly nested strings.

For example, string "(()(())())" is properly nested but string "())" isn't.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

'''

def solution(A):
    num_open = 0
    for x in A:
        if x == '(':
            num_open += 1
        else:
            num_open -= 1
        if num_open < 0:
            return 0
    if num_open == 0:
        return 1
    else:
        return 0

print(solution('(()(())())'))
print(solution('())'))