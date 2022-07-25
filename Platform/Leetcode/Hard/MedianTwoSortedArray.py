'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00
Explanation: merged array = [1,2,3] and median is 2.

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Logic:
Divide both array such that right most element of left half of array 1 must be lesser than leftmost element of right half of array 2
and vice versa.
Array1: 1, 3, 4, 7, 10, 12
Array2: 2, 3, 6, 15

Array1 Left: 1, 3, 4        Array1 Right: 7, 10, 12
Array2 Left: 2, 3           Array2 Right: 6, 15
Here, 4 <= 6 and 3 <= 7 
Above condition is true, hence this is a valid partition between two array

Once Valid partition is determined
If length is Even after merging then take Maximum of right most element of Array1 Left and Array2 Left and take Minimum of left most element of Array1 Right and Array2 Right
max(4, 3) + min (7, 6) = 4 + 6 = 10 = 10/2 = 5
If length is Odd take take Maximum of right most element of Array1 Left and Array2 Left
'''
import sys
    

def findMedianSortedArrays(nums1, nums2, len1, len2):
    A, B = nums1, nums2
    total = len(nums1) + len(nums2)
    half = total // 2
    
    if len(B) < len(A):
        A, B = B, A
    
    l, r = 0, len(A) - 1
    while True:
        part1 = (l + r) // 2 # A
        part2 = half - part1 - 2 # B
    
        Aleft = A[part1] if part1 >= 0 else float("-infinity")
        Aright = A[part1 + 1] if (part1 + 1) < len(A) else float("infinity")
        Bleft = B[part2] if part2 >= 0 else float("-infinity")
        Bright = B[part2 + 1] if (part2 + 1) < len(B) else float("infinity")
    
        # partition is correct
        if Aleft <= Bright and Bleft <= Aright:
            # odd
            if total % 2:
                return min(Aright, Bright)
            # even
            return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = part1 - 1
        else:
            l = part1 + 1



arr1 = [1, 3, 4, 7, 10, 12]
arr2 = [2, 3, 6, 15]
lenarr1 = len(arr1)
lenarr2 = len(arr2)
print(findMedianSortedArrays(arr1, arr2, lenarr1, lenarr2))


arr1 = [1, 3]
arr2 = [2]
lenarr1 = len(arr1)
lenarr2 = len(arr2)
print(findMedianSortedArrays(arr1, arr2, lenarr1, lenarr2))


