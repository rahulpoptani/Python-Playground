'''
Input:
-------
5
2 3 6 6 5
Output:
--------
5
Explanation:
-------------
List is [2, 3, 6, 6, 5]. The maximum score is 6 and second maximum is 5. Hence print 5 as runner-up score
'''


n = 5
arr = list(map(int, '2 3 6 6 5'.split()))
newlist = sorted(set(arr))
print(newlist[-2])