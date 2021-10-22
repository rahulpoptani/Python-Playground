# Array consist of N different integers in range (1, (N+1))
# Exactly 1 element is missing
# Ex: [2,3,1,5], here 4 is missing

def solution(arr):
    first_element = 1
    last_element = len(arr)+1
    sum_ofall_element = (last_element * (last_element + first_element)) / 2
    for x in arr:
        sum_ofall_element = sum_ofall_element - x
    print(int(sum_ofall_element))

solution([2,3,1,5,4])