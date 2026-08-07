import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # tuple (dist, idx) and use minheap to sort

        info = []
        for i in range(len(points)):
            dist = (points[i][0]**2 + points[i][1]**2)**(1/2)
            t = (dist, i)
            info.append(t)

        heapq.heapify(info)
        
        res = []
        for i in range(k):
            element = heapq.heappop(info)
            res.append(points[element[1]])
        
        return res
        