class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        print('Processing Lists: {} and {}'.format(nums1, nums2))
        res_sorted = sorted(nums1 + nums2)
        res_sorted_length = len(res_sorted)
        res = 0.0
        if res_sorted_length % 2 == 1:
            mid_index = (res_sorted_length // 2)
            res = res_sorted[mid_index]
            print('Odd Digits: Mid Index {} | Result: {}'.format(mid_index, res))
        elif res_sorted_length % 2 == 0 and res_sorted_length > 1:
            mid_index_left = (res_sorted_length // 2) - 1
            mid_index_right = (res_sorted_length // 2)
            res = (res_sorted[mid_index_left] + res_sorted[mid_index_right]) / 2
            print('Even Digits: Mid Index Left: {} | Mid Index Right: {} | Result: {}'.format(mid_index_left, mid_index_right, res))
        print('Result is: {}'.format(res))
        return res

s = Solution()

print(s.findMedianSortedArrays([1,2], [3,4]))

# print(s.findMedianSortedArrays([1,3], [2]))

# print(s.findMedianSortedArrays([0, 0], [0, 0]))

# print(s.findMedianSortedArrays([], [1]))

# print(s.findMedianSortedArrays([2], []))