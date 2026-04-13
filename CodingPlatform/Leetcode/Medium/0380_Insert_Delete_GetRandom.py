'''
Implement the RandomizedSet class:
RandomizedSet() Initializes the RandomizedSet object.
bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.
You must implement the functions of the class such that each function works in average O(1) time complexity.

Example 1:
Input
["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.
'''
from Common.Tags import DESIGN, HASHMAP, ARRAY
import random

class RandomizedSet:
    def __init__(self):
        self.val_to_idx = {}   # val -> index in array
        self.nums = []         # array of values

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.nums.append(val)
        self.val_to_idx[val] = len(self.nums) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        
        # Swap val with the last element, then pop
        idx = self.val_to_idx[val]
        last = self.nums[-1]
        
        self.nums[idx] = last
        self.val_to_idx[last] = idx
        
        self.nums.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)

# test cases
randomizedSet = RandomizedSet()
print(randomizedSet.insert(1))  # True
print(randomizedSet.remove(2))  # False
print(randomizedSet.insert(2))  # True
print(randomizedSet.getRandom())  # 1 or 2
print(randomizedSet.remove(1))  # True
print(randomizedSet.insert(2))  # False
print(randomizedSet.getRandom())  # 2