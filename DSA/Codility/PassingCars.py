# An array with values 0 and 1 represent cars moving in left (0) or right(0) direction 
# Identify how many cars pass each other
# Example [0, 1, 0, 1, 1] 
# Index 0 has 3 cars (1) coming towards
# Index 2 has 2 cars (1) coming towards

def passing_cars(arr):
    cars_passed = 0
    for x in range(len(arr)):
        if arr[x] == 0:
            for y in range(x,len(arr)):
                if arr[y] == 1:
                    cars_passed += 1
    print(cars_passed)

passing_cars([0, 1, 0, 1, 1])


# Using Suffix Sum
# Array  = [0, 1, 0, 1, 1]
# Suffix = [3, 3, 2, 2, 1, 0]
# How Suffix sum is calculated? Get the last element (rightmost) from array and start adding the left elements 

def passing_cars2(arr):
    suffix_arr = [0] * (len(arr)+1)
    for x in range(len(arr)-1, -1, -1):
        suffix_arr[x] = arr[x] + suffix_arr[x+1]
    
    count = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            count += suffix_arr[i]
        if count > 1000000000: # Codility specific check
            return -1
    return count


print(passing_cars2([0, 1, 0, 1, 1]))