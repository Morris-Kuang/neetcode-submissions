import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        
        left = -stones[0]
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            left = -s1 - (-s2)
            heapq.heappush(stones, -left)
        
        return left
