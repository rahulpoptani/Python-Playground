# The slice can have a min length of 2
# The min avg slice has length of 2 or 3
# Return starting position of slice

import sys

def solution(arr):
    min_start_pos = 0
    min_element = sys.maxsize

    for x in range(len(arr)-2):
        avg2 = (arr[x] + arr[x+1]) / 2
        avg3 = (arr[x] + arr[x+1] + arr[x+2]) / 3

        current_min_avg = min(avg2, avg3)
        if current_min_avg < min_element:
            min_element = current_min_avg
            min_start_pos = x
    
    last2 = (arr[len(arr)-2] + arr[len(arr)-1]) / 2
    if last2 < min_element:
        min_element = last2
        min_start_pos = len(arr)-2
    
    print(min_start_pos)

solution([1, 2, 3, -8])