'''
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N
Example:
Number 9 has binary representation 1001 and contains a binary gap of length 2
Number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3
Number 20 has binary representation 10100 and contains one binary gap of length 1
Number 15 has binary representation 1111 and has no binary gaps
Number 32 has binary representation 100000 and has no binary gaps

Given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap
N is an integer within the range [1..2,147,483,647]
'''

def solution(N):
    inbinary = bin(N).replace("0b","")
    max_zero = current_zero = 0
    for x in inbinary:
        if x == '1':
            max_zero = max(max_zero, current_zero)
            current_zero = 0
        else:
            current_zero += 1
    return max_zero

print(solution(9))
print(solution(529))
print(solution(20))
print(solution(15))
print(solution(32))