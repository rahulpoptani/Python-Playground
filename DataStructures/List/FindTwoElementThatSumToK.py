def find_sum(lst, k):
    lst.sort()
    l = 0
    r = len(lst)-1
    while(l <= r):
        if (lst[l] + lst[r] == k):
            return [lst[l],lst[r]]
        if (lst[l] + lst[r] < k):
            l += 1
        if (lst[l] + lst[r] > k):
            r -= 1

lst = [1,21,3,14,5,60,7,6]
k = 81

print(find_sum(lst,k))

# Time Complexity
# Linear scan takes O(n) and sort takes O(nlogn). Overall Time complexity = O(nlogn)
# Brute-force approach with 2 nested loops would have taken O(n square)
