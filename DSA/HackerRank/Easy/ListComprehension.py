'''
Take 4 Inputs => X, Y, Z, N
Create all permutation of axis X, Y, Z such that the sum should NOT be equal to N
(i, j, k) Cordinates Condition: 0 <= i <= X, 0 <= j <= Y, 0 <= k <= Z
Input:
-------
1
1
1
2

Output:
--------
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    lst = [
        [x1,y1,z1] 
        for x1 in range(x+1) 
        for y1 in range(y+1) 
        for z1 in range(z+1) 
        if x1+y1+z1 != n
    ]
    print(lst)