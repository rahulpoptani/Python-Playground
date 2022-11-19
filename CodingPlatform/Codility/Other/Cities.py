'''
A network consisting of M cities and M-1 roads connecting them is given.
Cities are labelled with distinct integers with range [0..(M-1)]
Roads connect cities in such a way that each pair of distinct cities is connected either by a direct road or along a path consisting of direct roads.
There is exactly one way to reach any city from another city.
The number of roads traversed is the distance between the cities.

T[0] = 9
T[1] = 1
T[2] = 4
T[3] = 9
T[4] = 0
T[5] = 4
T[6] = 8
T[7] = 9
T[8] = 0
T[9] = 1

One of the city is capital and the goal is the count the number of cities position away from it.
if city 1 is capital then the cities positioned at various distance from the capital is:
    Cities 9        -> Distance 1
    Cities 0, 3, 7  -> Distance 2
    Cities 8, 4     -> Distance 3
    Cities 2, 5, 6  -> Distance 4

if T[P] = Q and P = Q, then P is capital
if T[P] = Q and P not= Q, then there is a direct road between P and Q

Return number of cities positioned at each distance 1,2,3,4..M-1

the function should return: [1, 3, 2, 3, 0, 0, 0, 0, 0]

Ref: https://leetcode.com/discuss/interview-question/795275/Codility-or-Python
'''



import collections

def solution(T):

    # find the capital
    capital = -1
    for i in range(0, len(T)):
        if i == T[i]:
            capital = i
            break
    
    # create adj list
    adj = collections.defaultdict(list)
    for k,v in enumerate(T):
        adj[k].append(v)
        adj[v].append(k)

    # visit set to maintain list of visited nodes
    visit = set([])

    q = collections.deque([])
    # initialize queue with the capital at distance 0.
    q.append((capital, 0))
    
    # create distance array
    D = [0] * (len(T) - 1)

    # perform bfs with following the distance
    while q:
        node, dist = q.popleft()
        D[dist] += 1
        visit.add(node)

        for nei in adj[node]:
            if nei not in visit:
                q.append((nei, dist+1))
    

    return D


if __name__ ==  "__main__":
    T = [9,1,4,9,0,4,8,9,0,1]
    answ = solution(T)
    print(answ)