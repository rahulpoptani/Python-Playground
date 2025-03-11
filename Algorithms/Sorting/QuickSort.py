
'''
Quick Sort is a highly efficient divide-and-conquer sorting algorithm that:
    Picks a pivot element from the array.
    Partitions the array such that:
        Elements smaller than the pivot go to the left.
        Elements larger than the pivot go to the right.
    Recursively applies Quick Sort to both halves.
'''

def partition(l, r, nums):
    pivot = nums[r]
    pointer = l
    for x in range(l, r):
        if nums[x] <= pivot:
            nums[x], nums[pointer] = nums[pointer], nums[x]
            pointer += 1
    nums[pointer], nums[r] = nums[r], nums[pointer]
    return pointer

def quicksort(l, r, nums):
    if len(nums) == 1: return nums
    if l < r:
        pointer = partition(l, r, nums)
        quicksort(l, pointer-1, nums)
        quicksort(pointer+1, r, nums)
    return nums

arr1 = [4,5,1,2,3]
print(quicksort(0, len(arr1)-1, arr1))
