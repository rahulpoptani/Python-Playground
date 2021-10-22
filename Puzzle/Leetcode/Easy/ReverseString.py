class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # Approach 1
        # def helper(left, right):
        #     if left < right:
        #         s[left], s[right] = s[right], s[left]
        #         helper(left + 1, right - 1)
        # helper(0, len(s)-1)

        # Approach 2
        left, right = 0, len(s)-1
        while (left < right):
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1


s = ["h","e","l","l","o"]
sol = Solution()
sol.reverseString(s)
print(s)