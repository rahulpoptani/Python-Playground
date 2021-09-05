# Take a number and convert into binary
# Identify maximum number of 0 between two 1's
# Ex: 1041 Binary is 100000100001, here longest binary gap is 5

def solution(s):
    inbinary = bin(s).replace("0b","")
    max_zero = current_zero = 0
    for x in inbinary:
        if x == '1':
            max_zero = max(max_zero, current_zero)
            current_zero = 0
        else:
            current_zero += 1
    print(max_zero)

solution(1041)