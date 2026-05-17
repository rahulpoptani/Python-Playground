'''
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
 

Example 1:
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
'''

from Common.Tags import DESIGN, HEAP
import heapq

# Approach: Two Heaps
# Split the stream into two halves:
#   - maxHeap (left half): largest element is at the top → gives the lower median candidate
#   - minHeap (right half): smallest element is at the top → gives the upper median candidate
#
# Python's heapq is a min-heap, so we negate values when pushing to maxHeap to simulate a max-heap.

class MedianFinder:

    def __init__(self):
        self.maxHeap = []
        self.minHeap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap, -num)

        # Give to minHeap if maxHeap's top is greater than minHeap's top
        if self.minHeap and self.maxHeap and (-self.maxHeap[0] > self.minHeap[0]):
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        # Balancing - Give to minHeap if maxHeap is larger than minHeap by more than 1
        if len(self.maxHeap) > len(self.minHeap) + 1:
            val = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, val)
        
        # Give to maxHeap if minHeap is larger than maxHeap
        if len(self.minHeap) > len(self.maxHeap):
            val = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -val)
        
        print(f"maxHeap: {self.maxHeap}, minHeap: {self.minHeap}")
    
    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0])/2

medianFinder = MedianFinder();
medianFinder.addNum(1);    # arr = [1]
medianFinder.addNum(2);    # arr = [1, 2]
print(medianFinder.findMedian()); # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    # arr[1, 2, 3]
print(medianFinder.findMedian()); # return 2.0