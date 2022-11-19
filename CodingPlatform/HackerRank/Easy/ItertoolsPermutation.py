'''
String Permutation
Input:
--------
HACK 2
Output:
---------
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
'''

from itertools import permutations

# value, size = input().split()

# perm = sorted(list(permutations(value, int(size))))

# for x in perm:
#     value = ''
#     for y in x:
#         value += y
#     print(value)


# List Permutation
# Comment above code

ll = [1,2,3,4]
llperm = list(permutations(ll, 2))
print(*llperm) # the start will explode the list of tuples. Can be used inside print function. Cannot be used while assignment

