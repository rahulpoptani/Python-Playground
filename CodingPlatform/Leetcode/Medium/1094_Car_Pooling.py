'''
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).
You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.
Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

Example 1:
Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false

Example 2:
Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
'''

from Common.Tags import ARRAY, SIMULATION, PREFIX_SUM
from typing import List
from collections import defaultdict

def carPooling(trips: List[List[int]], capacity: int) -> bool:
        events = defaultdict(int)
        
        for cap, start, end in trips:
            events[start] += cap
            events[end] -= cap
        
        current_capacity = 0
        for event in sorted(events.keys()):
            current_capacity += events[event]
            if current_capacity > capacity:
                return False
        
        return True

# test cases
print(carPooling([[2,1,5],[3,3,7]], 4)) # false
print(carPooling([[2,1,5],[3,3,7]], 5)) # true
