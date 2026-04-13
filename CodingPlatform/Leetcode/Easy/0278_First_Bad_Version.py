'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example 1:
Input: n = 5, bad = 4
Output: 4

Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.

Example 2:
Input: n = 1, bad = 1
Output: 1
'''

from Common.Tags import BINARY_SEARCH, GRIND_75 

def isBadVersion(version: int) -> bool:
    # This is a mock implementation of the isBadVersion API for testing purposes.
    # In a real scenario, this function would be provided by the system and would not be implemented by the user.
    bad_version = 4  # Example bad version for testing
    return version >= bad_version

def firstBadVersion(self, n: int) -> int:
    left, right = 1, n

    while left < right:
        mid = left + (right - left) // 2   # Avoids integer overflow

        if isBadVersion(mid):
            right = mid        # mid could be the answer; search left half
        else:
            left = mid + 1     # mid is good; first bad must be to the right

    return left                # left == right, converged on the first bad version

print(firstBadVersion(5))  # Output: 4

'''
Time        O(log n)    Halves the search space each step
Space       O(1)        Just two pointers
API calls   O(log n)    At most ⌊log₂n⌋ + 1 calls

Key invariant: The answer always lives in [lo, hi]. When lo == hi, there's only one candidate left — that's our answer.
'''