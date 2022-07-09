
import heapq

H = [21,1,45,78,3,5]
K = [-x for x in H]

heapq.heapify(K)

print(K)

print(heapq.heappop(K))

print(K)