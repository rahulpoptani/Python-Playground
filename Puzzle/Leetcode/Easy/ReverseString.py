""" Do not return anything, modify s in-place instead """
def reverseString(s):
    left, right = 0, len(s)-1
    while (left < right):
        s[left], s[right] = s[right], s[left]
        left, right = left+1, right-1


s = ["h","e","l","l","o"]
reverseString(s)
print(s)