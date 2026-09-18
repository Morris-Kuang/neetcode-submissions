"""
heapq since we need in sorted order - reach O(log n) per added element

A = -1 
B = 5 9

check condition: if num > B min: pop one and let num in
if num < B min: throw to A 


TIME: addNum - O(log N), O(1) for findMedian
SPACE: O(n)
"""
import heapq
class MedianFinder:

    def __init__(self):
        self.former = [] # smallest - mid (maxHeap)
        self.latter = [] # mid - greatest (minHeap)
        
        

    def addNum(self, num: int) -> None:
        elements = len(self.former) + len(self.latter)
        
        if elements % 2 == 0:
            if elements > 0 and num > self.latter[0]:
                temp = heapq.heappop(self.latter)
                heapq.heappush(self.former, -temp)
                heapq.heappush(self.latter, num)
            else:
                heapq.heappush(self.former, -num)

        else: # elements % 2 == 1
            if num < -self.former[0]:
                temp = heapq.heappop(self.former)
                heapq.heappush(self.latter, -temp)
                heapq.heappush(self.former, -num)
            else:
                heapq.heappush(self.latter, num)


    def findMedian(self) -> float:

        if (len(self.former) + len(self.latter)) % 2 == 0:
            num1 = self.former[0]
            num2 = self.latter[0]
            return (-num1 + num2) / 2
        else:
            return -self.former[0]
        
        