class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        Cycle Detection - using DFS
        1. prereq points to course
        2. visiting set to track dfs path, 
        3. if a node traversed is alr in visiting => False
        4. if successfully process the courses, c be removed (mark as done)
        """
        prereq = {i:[] for i in range(numCourses)}
        for c, p in prerequisites:
            prereq[p].append(c) # prereq p for course c
        
        visiting = set()

        def dfs(p): # start dfs from prereq
            if p in visiting:
                return False
            
            if prereq[p] == []:
                return True
            
            visiting.add(p)
            for following in prereq[p]:
                if not dfs(following): # if dfs not True
                    return False
            visiting.remove(p) # remember to clear up for next iteration
            prereq[p] = [] # prereq sequence checked valid

            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True

