class Solution:
    from collections import Counter
    import heapq
    from collections import deque
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Dic "A": 4, MaxHeap [times]
        deque = [[times-1, next avail],] vs time, pop back to maxHeap if time arrives
        """

        count = Counter(tasks)
        maxHeap = []

        for key, value in count.items():
            maxHeap.append([-value, key])  # maxHeap
        heapq.heapify(maxHeap)


        t = 0
        q = deque()
        while maxHeap or q:
            t += 1
            
            if q and t >= q[0][1]:  # NEED TO FIRST CHECK and ADD to maxHeap!!
                cnt, time, key = q.popleft()
                heapq.heappush(maxHeap, [cnt, key])

            if maxHeap:
                cnt, key = heapq.heappop(maxHeap)
                if cnt + 1 < 0:
                    q.append([cnt + 1, t + n + 1, key]) # do not put into deque if cnt is the last element (no more to queue)
        
        return t




