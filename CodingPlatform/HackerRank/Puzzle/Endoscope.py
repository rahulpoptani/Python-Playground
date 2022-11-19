'''
https://www.hackerearth.com/problem/algorithm/question-7-4/

2
5 6 2 1 3
0 0 5 3 6 0
0 0 2 0 2 0
3 3 1 3 7 0
0 0 0 0 0 0
0 0 0 0 0 0
5 6 2 2 6
3 0 0 0 0 3
2 0 0 0 0 6
1 3 1 1 3 1
2 0 2 0 0 2
0 0 4 3 1 1

'''

class Node:
    def __init__(self,x,y,l):
        self.x = x
        self.y = y
        self.l = l

def valid(x,y): return x >= 0 and y >= 0 and x < MH and y < MW and Visited[x][y] != 1
def left(x,y): return Matrix[x][y] in [1,3,6,7]
def right(x,y): return Matrix[x][y] in [1,3,4,5]
def up(x,y): return Matrix[x][y] in [1,2,4,7]
def down(x,y): return Matrix[x][y] in [1,2,6,5]


for x in range(int(input().strip())):
    Matrix = []
    Visited = []
    MH,MW,EV,EH,EL = list(map(int, input().strip().split(" ")))
    Visited = [ MW*[0] for _ in range(MH) ]
    
    for y in range(MH):
        Matrix.append(list(map(int, input().strip().split(" "))))
    
    queue = [Node(EV,EH,EL)]

    scope = 0
    while queue:
        curr = queue.pop()
        Visited[curr.x][curr.y] = 1 # mark as visited
        if curr.l == 0: continue
        if Matrix[curr.x][curr.y] != 0: scope += 1
        # look left
        if valid(curr.x,curr.y-1) and left(curr.x,curr.y) and right(curr.x,curr.y-1):
            queue.insert(0,Node(curr.x,curr.y-1,curr.l-1))
            Visited[curr.x][curr.y-1] = 1 # no other valid condition should duplicate
        # look right
        if valid(curr.x,curr.y+1) and right(curr.x,curr.y) and left(curr.x,curr.y+1):
            queue.insert(0,Node(curr.x,curr.y+1,curr.l-1))
            Visited[curr.x][curr.y+1] = 1
        # look up
        if valid(curr.x-1,curr.y) and up(curr.x,curr.y) and down(curr.x-1,curr.y):
            queue.insert(0,Node(curr.x-1,curr.y,curr.l-1))
            Visited[curr.x-1][curr.y] = 1
        # look down
        if valid(curr.x+1,curr.y) and down(curr.x,curr.y) and up(curr.x+1,curr.y):
            queue.insert(0,Node(curr.x+1,curr.y,curr.l-1))
            Visited[curr.x+1][curr.y] = 1
    print(scope)

