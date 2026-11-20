from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Topological Sort: In-bound and Out-bound, with BFS
        repeatedly takes courses that have zero prerequisites (in-bound)
        1. In-bound decrement by one if previous dependent node is put in queue
        2. when it reaches 0, allow to be put in queue
        3. If all courses can be taken -> no cycle, return true
           If some courses are never taken - cycle exists, return false

        use adjacency list to record the dependencies
        use an array to keep track indegree
        use finish to keep track how many taken
        """
        indegree = [0] * numCourses

        prereq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[p].append(c) # prereq p for course c
            indegree[c] += 1
        
        queue = deque()
        for n in range(numCourses):
            if indegree[n] == 0:
                queue.append(n)
        
        finish = 0 # keep track whether every class could be taken
        while queue:
            node = queue.popleft()
            finish += 1
            
            for nei in prereq[node]:
                indegree[nei] -= 1
                if indegree[nei] == 0: # officially unlocked!
                    queue.append(nei)

        return finish == numCourses

        
        
        