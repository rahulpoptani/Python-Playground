from heapq import heappush,heappop

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

# ['apple', 'orange', 'banana'] - 'apple' being the smallest comes to the front of the list to come out
print(fruits) 

heappop(fruits) # 'apple' removed

# ['banana', 'orange'] - 'banana' adjusted to become the smallest
print(fruits)