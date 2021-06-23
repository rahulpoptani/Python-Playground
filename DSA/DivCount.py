# An Array between number A and B, calculate number of elements divisble by K
# A = 4, B = 17, K = 3
# Array will be [4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# Elements divisble by K are [6,9,12,15]
# Trick: Take the first element and divide by K and ceil the number, take last element divide by K
# and floor the number
# First element = 4 / 3 = 1.33 ~ 2
# Last element = 17 / 3 = 5.66 ~ 5
# To find the number of such elements = last element - first element + 1
# 5 - 2 + 1 = 3

import math

def div_count(a,b,k):
    first_element = math.ceil(a/k)
    last_element = math.floor(b/k)
    return last_element - first_element + 1


print(div_count(6, 12, 2))